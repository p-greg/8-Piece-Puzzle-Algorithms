import stateController as sc
import heapq as h
import copy
import gc

def printPath(state):
    while state.parent:
        print()
        state.printState()
        print("^^^^^^ move to ^^^^^^")
        state=state.parent
    print()
    state.printState()


#-- create the states
start = sc.heuristicOne([[7,2,4],[5,0,6],[8,3,1]])
#start = sc.heuristicOne([[1,2,3],[6,4,5],[0,7,8]])
start.setCost(0)
goalState = sc.heuristicOne([[0,1,2],[3,4,5],[6,7,8]])
fake = sc.heuristicOne([[0,1,2],[3,4,5],[6,7,8]])

#s2 = sc.bestState1(1,0,3,5,7,8,6,2,4)

#prove equality will work between classes
print(goalState==fake)

print("Start state: ")
start.printState()
print()

pQueue = []
h.heappush(pQueue, (start.__hash__(), start))
current = sc.heuristicOne([[0,0,0],[0,0,0],[0,0,0]])

expandedNodes = 1

while not current==goalState:
    pop = h.heappop(pQueue)
    current = pop[1]
    nextNodes = current.nextNodes()

    #following for testing
#    if (expandedNodes%2==0):
#        current.printState()
#        while len(pQueue)>0:
#            print()
#            pop = h.heappop(pQueue)
#            print(" "+str(pop[1].cost))
#            print(" "+str(pop[1].__hash__()))
#            pop[1].printState()
#        break

    for j in range(len(nextNodes)):
        i = j-1
        child = sc.heuristicOne(nextNodes[i])

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
            h.heappush(pQueue, (child.__hash__(),child))

        #if current.parent:
        #    if not current.parent==child:
        #        current.addChild(child)
        #        child.parent=current
        #        child.setCost(current.cost+1)
        #        h.heappush(pQueue, (child.__hash__(), child))
        #else:
        #    current.addChild(child)
        #    child.parent=current
        #    child.setCost(current.cost+1)
        #    h.heappush(pQueue, (child.__hash__(), child))
    expandedNodes+=1
    gc.collect()

if current==goalState:
    printPath(current)
    print("Total States expanded: "+str(expandedNodes))
