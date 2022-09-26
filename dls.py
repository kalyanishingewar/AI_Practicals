from collections import defaultdict

# DLS algorithm
flag = 0
def dls(graph, start, visited, output, lmt, cnt, goal):
    global flag
    if (visited[start]):
        return
    output.append(start);
    print("Current Node of DFS traversal(OUTPUT): " , start)
    visited[start] = 1
   
    for i in graph[start]:
        print("Parent is: " ,start , " Child is: " , i)
        if(visited[i] != 1 and lmt != cnt):
            dls(graph, i, visited, output, lmt, cnt+1, goal)
        elif (start == goal):
           flag = 1 

   
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
cnt = 0
limit = int(input("Enter Limit: "))
goal = int(input("Enter Goal: "))

dls(graph1, src, visited, output, limit, cnt, goal)

print("Output of DLS Traversal: ")
for i in output:
    print(i, end = " ")
    
if (flag == 1):
    print("")
    print(goal , "Found!!")
else:
    print("")
    print(goal, "Not found!")