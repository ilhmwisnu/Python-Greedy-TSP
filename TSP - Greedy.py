# Python Traveling Salesman Problem Program
# Greedy Approach

def TSP(graph,startNode):
    start = startNode - 1
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
    visitedNode = list(map(lambda x : str(x + 1), visitedNode)) # Convert node index to its name
    
    print("Path :", " -> ".join(visitedNode))
    print("Result :", sum)

graph = [
    [0, 10, 15, 20], #1
    [10, 0, 35, 25], #2
    [15, 35, 0, 30], #3
    [20, 25, 30, 0], #4
]

if __name__ == "__main__" :
    TSP(graph,1)    
