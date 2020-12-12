from common import SeatingSystem


if __name__ == "__main__":
    # O(s*n^2) time and O(n) space
    # with s: number of steps until convergence, n: number of points in grid 
    # Time complexity could be optimized by saving and reusing neighbors of each point
    seating_system = SeatingSystem(5, False)
    seating_system.run()
    print(seating_system.occupied)
