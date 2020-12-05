def to_binary(code, one_char):
  result = 0
  for char in code:
    result = result << 1
    result |= (char == one_char)
  return result

def get_col(code):
  col_code = code[7:]
  col = to_binary(col_code, "R")
  return col
  
def get_row(code):
  row_code = code[:7]
  row = to_binary(row_code, "B")
  return row

def get_seat_id(code):
  return get_row(code) * 8 + get_col(code)

def all_ids():
  return [get_seat_id(code) for code in get_input()]
  
def highest_id():
  return max(all_ids())
  
def lowest_id():
  return min(all_ids())

def get_input():
  with open("input.txt") as f:
    return f.read().splitlines()
