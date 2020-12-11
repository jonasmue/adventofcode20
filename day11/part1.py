from common import SeatingSystem


if __name__ == "__main__":
    # O(s*n) time and O(n) space
    # with s: number of steps until convergence, n: number of points in grid
    seating_system = SeatingSystem(4, True)
    seating_system.run()
    print(seating_system.occupied)
