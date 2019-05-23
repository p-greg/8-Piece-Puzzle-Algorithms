from abc import ABCMeta, abstractmethod

#this is a generic state class that holds the values of each
#position in the environment class State:
class State:
    parent=None
    children=[]
    cost=0
    ID=0

    state = [[0,0,0],[0,0,0],[0,0,0]]

    def __init__(self,state,parent=None,children=None):
        self.state = state
        self.parent = parent
        if children:
            self.children = children

    #set the cost to get to this state
    def setCost(self, cost):
        self.cost=cost

    def setID(self, ID):
        self.ID=ID

    #                                   0 1 2 
    #                                   3 4 5
    # printState prints in this format: 6 7 8 
    def printState(self):
        print(str(self.state[0][0])+" "+str(self.state[0][1])+" "+str(self.state[0][2]))
        print(str(self.state[1][0])+" "+str(self.state[1][1])+" "+str(self.state[1][2]))
        print(str(self.state[2][0])+" "+str(self.state[2][1])+" "+str(self.state[2][2]))

    # printSmall will print in this format: ( 0 1 2 3 4 5 6 7 8 9 )
    def printSmall(self):
        print("("+str(self.state[0][0])+" "+str(self.state[0][1])+" "+str(self.state[0][2])+" "+str(self.state[1][0])+" "+str(self.state[1][1])+" "+str(self.state[1][2])+" "+str(self.state[2][0])+" "+str(self.state[2][1])+" "+str(self.state[2][2])+")")

    def stateString(self):
        return "("+str(self.state[0][0])+" "+str(self.state[0][1])+" "+str(self.state[0][2])+" "+str(self.state[1][0])+" "+str(self.state[1][1])+" "+str(self.state[1][2])+" "+str(self.state[2][0])+" "+str(self.state[2][1])+" "+str(self.state[2][2])+")"


    #nextNodes returns a tuple of all the possible 
    #next nodes in multidimensional arrays
    #total possible nodes vary from 2-4
    #Ex. ([[8,1,2],[3,4,5],[6,7,0]]) returns (([[8,1,2],[3,4,0],[6,7,5]]),([[8,1,2],[3,4,5],[6,0,7]]))
    def nextNodes(self):
        if self.state[0][0]==0:
            return ([[self.state[0][1],self.state[0][0],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[1][0],self.state[0][1],self.state[0][2]],[self.state[0][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]])
        if self.state[0][1]==0:
            return ([[self.state[0][1],self.state[0][0],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][2],self.state[0][1]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[1][1],self.state[0][2]],[self.state[1][0],self.state[0][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]])
        if self.state[0][2]==0:
            return ([[self.state[0][0],self.state[0][2],self.state[0][1]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[1][2]],[self.state[1][0],self.state[1][1],self.state[0][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]])
        if self.state[1][0]==0:
            return ([[self.state[1][0],self.state[0][1],self.state[0][2]],[self.state[0][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][1],self.state[1][0],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[2][0],self.state[1][1],self.state[1][2]],[self.state[1][0],self.state[2][1],self.state[2][2]]])
        if self.state[1][1]==0:
            return ([[self.state[0][0],self.state[1][1],self.state[0][2]],[self.state[1][0],self.state[0][1],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][1],self.state[1][0],self.state[1][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][2],self.state[1][1]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[2][1],self.state[1][2]],[self.state[2][0],self.state[1][1],self.state[2][2]]])
        if self.state[1][2]==0:
            return ([[self.state[0][0],self.state[0][1],self.state[1][2]],[self.state[1][0],self.state[1][1],self.state[0][2]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][2],self.state[1][1]],[self.state[2][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[2][2]],[self.state[2][0],self.state[2][1],self.state[1][2]]])
        if self.state[2][0]==0:
            return ([[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[2][0],self.state[1][1],self.state[1][2]],[self.state[1][0],self.state[2][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][1],self.state[2][0],self.state[2][2]]])
        if self.state[2][1]==0:
            return ([[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][1],self.state[2][0],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[2][1],self.state[1][2]],[self.state[2][0],self.state[1][1],self.state[2][2]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][2],self.state[2][1]]])
        if self.state[2][2]==0:
            return ([[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[1][2]],[self.state[2][0],self.state[2][2],self.state[2][1]]],
                    [[self.state[0][0],self.state[0][1],self.state[0][2]],[self.state[1][0],self.state[1][1],self.state[2][2]],[self.state[2][0],self.state[2][1],self.state[1][2]]])

    #equality to check when current state equals the goal state
    def __eq__(self,other):
        return self.state == other.state

    #check a state is solvable 
    def solvable(self):
        total=0
        for i in range(8):
            step = i+1
            row = i//3
            col = i%3
            value = int(self.state[row][col])
            for j in range(i+1,9):
                row2 = j//3
                col2 = j%3
                value2 = self.state[row2][col2]
                if not value2==0 and value2<value:
                    total+=1
        if total%2==0:
            return True
        else:
            return False

    def addChild(self,child):
        self.children.append(child)

    #abstract the hash method which will
    #be used as the heuristic + cost var
    @abstractmethod
    def __hash__(self):
        pass

class heuristicOne(State):
    def __hash__(self):
        n = 0
        if not self.state[0][0]==0:
            n +=1
        if not self.state[0][1]==1:
            n+=1
        if not self.state[0][2]==2:
            n+=1
        if not self.state[1][0]==3:
            n+=1
        if not self.state[1][1]==4:
            n+=1
        if not self.state[1][2]==5:
            n+=1
        if not self.state[2][0]==6:
            n+=1
        if not self.state[2][1]==7:
            n+=1
        if not self.state[2][2]==8:
            n+=1
        return n
    def __gt__(self,other):
        if self.__hash__() > other.__hash__():
            return True
        elif self.__hash__() < other.__hash__():
            return False
        else:
            if self.ID>other.ID:
                return True
            else:
                return False

class heuristicTwo(State):
    def __hash__(self):
        manHat = 0
        for i in range(3):
            for j in range(3):
                x=(self.state[i][j]//3)+1
                y=(self.state[i][j]+1)%3
                if y==0:
                    y=3
                manHat+=abs((i+1)-x)+abs((j+1)-y)
        return manHat
    def __gt__(self,other):
        if self.__hash__()>other.__hash__():
            return True
        elif self.__hash__()<other.__hash__():
            return False
        else:
            if self.ID>other.ID:
                return True
            else:
                return False

class heuristicThree(State):
    def __hash__(self):
        n = 0
        if not self.state[0][0]==0:
            n+=1
        if not self.state[0][1]==1:
            n+=1
        if not self.state[0][2]==2:
            n+=1
        if not self.state[1][0]==3:
            n+=1
        if not self.state[1][1]==4:
            n+=1
        if not self.state[1][2]==5:
            n+=1
        if not self.state[2][0]==6:
            n+=1
        if not self.state[2][1]==7:
            n+=1
        if not self.state[2][2]==8:
            n+=1
        manHat = 0
        for i in range(3):
            for j in range(3):
                x=(self.state[i][j]//3)+1
                y=(self.state[i][j]+1)%3
                if y==0:
                    y=3
                manHat+=abs((i+1)-x)+abs((j+1)-y)
        r = (manHat+n)/2
        return r
    def __gt__(self,other):
        if self.__hash__()>other.__hash__():
            return True
        elif self.__hash__()<other.__hash__():
            return False
        else:
            if self.ID>other.ID:
               return True
            else:
               return False

