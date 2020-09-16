# Author: Evelyn Moore eim5178@psu.edu
# Collaborator:

def sum_n(n):
  if (n<=1):
    return n
  else:
    n = n%10
    return n + sum_n(n-1)
def run():
  n = int(input("Enter an int: "))
  nsum = sum_n(n)
  print(f"sum of the digits of {n} is {nsum}")
  
if __name__ == '__main__':
  run()