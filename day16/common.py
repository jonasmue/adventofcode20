def get_input():
    
    def parse_ticket(line):
        return [int(num) for num in line.split(",")]

    def parse_range(text, n):
        rng = text.split("or")[n].strip()
        start = int(rng.split("-")[0])
        end = int(rng.split("-")[1])
        return range(start, end + 1)
        
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
        fields = {}
        for line in groups[0].splitlines():
            split = line.split(":")
            name = split[0]
            ranges = parse_range(split[1], 0), parse_range(split[1], 1)
            fields[name] = ranges    
        my_ticket = parse_ticket(groups[1].splitlines()[1])
        nearby_tickets = [parse_ticket(line) for line in groups[2].splitlines()[1:]]
        return fields, my_ticket, nearby_tickets

 
def invalid_values(ticket, valid_numbers):
    return [num for num in ticket if num not in valid_numbers]


def valid_numbers(fields):
    valid = set()
    for ranges in fields.values():
        for r in ranges:
            valid.update(r)
    return valid


def valid_tickets(fields, nearby_tickets):
    valid_tickets = []
    scan_error_rate = 0
    for ticket in nearby_tickets:
        invalid = invalid_values(ticket, valid_numbers(fields))
        if len(invalid): scan_error_rate += sum(invalid)
        else: valid_tickets.append(ticket)
    return valid_tickets, scan_error_rate
