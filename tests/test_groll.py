import tomli

from src.groll import groll


def test_version():
    with open("pyproject.toml", "rb") as f:
        metadata = tomli.load(f)
    assert groll.__version__ == metadata["tool"]["poetry"]["version"]


def test_get_dice():
    d1 = groll.get_dice("3d20")
    d2 = groll.get_dice("d4")
    assert d1.number == 3
    assert d1.sides == 20
    assert d2.number == 1
    assert d2.sides == 4


# def test_parse():
#     args = ("4", "+9")
#     assert groll.parse(args) == [4, "+", 9]
