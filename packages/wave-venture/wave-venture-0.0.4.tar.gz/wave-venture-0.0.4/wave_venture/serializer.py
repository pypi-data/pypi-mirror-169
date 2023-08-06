import datetime

import numpy as np
import pandas as pd
import xarray as xr

from wave_venture import utils


def _decode_array_values(data):
    _type = data["_type"]

    if _type in {"number", "fraction", "degree", "radian", "boolean"}:
        return data["values"]
    elif _type == "complex":
        return np.array(data["real"]) + np.array(data["imag"]) * 1j
    elif _type == "string":
        return data["values"]
    elif _type == "datetime":
        return pd.to_datetime(data["epochs"], unit="s")
    else:
        raise NotImplementedError(data)


def decoder(obj):
    _type = obj.get("_type", None)  # safely get _type if it exists

    if _type == "datetime" and "epoch" in obj:
        return datetime.datetime.utcfromtimestamp(obj["epoch"])
    elif _type == "array":
        array = xr.Dataset(
            data_vars={
                name: (obj["dimensions"], _decode_array_values(data))
                for name, data in obj["fields"].items()
            },
            coords={
                name: _decode_array_values(data)
                for name, data in obj["indices"].items()
            },
        )
        for name in obj["indices"].keys():
            array[name].attrs["interpolation"] = obj["indices"][name].get("interpolation")
            array[name].attrs["_type"] = obj["indices"][name]["_type"]
        for name in obj["fields"].keys():
            array[name].attrs["_type"] = obj["fields"][name]["_type"]
        return array
    else:
        return obj


def _encode_array_values(xarray, *, name):
    # Get type
    try:
        _type = xarray.data_vars[name].attrs["_type"]
    except KeyError:
        _type = xarray.coords[name].attrs["_type"]

    # format values
    if (
        _type in {"number", "fraction", "degree", "radian"}
        and np.issubdtype(xarray[name].dtype, np.number)
    ):
        result = {"values": xarray[name].to_numpy().tolist()}
    elif (
        _type == "datetime"
        and xarray[name].dtype == np.dtype("<M8[ns]")
    ):
        result = {"epochs": (xarray[name].to_numpy().view(np.int64) / 10 ** 9).tolist()}
    elif _type == "string":
        result = {"values": list(map(str, xarray[name].to_numpy().tolist()))}
    elif (
        _type == "boolean"
        and np.issubdtype(xarray[name], np.dtype("bool"))
    ):
        result = {"values": xarray[name].to_numpy().tolist()}
    elif (
        _type == "complex"
        and np.issubdtype(xarray[name], np.dtype("complex"))
    ):
        result = {
            "real": xarray[name].real.to_numpy().tolist(),
            "imag": xarray[name].imag.to_numpy().tolist(),
        }
    else:
        raise NotImplementedError(f"Unable type {_type} on {xarray[name].dtype}")

    result = {**result, "_type": _type}

    if name in set(xarray.coords):
        if interpolation := xarray[name].attrs.get("interpolation"):
            result["interpolation"] = interpolation

    return result


def encoder(obj):
    if isinstance(obj, datetime.datetime) and utils.is_naive(obj):
        return {
            "_type": "datetime",
            "epoch": utils.to_epoch(obj),
        }
    elif isinstance(obj, datetime.datetime) and utils.is_utc(obj):
        return {
            "_type": "datetime",
            "epoch": utils.to_epoch(obj),
        }
    elif isinstance(obj, datetime.datetime):
        raise TypeError("Encountered unexpected timezone aware datetime.")
    elif isinstance(obj, complex):
        return {"_type": "complex", "real": obj.real, "imag": obj.imag}
    elif isinstance(obj, (np.ndarray, np.number)):
        return obj.tolist()
    elif isinstance(obj, xr.Dataset):
        return {
            "_type": "array",
            "fields": {
                column: _encode_array_values(obj, name=column)
                for column in obj.data_vars
            },
            "dimensions": list(obj.coords),
            "indices": {
                coord: _encode_array_values(obj, name=coord)
                for coord in list(obj.coords)
            },
        }
    else:
        raise ValueError(f"Can't encode object of type {type(obj).__name__}")
