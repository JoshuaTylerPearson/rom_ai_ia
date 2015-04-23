#	rom_ai_ia version 1.1 
#	by Joshua Pearson
#	last change 2015-04-25

graph = {'A': set(['140S', '75Z', '118T']),
         'Z': set(['75A', '71O']),
         'O': set(['71Z', '151S']),
         'T': set(['118A', '111L']),
         'L': set(['111T', '70M']),
         'M': set(['70L', '75D']),
         'D': set(['75M', '120C']),
         'S': set(['99F', '80R', '140A']),
         'R': set(['80S', '97P', '146C']),
         'C': set(['146R', '138P', '120D']),
         'P': set(['97R', '138C', '101B']),
         'F': set(['99S', '211B']),
         'G': set(['90B']),
         'B': set(['211F', '101P', '90G', '85U']),
         'U': set(['85B', '98H', '142V']),
         'H': set(['98U', '86E']),
         'E': set(['86H']),
         'V': set(['142U', '92I']),
         'I': set(['92V', '87N']),
         'N': set(['87I'])}

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next[-1:] == goal:
                yield path + [next[-1:]]
            else:
                queue.append((next[-1:], path + [next[-1:]]))
                
def shortest_path_bfs(graph, start, goal):
    try:
        return next(bfs_path(graph, start, goal))
    except StopIteration:
        return None

def uniform_cost(graph, start, goal):
    frontier = [(0, [start])]
    while frontier:
        cost, path = frontier.pop()
        if path[-1] == goal:
            return str(path) + ": " + str(cost)
        for n_path in graph[path[-1]] - set(path):
            frontier.append((int(n_path[:-1]) + int(cost) , path + [n_path[-1:]]))
        frontier.sort(reverse=True)

srt = input('Starting city: ')
srt = srt.upper()[:1]
if not srt or srt.isdigit():
    while not srt or srt.isdigit():
        srt = input('Starting city: ')
        srt = srt.upper()[:1]

end = input('Ending city: ')
end = end.upper()[:1]
if not end or end.isdigit():
    while not end or end.isdigit():
        end = ('Ending city: ')
        end = end.upper()[:1]

slct = input('0: breadth first\n1: uniform cost\n')
if not slct or not slct.isdigit():
    while not slct or not slct.isdigit():
        slct = input('0: breadth first\n1: uniform cost\n')
        
slct = int(slct)
if slct == 0:
	print("shortest path: " + str(shortest_path_bfs(graph, srt, end)))
elif slct == 1:
	print("shortest path: " + str(uniform_cost(graph, srt, end)))
else:
	print("not currently supported")
input()
