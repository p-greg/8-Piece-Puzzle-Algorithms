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
start = sc.bestState2(7,2,4,5,0,6,8,3,1)
start.setCost(0)
goalState = sc.bestState1(0,1,2,3,4,5,6,7,8)
fake = sc.bestState1(0,1,2,3,4,5,6,7,8)

#s2 = sc.bestState1(1,0,3,5,7,8,6,2,4)

#prove equality will work between classes
#print(goalState==fake) 

print("Start state: ")
start.printState()
print()

pQueue = []
h.heappush(pQueue, (start.__hash__(), start))
current = sc.bestState1(0,0,0,0,0,0,0,0,0)

expandedNodes = 1

while not current==goalState:
    pop = h.heappop(pQueue)
    current = pop[1]
    nextNodes = current.nextNodes()

    #following for testing
#    if (count%100==0):
#        print(current.cost)
#        current.printSmall()
#        for u in range(5):
#           pop = h.heappop(pQueue)
#           print(" "+str(pop[1].cost))
#           print(" "+str(pop[1].__hash__()))
#           printPath(pop[1])
#        break

    for j in range(len(nextNodes)):
        i = j-1
        child = sc.bestState1(nextNodes[i][0],nextNodes[i][1],nextNodes[i][2],nextNodes[i][3],nextNodes[i][4],nextNodes[i][5],nextNodes[i][6],nextNodes[i][7],nextNodes[i][8])
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

printPath(current)
print("Total States expanded: "+str(count))
