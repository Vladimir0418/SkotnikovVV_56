import pytest

def zap(s,b):
    
    return str(s+b)


def test_zap1():
    assert zap("vova", "vova") == "vovavova"


@pytest.mark.parametrize("s, b, c", [("spam", "spam", "spamspam"),
                                    ("vova", "vova", "vovavova")])
def test_zap2(s, b, c):
    assert zap(s, b) == c

def test_zap3():
    try:
        assert zap("vova", "vova") == "k"
    except AssertionError:
        pass


def zaplist(s, b):
	if (s == b):
		return True


def test_zaplist1():
	assert zaplist([1,2,3], [1,2,3]) == True


@pytest.mark.parametrize("s, b", [[7,7],
	["x", "x"]])
def test_zaplist2(s, b):
    assert zaplist(s, b) == True


def test_zaplist3():
	try:
	    assert zaplist(["x","y","z","z"],["t","o","t","o"]) == True 
	except AssertionError:
		pass