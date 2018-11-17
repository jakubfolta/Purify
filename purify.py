def purify(group):
  package = group[:] # or "package = list(group)"
  for number in group:
    if number % 2 != 0:
      package.remove(number)
  return package

print(purify([1, 2, 4, 4, 5, 7, 8, 9, 9, 6]))
