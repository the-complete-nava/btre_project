import heapq

def a_star(graph,heuristic,start,goal):
    open_set, came_from,g_score = [(heuristic[start],start)], {},{start : 0}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [current] + path[::-1]
        for neighbour, cost in graph[current]:
            new_score = g_score[current] + cost
            if neighbour not in g_score or new_score <g_score [neighbour]:
                g_score[neighbour]= new_score
                heapq.heappush(open_set,(new_score + heuristic[neighbour],neighbour))
                came_from[neighbour]=current
    return None

graph = {'S':[('A',1),('G',10)],'A':[('B',2),('C',1)],'B':[('D',5)],'C':[('D',3),('G',4)],'D':[('G',2)],'G':[]}
heuristic={'S':5,'A':3,'B':4,'C':2,'D':6,'G':0}
result=a_star(graph,heuristic,'S','G')
print("optimal path:", '-->'.join(result)if result else "no path found.")
    