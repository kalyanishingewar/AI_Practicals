

from collections import defaultdict

# DFS algorithm
def dfs(graph, start, visited, output):
    if (visited[start]):
        return
    output.append(start);
    print("Current Node of DFS traversal(OUTPUT): " , start)
    visited[start] = 1
    
    for i in graph[start]:
        print("Parent is: " ,start , " Child is: " , i)
        if(visited[i] != 1):
            dfs(graph, i, visited, output)
    
    
graph1 = defaultdict(list)
v = int(input("Enter Total No. of vertices in graph: "))
e = int(input("Enter Total No. of edges in graph: "))

for i in range(e):
    x = int(input(f"Enter Starting vertex of edge {i+1}: "))
    y = int(input(f"Enter Ending vertex of edge {i+1}: "))
    
    graph1[x].append(y);
    graph1[y].append(x);
    
src = int(input("Enter source vertex: "))
visited = []
for i in range(v+1):
    visited.append(0)
output = []
dfs(graph1, src, visited, output)

print("Output of DFS Traversal: ")
for i in output:
    print(i, end = " ")