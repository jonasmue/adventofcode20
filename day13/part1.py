from common import get_input


def get_result():
    # O(n) time and space
    timestamp, buses = get_input()
    buses = [int(b) for b in buses if b != "x"]

    best_departure = best_bus = None
    for bus in buses:
        rest = timestamp % bus
        prev_departure = timestamp - rest
        next_departure = prev_departure + bus
        if best_departure is None or next_departure < best_departure:
            best_departure = next_departure
            best_bus = bus
    
    return (best_departure - timestamp) * best_bus


if __name__ == "__main__":
    print(get_result())
