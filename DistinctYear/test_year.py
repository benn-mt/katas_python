from year import Year

def test_single_digit_years_are_always_distinct_years():
    year = Year(2)
    assert year.isDistinct() == True
    year = Year(9)
    assert year.isDistinct() == True

def test_two_digit_years_wih_different_digits_are_distinct():
    year = Year(12)
    assert year.isDistinct() == True
    year = Year(15)
    assert year.isDistinct() == True

def test_two_digit_years_with_same_digit_are_not_distinct():
    year = Year(11)
    assert year.isDistinct() == False
    year = Year(44)
    assert year.isDistinct() == False
    
    
def test_three_digit_years_with_at_least_2_same_digits_are_not_distinct():
    year = Year(111)
    assert year.isDistinct() == False
    year = Year(112)
    assert year.isDistinct() == False
    year = Year(211)
    assert year.isDistinct() == False
    year = Year(121)
    assert year.isDistinct() == False

def test_examples_from_kata():
    year = Year(1987)
    assert year.isDistinct() == True
    year = Year(2013)
    assert year.isDistinct() == True

def test_years_are_equal():
    assert Year(1906) == Year(1906)
    assert Year(1908) != Year(1907)

def test_can_get_next_distinct_year():
     year = Year(1906)
     assert year.getNextDistinctYear() == Year(1907)
     year = Year(1907)
     assert year.getNextDistinctYear() == Year(1908)
     year = Year(1906)
     assert year.getNextDistinctYear().getNextDistinctYear() == Year(1908)
     year = Year(1908)
     assert year.getNextDistinctYear() == Year(1920)
     year = Year(1987)
     assert year.getNextDistinctYear() == Year(2013)
