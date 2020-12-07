from common import get_input


def potential_containers():
    # O(n) time and space
    # with n: number of rules (bag types) → we visit each rule at most once
    luggage_rules = get_input()

    def traverse(key="shiny gold", visited=None):
        if visited is None: visited = set()
        total = 0
        for container in luggage_rules.keys():
            if container in visited: continue
            if key in luggage_rules[container]:
                visited.add(container)
                total += 1
                total += traverse(container, visited)
        return total

    return traverse()


if __name__ == "__main__":
    print(potential_containers())
