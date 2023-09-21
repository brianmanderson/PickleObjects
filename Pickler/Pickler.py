import os
import pickle
from typing import Union


def load_obj(path: Union[str, bytes, os.PathLike]):
    if path[-4:] != '.pkl':
        path += '.pkl'
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    else:
        out = {}
        return out


def save_obj(obj, path: Union[str, bytes, os.PathLike]):
    if path[-4:] != '.pkl':
        path += '.pkl'
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.DEFAULT_PROTOCOL)
    return None


if __name__ == '__main__':
    pass
