
__all__ = [
    "BaseConfig",
]


class BaseConfig:

    def __init__(self, **data) -> None:
        for key in data:
            key_type = self.__annotations__.get(key, None)
            if not key_type:
                raise KeyError(f"key '{key}' not exists in class {self.__class__.__name__}")
            # only support List in config
            if hasattr(key_type, "__origin__") and key_type.__origin__ == list:
                key_type = key_type.__args__[0]
                for elem in data[key]:
                    if not isinstance(elem, key_type):
                        raise ValueError(f"expected elem type '{key_type}' but got '{type(elem)}'")
            else:
                if not isinstance(data[key], key_type):
                    raise ValueError(f"value type of key '{key}' must be {key_type}")
            setattr(self, key, data[key])
        for key in self.__annotations__:
            if key not in self.__dict__:
                setattr(self, key, getattr(self.__class__, key))

    @classmethod
    def from_dict(cls, kwconfigs: dict):
        for key in kwconfigs:
            key_type = cls.__annotations__.get(key, None)
            if not key_type:
                raise KeyError(f"key '{key}' not exists in class {cls.__name__}")
            # support list of items
            if hasattr(key_type, "__origin__") and key_type.__origin__ == list:
                key_type = key_type.__args__[0]
                if issubclass(key_type, BaseConfig):
                    kwconfigs[key] = [key_type.from_dict(it) for it in kwconfigs[key]]
            elif issubclass(key_type, BaseConfig):
                kwconfigs[key] = key_type.from_dict(kwconfigs[key])
        return cls(**kwconfigs)
