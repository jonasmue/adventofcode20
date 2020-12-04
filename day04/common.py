import re

def is_passport_valid(passport, required_fields):
  for field_name, policy in required_fields.items():
    if not field_name in passport.keys(): return False
    if not policy(passport[field_name]): return False
  return True
  
def count_valid(required_fields):
  # Time: O(f*n), f: number of required fields, n: number of passports
  # Space: O(1)
  return sum(map(lambda p: is_passport_valid(p, required_fields), get_input()))
        
def get_input():
  with open("input.txt") as f:
    passport_chunks = f.read().split("\n\n")
    passports = []
    for chunk in passport_chunks:
      passport_raw = chunk.split()
      passports.append({item.split(":")[0]:item.split(":")[1] for item in passport_raw})
    return passports
      
