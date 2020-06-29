from ps2b import solve

# find the highest unsolvable combination of sizes

n = 6
consecutive = 0
last = 6

while consecutive < 6:
  s = solve(n)
  if s == (None, None, None):
    consecutive = 0
    last = n
  else:
    consecutive += 1
  n += 1

print('Highest unsolvable number of nuggets with combination of sizes: ', last)

