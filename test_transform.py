from transform import clean_numbers, average, total

def test_clean_numbers():
    result = clean_numbers([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]

def test_average():
    result = average([2, 4, 6])
    assert result == 4

def test_total():
    result = total([1, 2, 3])
    assert result == 6
