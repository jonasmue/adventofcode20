from common import get_input

def potential_containers():
  luggage_rules = get_input()
  
  def traverse(needle = "shiny gold", visited=set()):
    total = 0
    for container in luggage_rules.keys():
      if container in visited: continue
      if needle in luggage_rules[container]:
        visited.add(container)
        total += 1
        total += traverse(container, visited)
    return total
    
  return traverse()
  
if __name__ == "__main__":
  print(potential_containers())
