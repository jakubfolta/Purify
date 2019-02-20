def purge(numbers):
  for digit in numbers[:]:
    if digit % 2 != 0:
      numbers.remove(digit)
  return numbers

print(purge([1, 2, 2, 3, 3, 4, 5, 5, 7, 8, 8]))


def purging(numbers):
  digits = numbers[:]
  for character in digits:
    if character % 2 != 0:
      numbers.remove(character)
  return numbers

print(purging([2, 3, 3, 4, 6, 7, 7, 9, 8, 8, 9]))
  
def removeEvenNumbers(numbers):
  for digit in numbers[:]:
    if digit % 2 != 0:
      numbers.remove(digit)
  return numbers

print(removeEvenNumbers([1, 2, 4, 4, 9, 4, 3, 5, 7, 8, 8]))

def displayOddNumbers(number):
  return ', '.join([str(x) for x in number if x % 2 != 0])

print(displayOddNumbers([1, 2, 4, 4, 9, 4, 3, 5, 7, 8, 8]))

def removeOddNumber(numbers):
  secondSet = numbers[:]
  for x in numbers:
    if x % 2 == 0:
      secondSet.remove(x)
  return(secondSet)

print(removeOddNumber([1, 3, 2, 1, 3, 8, 6, 9, 5, 4]))
    

