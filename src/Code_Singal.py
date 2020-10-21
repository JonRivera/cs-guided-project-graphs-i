# You are given a directed acyclic graph (DAG) that contains N nodes.
#
# Write a function that can find all the possible paths from node 0 to node N - 1. You can
# return the path in any order.
#
# graph[a] is a list of all nodes b for which the edge a -> b exists. (
# graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).


#
# Input: graph = [[1, 2],[3],[3],[4],[]] (N-1 Node here represents the index of the fifth node or Node 4)
# Output: [[0,1,3,4], [0,2,3,4]]

from collections import deque


# Keep in mind that each node can be represented as an index, ex)The first node is index 0
# and the last node(4th one) is index 3
# Run a for loop that goes traverses the graph and tracks when we find the target
# The for loop is going to be searching over all the nodes and is going to be
# Store temp all the nodes the create a path towards node n-1 into a deque (FIFO)
# Store all path that end up in node n -1 into a results list
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    results = []

    def backtrack(currNode, path):
        # if we reach the target, no need to explore further.
        if currNode == target:
            results.append(list(path))
            return
        # explore the neighbor nodes one after another.
        for nextNode in graph[currNode]:
            path.append(nextNode)
            # go back to 0 node when we perform path.pop by recursion ,pop .. .pop (backwards recursion)
            backtrack(nextNode, path)  #foward recursion
            path.pop() # recursively were removing the nodes that were checked if they were targets (bacward recursion)

    # kick of the backtracking, starting from the source node (0).
    path = deque([0])
    backtrack(0, path)

    return results


