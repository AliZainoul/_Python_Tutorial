def test_upper():
    assert 'hello'.upper() == 'HELLO'

def test_isupper():
    assert 'HELLO'.isupper()
    assert not 'Hello'.isupper()

if __name__ == '__main__':
    import pytest
    pytest.main()
