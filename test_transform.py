from transform import clean_numbers

def test_clean_numbers():
    result = clean_numbers([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]
