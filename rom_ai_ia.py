#	rom_ai_ia version 1.1 
#	by Joshua Pearson
#	last change 2015-04-25

# graph of nodes with {'City name': set(['distance to child node+name of child node']),
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
		 

def bfs_path(graph, start, goal):		#breadth first search takes graph of nodes, stating node, and ending node
    queue = [(start, [start])]		#make queue starting with start node with a path starting at the starting node
    while queue:		#while the queue is not empty
        (vertex, path) = queue.pop(0)		#pop the next node and the path it is in
        for next in graph[vertex] - set(path):		#iterate over the children of the node 
            if next[-1:] == goal:		#if the popped path end in the goal node:
                yield path + [next[-1:]]		#then return the current path ending in the end node
            else:		#otherwise:
                queue.append((next[-1:], path + [next[-1:]]))		#append the child node to the current path and add it to the queue
                
def shortest_path_bfs(graph, start, goal):		#takes the graph of nodes, stating node, and ending node then runs the breadth first search once which yields the path with the fewest nodes
    try:
        return next(bfs_path(graph, start, goal))
    except StopIteration:
        return None

def uniform_cost(graph, start, goal):		#uniform cost search takes graph of nodes, stating node, and ending node
    frontier = [(0, [start])]		#create an array of arrays in the format cost of path, path
    while frontier:		#while the frontier is not empty
        cost, path = frontier.pop()		#pop the frontier separate cost of path and path
        if path[-1] == goal:		#if the popped path end in the goal node:
            return str(path) + ": " + str(cost)		#return the current path append to the total cost
        for n_path in graph[path[-1]] - set(path):		#for all the child nodes of the end of the current path:
            frontier.append((int(n_path[:-1]) + int(cost) , path + [n_path[-1:]]))		#append the frontier with the current cost, and appended the child node to the current path
        frontier.sort(reverse=True)		#sort all paths in frontier by least cost

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
