import re
from common import count_valid

def match_num(num_str, min, max):
  try:
    num = int(num_str)
    return min <= num and num <= max
  except ValueError:
    return False

def match_byr(byr):
  return match_num(byr, 1920, 2002)

def match_iyr(iyr):
  return match_num(iyr, 2010, 2020)
    
def match_eyr(eyr):
  return match_num(eyr, 2020, 2030)

def match_hgt(hgt):
  unit = hgt[-2:]
  value = hgt[:-2]
  if unit == "in": return match_num(value, 59, 76)
  elif unit == "cm": return match_num(value, 150, 193)
  else: return False
  
def match_hcl(hcl):
  return len(hcl) == 7 and bool(re.match("\#([0-9a-f]){6}", hcl))

def match_ecl(ecl):
  return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def match_pid(pid):
  return len(pid) == 9 and bool(re.match("\d{9}", pid))

REQUIRED_FIELDS = {
  "byr": match_byr,
  "iyr": match_iyr,
  "eyr": match_eyr,
  "hgt": match_hgt,
  "hcl": match_hcl,
  "ecl": match_ecl,
  "pid": match_pid
  }

if __name__ == "__main__":
  print(count_valid(REQUIRED_FIELDS))
