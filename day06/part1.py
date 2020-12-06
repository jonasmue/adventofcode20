from common import get_input

def union_count():
  # O(n*a) time and O(n) space
  # with n: number of passengers, a: longest answer set
  return sum([len(set.union(*group)) for group in get_input()])
  
if __name__ == "__main__":
  print(union_count())
