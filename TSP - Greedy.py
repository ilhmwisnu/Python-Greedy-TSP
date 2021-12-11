# Python Traveling Salesman Problem Program
# Greedy Approach

def TSP(graph,startNode):
    start = startNode
    visitedNode = []
    visitedNode.append(start)
    sum = 0

    currentNode = graph[start]    

    for i in range(len(graph)-1) :
        min_index = 0
        min = 999999
        for index,value in enumerate(currentNode):
             
            if index not in visitedNode and value < min :
                min = value
                min_index = index
        
        sum += min
        visitedNode.append(min_index)
        currentNode = graph[min_index]

    sum += currentNode[start]
    visitedNode.append(start)

    print("Path :", " -> ".join(map(str,visitedNode)))
    print("Result :", sum)

graph = [
    [0, 10, 15, 20], #A(0)
    [10, 0, 35, 25], #B(1)
    [15, 35, 0, 30], #C(2)
    [20, 25, 30, 0], #D(3)
]

if __name__ == "__main__" :
    TSP(graph,0)    
