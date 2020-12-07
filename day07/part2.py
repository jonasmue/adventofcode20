from common import get_input


def required_bags():
    # O(k) time and space thanks to dynamic programming
    # with k: number of rules where our key is involved
    luggage_rules = get_input()
    bag_map = {}

    def traverse(key="shiny gold"):
        if key in bag_map.keys(): return bag_map[key]
        total = 0
        for container, amount in luggage_rules[key].items():
            total += amount
            total += amount * traverse(container)
        bag_map[key] = total
        return total

    return traverse()


if __name__ == "__main__":
    print(required_bags())
