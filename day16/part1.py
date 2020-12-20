from common import *


if __name__ == "__main__":
    fields, _, nearby_tickets = get_input()
    _, scan_error_rate = valid_tickets(fields, nearby_tickets)
    print(scan_error_rate)
