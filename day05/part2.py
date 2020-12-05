from common import all_ids, lowest_id, highest_id

def missing_id():
  # O(n) time and space
  # Length of seat codes is constant → conversion code to id is constant
  low = lowest_id()
  high = highest_id()
  expected_values = set([i for i in range(low, high + 1)])
  for id in all_ids():
    expected_values.remove(id)
  return expected_values.pop()

if __name__ == "__main__":
  print(missing_id())
