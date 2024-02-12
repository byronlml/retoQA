def config(name, default=None):

    if name in _config:
        return _config[name]
    return default


_config = {
    "BASE_URL": "https://www.saucedemo.com/"
}
