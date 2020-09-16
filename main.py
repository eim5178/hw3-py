# Author: Evelyn Moore eim5178@psu.edu
# Collaborator:


def run():
  n = int(input("Enter an int: "))
  n_sum = digit_sum(n)
  print(f"The sum is {n_sum}")

def digit_sum(n):
  if (n<10):
    return n
  else:
    l = n % 10
    d = n//10
    n = l + digit_sum(d)
    return n

if __name__ == '__main__':
  run()

