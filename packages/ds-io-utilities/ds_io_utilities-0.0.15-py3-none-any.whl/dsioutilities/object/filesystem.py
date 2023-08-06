from ..utils import get_asset_property

def get_path(name):

    metadata = {"type": "filesystem"}

    return get_asset_property(name), metadata
