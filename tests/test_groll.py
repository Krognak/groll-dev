import tomli

from src.groll import groll


def test_version():
    with open("pyproject.toml", "rb") as f:
        metadata = tomli.load(f)
    assert groll.__version__ == metadata["tool"]["poetry"]["version"]
