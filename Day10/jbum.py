import math

def main():
  n = int(input())
  m = int(math.ceil(math.log2(n)))
  x = [1] * m
  for i in range(m-1, -1, -1):
    if n % 2 == 1:
      x[i] = n
      n = n // 2
    else:
      n = n // 2
  print(m)
  for i in range(m):
    print(x[i])

if __name__ == '__main__':
  main()