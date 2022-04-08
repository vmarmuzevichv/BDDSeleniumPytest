
'''@pytest.mark.sanity
def test_00():
    num = 9/4
    s1 = "I like nexient"
    assert  str(num) == "2.25"
    assert s1 == "I like nexient"
    assert s1 + str(num) == "I like nexient2.25"

def test_01():
    letters = "asdasdasdasdasdasd"
    assert  letters[0] == "a"
    assert  letters[-1] == "d"

@pytest.mark.sanity
def test_02():
    letters = "asdasdasdasdasdxyi"
    assert  len(letters) == 32

@pytest.mark.sanity
@pytest.mark.str
def test_03():
    letters = "asdasdasdasdasdxyi"
    assert letters[:] == letters
    assert letters[10:] == "sdasdxyi"
'''

print('Hello')
