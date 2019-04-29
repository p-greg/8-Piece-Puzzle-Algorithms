import stateController as sc
import heapq as h
import copy
import gc
import sys

def printPath(state):
    global finalPath
    global moves
    while state.parent:
        string=state.stateString()
        finalPath=string+" --> "+finalPath
        print()
        state.printState()
        print("^^^^^^ move to ^^^^^^")
        moves+=1
        state=state.parent
    print()
    string = state.stateString()
    finalPath=string+" --> "+finalPath
    moves+=1
    state.printState()

#validate system arguments
if len(sys.argv)==10:
    #user inputted state
    start = sc.heuristicTwo([[int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])],[int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])],[int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9])]])
else:
    #random start state 
    start = sc.heuristicTwo([[7,2,3],[8,4,5],[0,1,6]])

#-- create the states
current = sc.heuristicTwo([[0,0,0],[0,0,0],[0,0,0]])
start.setCost(0)
goalState = sc.heuristicTwo([[0,1,2],[3,4,5],[6,7,8]])
fake = sc.heuristicTwo([[0,1,2],[3,4,5],[6,7,8]])

#prove equality will work between classes
#print(goalState==fake)

print("Start state: ")
start.printState()
print()

pQueue = []
h.heappush(pQueue, (start.__hash__(), start))

expandedNodes = 1

while not current==goalState:
    pop = h.heappop(pQueue)
    current = pop[1]
    nextNodes = current.nextNodes()

#   following for testing
    if (expandedNodes%2==0):
        current.printState()
        while len(pQueue)>0:
            print()
            pop = h.heappop(pQueue)
            print(" "+str(pop[1].cost))
            print(" "+str(pop[1].__hash__()))
            pop[1].printState()
        break

    for j in range(len(nextNodes)):
        i = j-1
        child = sc.heuristicTwo(nextNodes[i])

        #need to check if any parent is
        #the child state to prevent loops
        tempNode = copy.copy(current)
        addChildBool=True
        while tempNode.parent:
            tempNode=tempNode.parent
            if tempNode==child:
                addChildBool=False
        if addChildBool:
            current.addChild(child)
            child.parent=current
            child.setCost(current.cost+1)
            h.heappush(pQueue, (child.__hash__()+child.cost,child))

    expandedNodes+=1
    gc.collect()

finalPath = current.stateString()
current.printState()
print("^^^^^ Final State ^^^^^")
moves=0
printPath(current.parent)
print("Total States expanded: "+str(expandedNodes))
print("Total moves: "+str(moves))

print()
print(finalPath)
