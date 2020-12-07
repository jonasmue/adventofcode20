from common import get_input

def required_bags():
  luggage_rules = get_input()
  
  def traverse(needle = "shiny gold"):
    total = 0
    for container, amount in luggage_rules[needle].items():
      total += amount
      total += amount * traverse(container)
    return total
  
  return traverse()
  
if __name__ == "__main__":
  print(required_bags())
