
from class_under_test import ClassUnderTest

def test_equals():
    myClass = ClassUnderTest(304)
    myOtherClass = ClassUnderTest(304);
    assert myClass.equals(myOtherClass) == True

    myOtherClass = ClassUnderTest(123);
    assert myClass.equals(myOtherClass) == False