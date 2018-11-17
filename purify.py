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
