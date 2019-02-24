def purify(group):
  package = group[:] # or "package = list(group)"
  for number in group:
    if number % 2 != 0:
      package.remove(number)
  return package

print(purify([1, 2, 4, 4, 5, 7, 8, 9, 9, 6]))


def purifying(pack):
  for number in pack[:]:
    if number % 2 != 0:
      pack.remove(number)
  return pack

print(purifying([1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7]))


def purify(horde):
  return [number for number in horde if number % 2 == 0] 

print(purify([1, 2, 2, 3, 3, 6, 6]))


def removeEvenNumber(numbers):
  numbersCopy = numbers[:]
  for x in numbers:
    if x % 2 == 0:
      numbersCopy.remove(x)
  return numbersCopy

print(removeEvenNumber([1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7]))

def removeOdd(horde):
  return [number for number in horde if number % 2 == 0] 

print(removeOdd([1, 2, 2, 3, 5, 6, 8, 8, 3, 6, 6]))


def remove_even_number(numbers):
  digits = list(str(numbers))
  for x in digits:
    if x % 2 != 0:
      numbers.remove(x)
  return numbers

print(remove_even_number(2132345))
      






















