
defaultLimit = 25
maxLimit = 100

class LimitParser():

  def parse(self,numberToClean):
    valueToReturn = defaultLimit

    if numberToClean:

      if numberToClean:
        numberToClean = numberToClean.strip()

      if numberToClean.isdigit():
        parsedNumber = int(numberToClean)

        if parsedNumber > 0:
          valueToReturn = parsedNumber
        if parsedNumber > maxLimit:
          valueToReturn = maxLimit

    return valueToReturn
