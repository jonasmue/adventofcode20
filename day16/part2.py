from functools import reduce
from common import *


def possible_columns(range_list, tickets):
    cols = {col for col in range(len(tickets[0]))}
    valid_numbers = set()
    for rng in range_list: valid_numbers.update(rng)
    impossible = {col for ticket in tickets for col in cols if ticket[col] not in valid_numbers}
    return cols - impossible
    

def csp(field2col):
    
    removed_cols = set()
    
    def is_complete():
        for v in field2col.values():
            if len(v) > 1: return False
        return True
        
    def recurse():
        # Recursively remove all impossible columns from set of possible columns
        if is_complete(): return
        for field, cols in field2col.items():
            if len(cols) == 1:
                col = next(iter(cols))
                if col in removed_cols:
                    continue
                for other_field, other_cols in field2col.items():
                    if other_field == field: continue
                    if col in other_cols:
                        other_cols.remove(col)
                removed_cols.add(col)   
        recurse()  
    
    recurse()


def assign_fields(fields, nearby_tickets):
    tickets, _ = valid_tickets(fields, nearby_tickets)
    field2col = {}
    for key, range_list in fields.items():
        field2col[key] = possible_columns(range_list, tickets)
    csp(field2col)
    return field2col
    

if __name__ == "__main__":
    fields, my_ticket, nearby_tickets = get_input()
    assigned = assign_fields(fields, nearby_tickets)
    prod = lambda a, b: a * b
    cols = [my_ticket[col.pop()] for k, col in assigned.items() if k.startswith("departure")]
    print(reduce(prod, cols))    
