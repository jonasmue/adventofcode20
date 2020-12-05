from common import highest_id
  
if __name__ == "__main__":
  # O(n) time and space
  # Length of seat codes is constant → conversion code to id is constant
  # Space could be constant by not saving ids in array, but not done for reusability
  print(highest_id())
