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
  
