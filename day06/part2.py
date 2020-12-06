from common import get_input

def intersection_count():
  # O(n*a) time and space
  # with n: number of passengers, a: longest answer set
  return sum([len(set.intersection(*group)) for group in get_input()])

if __name__ == "__main__":
  print(intersection_count())
