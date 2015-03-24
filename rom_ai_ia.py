graph = {'A': set(['S', 'Z', 'T']),
         'Z': set(['A', 'O']),
         'O': set(['Z', 'S']),
         'T': set(['A', 'L']),
         'L': set(['T', 'M']),
         'M': set(['L', 'D']),
         'D': set(['M', 'C']),
         'S': set(['F', 'R', 'A']),
         'R': set(['S', 'P', 'C']),
         'C': set(['R', 'P', 'D']),
         'P': set(['R', 'B']),
         'F': set(['S', 'B']),
         'G': set(['B']),
         'B': set(['F', 'P', 'G', 'U']),
         'U': set(['B', 'H', 'V']),
         'H': set(['U', 'E']),
         'E': set(['H']),
         'V': set(['U', 'I']),
         'I': set(['V', 'N']),
         'N': set(['I'])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

srt = input('Starting city: ')
end = input('Ending city: ')
print("shortest path: " + str(shortest_path(graph, srt.upper()[:1], end.upper()[:1])))