from collections import defaultdict
from platform import node

def find_best_team(reports, scores):
    def dfs(node):
        nonlocal ans
        if not node:
            return (0, 0)
        score = scores[node]
        for child in children[node]:
            child_score, child_players = dfs(child)
            score += child_score
            players += child_players

        average_score = score / players
        ans = max(ans, average_score)
        return score, players

    in_degree = [0] * len(scores)
    children = defaultdict(list)
    for manager, player in reports:
        in_degree[player] += 1
        children[manager].append(player)

    root = -1
    for player in range(len(scores)):
        if in_degree[player] == 0:
            root = player
            break

    ans = 0
    dfs(root)
    return ans