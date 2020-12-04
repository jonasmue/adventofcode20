from common import count_valid

REQUIRED_FIELDS = {
  "byr": lambda _: True,
  "iyr": lambda _: True,
  "eyr": lambda _: True,
  "hgt": lambda _: True,
  "hcl": lambda _: True,
  "ecl": lambda _: True,
  "pid": lambda _: True,
  }

if __name__ == "__main__":
  print(count_valid(REQUIRED_FIELDS))
