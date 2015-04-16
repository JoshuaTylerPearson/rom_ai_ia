graph = {'A': set(['S140', 'Z75', 'T118']),
         'Z': set(['A75', 'O71']),
         'O': set(['Z71', 'S151']),
         'T': set(['A118', 'L111']),
         'L': set(['T111', 'M70']),
         'M': set(['L70', 'D75']),
         'D': set(['M75', 'C120']),
         'S': set(['F99', 'R80', 'A140']),
         'R': set(['S80', 'P97', 'C146']),
         'C': set(['R146', 'P138', 'D120']),
         'P': set(['R97', 'C138', 'B101']),
         'F': set(['S99', 'B211']),
         'G': set(['B90']),
         'B': set(['F211', 'P101', 'G90', 'U85']),
         'U': set(['B85', 'H98', 'V142']),
         'H': set(['U98', 'E86']),
         'E': set(['H86']),
         'V': set(['U142', 'I92']),
         'I': set(['V92', 'N87']),
         'N': set(['I87'])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next[:1] == goal:
                yield path + [next[:1]]
            else:
                queue.append((next[:1], path + [next[:1]]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

#def a_star(graph, start, goal):
    

srt = input('Starting city: ')

srt = srt.upper()[:1]
if not srt:
    while not srt:
        srt = input('Starting city: ')
        srt = srt.upper()[:1]

end = input('Ending city: ')

end = end.upper()[:1]
if not end:
    while not end:
        end = input('Ending city: ')
        end = end.upper()[:1]

slct = input('0: breadth first\n1: uniform cost\n')
if not slct or not slct.isdigit():
    while not slct or not slct.isdigit():
        slct = input('0: breadth first\n1: uniform cost\n')

slct = int(slct)

if slct == 0:
	print("shortest path: " + str(shortest_path(graph, srt, end)))
elif slct == 1:
	print("not currently supported")
else:
	print("not currently supported")
