try:
    from fime._version import __version__, __version_tuple__
except ImportError:
    __version__ = version = '1.0.0.dev0'
    __version_tuple__ = version_tuple = (1, 0, 0, 'dev0')
