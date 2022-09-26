from collections import defaultdict    

def bfs(graph, visited, start, output):
    q = []
    visited[start] = 1
    q.append(start)
    while len(q) != 0:
        print("Elements in Queue: ", q)
        ele = q.pop(0)
        print("Popped Element: ",ele)
        output.append(ele)
        for i in graph[ele]:
            if(visited[i] != 1):
                visited[i] = 1
                q.append(i)
       

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
bfs(graph1, visited, src, output)

print("Output of BFS Traversal: ")
for i in output:
    print(i, end = " ")