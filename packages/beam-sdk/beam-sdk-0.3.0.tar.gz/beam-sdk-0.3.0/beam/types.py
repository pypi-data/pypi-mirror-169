import base64
import builtins
import io
import json
import os
from abc import ABC, abstractmethod
from importlib import import_module


class InvalidTypeException(Exception):
    def __init__(self, msg, errors=None):
        super().__init__(msg)
        self.msg = msg
        self.errors = errors


class InvalidPayloadException(Exception):
    def __init__(self, msg, errors=None):
        super().__init__(msg)
        self.msg = msg
        self.errors = errors


class ModelTypeSerializer(ABC):
    def __init__(self, *args, **kwargs):
        return self.define(*args, **kwargs)

    @abstractmethod
    def define(self, *args, **kwargs):
        pass

    @abstractmethod
    def schema(self):
        pass

    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass


class FloatType(ModelTypeSerializer):
    def define(self):
        pass

    def schema(self):
        return {"type": "float"}

    def serialize(self, obj):
        try:
            output = float(obj)
        except ValueError:
            raise InvalidTypeException("invalid_float_value")

        return output

    def deserialize(self, data):
        try:
            obj = float(data)
        except ValueError:
            raise InvalidTypeException("invalid_float_value")

        return obj


class StringType(ModelTypeSerializer):
    def define(self, max_length=None):
        self.max_length = max_length

    def schema(self):
        return {"type": "string", "max_length": self.max_length}

    def serialize(self, obj):
        output = str(obj)

        if self.max_length:
            if len(output) > self.max_length:
                raise InvalidTypeException("invalid_string_too_long")

        return output

    def deserialize(self, data):
        obj = str(data)

        if self.max_length:
            if len(obj) > self.max_length:
                raise InvalidTypeException("invalid_string_too_long")

        return obj


class JsonType(ModelTypeSerializer):
    def define(self):
        pass

    def schema(self):
        return {"type": "json"}

    def serialize(self, obj):
        if not isinstance(obj, dict) and not isinstance(obj, list):
            raise InvalidTypeException("invalid_json_type")

        try:
            output = json.loads(json.dumps(obj))
        except TypeError:
            raise InvalidTypeException("invalid_json")

        return output

    def deserialize(self, data):
        if isinstance(data, str):
            try:
                obj = json.loads(data)
            except ValueError:
                raise InvalidTypeException("invalid_json_str")
        elif isinstance(data, dict) or isinstance(data, list):
            obj = data
        else:
            raise InvalidTypeException("invalid_json")

        return obj


class ImageType(ModelTypeSerializer):
    def define(self, size=None, mode=None, raw=False):
        self.size = size
        self.mode = mode
        self.raw = raw

    def schema(self):
        return {
            "type": "image",
            "size": list(self.size) if self.size is not None else None,
            "mode": str(self.mode) if self.mode is not None else None,
            "raw": self.raw,
        }

    def serialize(self, obj):
        try:
            PIL_Image = import_module("PIL.Image")
        except ModuleNotFoundError:
            raise RuntimeError("pillow_required_for_image_inputs")

        # Load image from disk
        if isinstance(obj, str) and os.path.isfile(obj):
            obj = PIL_Image.open(obj)

        # Load image from base64
        elif isinstance(obj, str):
            base64_data = obj

            if "," in base64_data:
                base64_data = obj.split(",")[1]

            obj = PIL_Image.open(io.BytesIO(base64.b64decode(base64_data)))

        if self.size is not None and obj.size != self.size:
            raise InvalidTypeException("invalid_image_size")

        if self.mode is not None and obj.mode != self.mode:
            raise InvalidTypeException("invalid_image_mode")

        buffer = io.BytesIO()
        obj.save(buffer, format="PNG")
        output = base64.b64encode(buffer.getvalue()).decode("ascii")
        return output

    def deserialize(self, data):
        if self.raw:
            return str(data)

        try:
            PIL_Image = import_module("PIL.Image")
        except ModuleNotFoundError:
            raise RuntimeError("pillow_required_for_image_inputs")

        if "," in data:
            data = data.split(",")[1]

        obj = PIL_Image.open(io.BytesIO(base64.b64decode(data)))

        if self.size is not None and obj.size != self.size:
            raise InvalidTypeException("invalid_image_size")

        if self.mode is not None and obj.mode != self.mode:
            raise InvalidTypeException("invalid_image_mode")

        return obj


