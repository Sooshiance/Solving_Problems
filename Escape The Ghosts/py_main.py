def escapeGhosts(ghosts, target):
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    player_distance = manhattan_distance([0, 0], target)

    for ghost in ghosts:
        if manhattan_distance(ghost, target) <= player_distance:
            return False

    return True


# Test cases
print(escapeGhosts([[1, 0], [0, 3]], [0, 1]))
print(escapeGhosts([[1, 0]], [2, 0]))
print(escapeGhosts([[2, 0]], [1, 0]))
