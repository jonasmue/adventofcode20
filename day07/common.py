def get_input():
  with open("input.txt") as f:
    luggage_rules = {}
    for line in f.read().splitlines():
      linesplit = line.split("contain")
      container = " ".join(linesplit[0].split()[:2])
      content = {}
      for item in linesplit[1].split(","):
        try: amount = int(item.split()[0])
        except ValueError: continue
        bag = " ".join(item.split()[1:3])
        content[bag] = amount
      luggage_rules[container] = content
    return luggage_rules