class BinaryType(ModelTypeSerializer):
    def define(self):
        pass

    def schema(self):
        return {"type": "binary"}

    def serialize(self, obj):
        # Load binary from disk
        if isinstance(obj, str) and os.path.isfile(obj):
            with open(obj, "rb") as f:
                obj = f.read()

        try:
            output = base64.b64encode(obj).decode("ascii")
        except TypeError:
            raise InvalidTypeException("invalid_binary_data")

        return output

    def deserialize(self, data):
        try:
            return io.BytesIO(base64.b64decode(data)).getvalue()
        except TypeError:
            raise InvalidTypeException("invalid_binary_data")


class NumpyType(ModelTypeSerializer):
    def define(self, shape=None, dtype=float):
        self.shape = shape
        if isinstance(dtype, type):
            self.dtype = dtype
        elif isinstance(dtype, str):
            self.dtype = getattr(builtins, dtype)
        else:
            raise InvalidTypeException("invalid_numpy_type")

    def schema(self):
        return {
            "type": "numpy",
            "shape": list(self.shape) if self.shape is not None else None,
            "dtype": self.dtype.__name__ if self.dtype is not None else None,
        }

    def serialize(self, obj):
        if self.shape is not None and obj.shape != self.shape:
            raise InvalidTypeException("invalid_numpy_shape")

        if self.dtype is not None:
            obj = obj.astype(self.dtype)

        return obj.tolist()

    def deserialize(self, data):
        try:
            np = import_module("numpy")
        except ModuleNotFoundError:
            raise RuntimeError("numpy_required_for_numpy_inputs")

        obj = np.array(data, dtype=self.dtype)

        errors = []
        if self.shape is not None and obj.shape != self.shape:
            errors = ["invalid_shape"]

        if errors:
            raise InvalidTypeException("invalid_numpy_shape", errors=errors)

        return obj


class DataframeType(ModelTypeSerializer):
    def define(self, max_rows=None, max_cols=None):
        self.max_rows = max_rows
        self.max_cols = max_cols

    def schema(self):
        return {
            "type": "dataframe",
            "max_rows": self.max_rows,
            "max_cols": self.max_cols,
        }

    def serialize(self, obj):
        return obj.to_dict()

    def deserialize(self, data):
        try:
            pd = import_module("pandas")
        except ModuleNotFoundError:
            raise RuntimeError("pandas_required_for_dataframe_inputs")

        if isinstance(data, str):
            try:
                obj = pd.read_json(data)
            except ValueError:
                raise InvalidTypeException("invalid_dataframe_str")
        elif isinstance(data, dict):
            try:
                obj = pd.DataFrame.from_dict(data)
            except ValueError:
                raise InvalidTypeException("invalid_dataframe_dict")
        elif isinstance(data, pd.DataFrame):
            return data
        else:
            raise InvalidTypeException("invalid_dataframe")

        return obj


class TensorType(ModelTypeSerializer):
    def define(self, shape=None, dtype=float):
        self.shape = shape
        self.dtype = dtype

    def schema(self):
        return {
            "type": "tensor",
            "shape": list(self.shape) if self.shape is not None else None,
            "dtype": self.dtype.__name__ if self.dtype is not None else None,
        }

    def serialize(self, obj):
        if self.shape is not None and obj.shape != self.shape:
            raise InvalidTypeException("invalid_tensor_shape")

        if self.dtype is not None:
            obj = obj.to(self.dtype)

        return obj.tolist()

    def deserialize(self, data):
        try:
            torch = import_module("torch")
        except ModuleNotFoundError:
            raise RuntimeError("torch_required_for_tensor_inputs")

        obj = torch.tensor(data)
        obj = obj.to(self.dtype)

        if self.shape is not None and obj.shape != self.shape:
            raise InvalidTypeException("invalid_tensor_shape")

        return obj


class Types:
    Float = "float"
    String = "string"
    Json = "json"
    NumpyArray = "numpy"
    Dataframe = "dataframe"
    Tensor = "tensor"
    Image = "image"
    Binary = "binary"

    @staticmethod
    def to_list():
        t_list = []
        type_dict = vars(Types)

        for var_key in type_dict:
            if var_key[0].isupper():
                t_list.append(type_dict[var_key])

        return t_list


type_registry = {
    Types.Float: FloatType,
    Types.String: StringType,
    Types.Json: JsonType,
    Types.NumpyArray: NumpyType,
    Types.Dataframe: DataframeType,
    Types.Tensor: TensorType,
    Types.Image: ImageType,
    Types.Binary: BinaryType,
}


class PythonVersion:
    Python36 = "python3.6"
    Python37 = "python3.7"
    Python38 = "python3.8"


class OutputType:
    Directory = "directory"
    File = "file"
