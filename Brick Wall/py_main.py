from collections import defaultdict


def leastBricks(wall):
    edges = defaultdict(int)
    for row in wall:
        edge = 0
        for brick in row[:-1]:
            edge += brick
            edges[edge] += 1
    return len(wall) - max(edges.values(), default=0)


# Test cases
wall1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall1))

wall2 = [[1],[1],[1]]
print(leastBricks(wall2))
