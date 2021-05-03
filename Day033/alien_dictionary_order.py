from collections import deque, defaultdict as dd

def dfs(source, visited, graph, stack):

    visited.add(source)
    for i in graph[source]:
        if i not in visited:
            dfs(i, visited, graph, stack)

    stack.append(source)

def topological_sort(nodes, graph):

    visited = set()
    stack = deque()
    for i in nodes:
        if i not in visited:
            dfs(i, visited, graph, stack)

    while stack:
        print(stack.pop(), end = " -> ")


def get_order_dict(words):

    graph = dd(list)
    nodes = set()

    for i in range(len(words) - 1):
        ptr1 = 0
        ptr2 = 0
        n1 = len(words[i])
        n2 = len(words[i + 1])
        while ptr1 < n1 and ptr2 < n2 and words[i][ptr1] == words[i+1][ptr2]:
            ptr1 += 1
            ptr2 += 1

        nodes.add(words[i][ptr1])
        nodes.add(words[i+1][ptr2])
        graph[words[i][ptr1]].append(words[i+1][ptr2])

    topological_sort(nodes, graph)


words1 = ["baa", "abcd", "abca", "cab", "cad"]
words2 = ["caa", "aaa", "aab"]
get_order_dict(words1)
print()
get_order_dict(words2)

# b -> d -> a -> c ->
# c -> a -> b ->
