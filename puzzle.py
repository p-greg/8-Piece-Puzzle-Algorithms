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
#needs more validation
if len(sys.argv)==11:
    #user inputted state
    start = sc.heuristicOne([[int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])],[int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7])],[int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10])]])
else:
    #random start state 
    start = sc.heuristicOne([[7,2,3],[8,4,5],[0,1,6]])

#-- create the states
current = sc.heuristicOne([[0,0,0],[0,0,0],[0,0,0]])
child = sc.heuristicOne([[0,0,0],[0,0,0],[0,0,0]])
goalState = sc.heuristicOne([[0,1,2],[3,4,5],[6,7,8]])
fake = sc.heuristicOne([[0,1,2],[3,4,5],[6,7,8]])
start.setCost(0)
start.setID(1)

#prove equality will work between classes
#print(goalState==fake)

pQueue = [] #create the priority queue

mode=int(sys.argv[1])
if mode%2==1:
    print("A* Search")
    h.heappush(pQueue, (start.__hash__()+start.cost, start))
else:
    print("Best First Search")
    h.heappush(pQueue, (start.__hash__(), start))
print() #for formatting

#depending on the mode setting, use one of the 3 heuristic functions
#and add the cost for A* search

print("Start state: ")
start.printState()
print()

expandedNodes = 1
idCount = 1
stopped=False

while not current==goalState:
    pop = h.heappop(pQueue)
    current = pop[1]
    nextNodes = current.nextNodes()

    #every 5000 nodes expanded print a update on the screen 
    if (expandedNodes%5000==0):
        print("Expanded Nodes: "+str(expandedNodes))
    #every 10000 nodes expanded ask the user if they want to continue
    if (expandedNodes%10000==0):
        print("I have looked at "+str(expandedNodes)+" states and have not found a solution")
        print("I am going to start slowing down soon..")
        print("Would you like to keep going? [y/n]")
        userInput=input()
        print()
        if userInput=='n':
            stopped=True
            break
#        following used for testing purposes    
#        print("Cost "+str(current.cost))
#        print("Hash "+str(current.__hash__()))
#        print("ID "+str(current.ID))
#        current.printState()
#        for x in range(10):
#            pop = h.heappop(pQueue)
#            print("Cost "+str(pop[1].cost))
#            print("Hash "+str(pop[1].__hash__()))
#            print("ID "+str(pop[1].ID))
#            pop[1].printState()
#            print()
#        break

    for j in range(len(nextNodes)):
        i = j-1
        if mode//2==0: #mode one or two 
            child = sc.heuristicOne(nextNodes[i])
        elif mode//2==1: #mode two or three
            child = sc.heuristicTwo(nextNodes[i])
        else: #mode four or five
            child = sc.heuristicThree(nextNodes[i])
        #need to check if any parent is
        #the child state to prevent loops
        tempNode = copy.copy(current)
        addChildBool=True
        while tempNode.parent:
            tempNode=tempNode.parent
            if tempNode==child:
                addChildBool=False
        if addChildBool:
            idCount+=1
            current.addChild(child)
            child.parent=current
            child.setCost(current.cost+1)
            child.setID(idCount)
            if mode%2==1: #modes 1, 3 and 5 are for A*
                h.heappush(pQueue, (child.__hash__()+child.cost, child))
            else:
                h.heappush(pQueue, (child.__hash__(), child))
    expandedNodes+=1
    gc.collect()
#if the user stopped the program exit before printing the path
if stopped:
    print()
    print("I could not find a path.. sorry :(")
    sys.exit()

finalPath = current.stateString()
current.printState()
print("^^^^^ Final State ^^^^^")
moves=0
printPath(current.parent)
print("Total States Created: "+str(idCount))
print("Total States Checked: "+str(expandedNodes))
print("Moves: "+str(moves))

print()
print(finalPath)
