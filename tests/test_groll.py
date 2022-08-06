from src.groll import groll


def test_version():
    assert groll.__version__ == "0.0.1"


def test_parser():
    assert groll.parse(["4", "+9"]) == [4, "+", 9]


def test_math_eval():
    assert groll.eval_maths([1, "+", 2]) == 3
    assert groll.eval_maths([1, "-", 3]) == -2
    assert groll.eval_maths([4, "+", 7, "-", 8]) == 3
    assert groll.eval_maths([8, "/", 2]) == 4
