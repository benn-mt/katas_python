class Year:
    def __init__(self, yearAsNumber):
        self._yearAsNumber = yearAsNumber
    
    def isDistinct(self):
        yearAsString = str(self._yearAsNumber)
        uniqueDigitList = list()
        for digit in yearAsString:
            if digit not in uniqueDigitList:
                uniqueDigitList.append(digit)
        
        return len(uniqueDigitList) == len(yearAsString)

    # override == operator
    def __eq__(self, other):
        return self._yearAsNumber == other._yearAsNumber
    
    def getNextDistinctYear(self):
        nextYear = Year(self._yearAsNumber + 1)
        while nextYear.isDistinct() is False:
            nextYear = Year(nextYear._yearAsNumber + 1)
        
        return nextYear