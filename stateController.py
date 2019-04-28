from abc import ABCMeta, abstractmethod

#this is a generic state class that holds the values of each
#position in the environment
class State:
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    x8=0
    x9=0
    parent=None
    children=[]
    cost=0

    def __init__(self,x1,x2,x3,x4,x5,x6,x7,x8,x9,parent=None,children=None):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.x4=x4
        self.x5=x5
        self.x6=x6
        self.x7=x7
        self.x8=x8
        self.x9=x9
        self.parent = parent
        if children:
            self.children = children

    #set the cost to get to this state
    def setCost(self, cost):
        self.cost=cost

    #                                   0 1 2 
    #                                   3 4 5
    # printState prints in this format: 6 7 8 
    def printState(self):
        print(str(self.x1)+" "+str(self.x2)+" "+str(self.x3))
        print(str(self.x4)+" "+str(self.x5)+" "+str(self.x6))
        print(str(self.x7)+" "+str(self.x8)+" "+str(self.x9))

    # printSmall will print in this format: ( 0 1 2 3 4 5 6 7 8 9 )
    def printSmall(self):
        print("("+str(self.x1)+" "+str(self.x2)+" "+str(self.x3)+" "+str(self.x4)+" "+str(self.x5)+" "+str(self.x6)+" "+str(self.x7)+" "+str(self.x8)+" "+str(self.x9)+")")


    #nextNodes returns a tuple of all the possible next nodes
    #total possible nodes vary from 2-4
    #Ex. (8,1,2,3,4,5,6,7,0) returns ((8,1,2,3,4,0,6,7,5),(8,1,2,3,4,5,6,0,7))
    def nextNodes(self):
        if self.x1==0:
            return ((self.x2,self.x1,self.x3,self.x4,self.x5,self.x6,self.x7,self.x8,self.x9),(self.x4,self.x2,self.x3,self.x1,self.x5,self.x6,self.x7,self.x8,self.x9))
        if self.x2==0:
            return ((self.x2,self.x1,self.x3,self.x4,self.x5,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x3,self.x2,self.x4,self.x5,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x5,self.x3,self.x4,self.x2,self.x6,self.x7,self.x8,self.x9))
        if self.x3==0:
            return ((self.x1,self.x3,self.x2,self.x4,self.x5,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x6,self.x4,self.x5,self.x3,self.x7,self.x8,self.x9))
        if self.x4==0:
            return ((self.x4,self.x2,self.x3,self.x1,self.x5,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x5,self.x4,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x7,self.x5,self.x6,self.x4,self.x8,self.x9))
        if self.x5==0:
            return ((self.x1,self.x5,self.x3,self.x4,self.x2,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x5,self.x4,self.x6,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x6,self.x5,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x8,self.x6,self.x7,self.x5,self.x9))
        if self.x6==0:
            return ((self.x1,self.x2,self.x6,self.x4,self.x5,self.x3,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x6,self.x5,self.x7,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x5,self.x9,self.x7,self.x8,self.x6))
        if self.x7==0:
            return ((self.x1,self.x2,self.x3,self.x7,self.x5,self.x6,self.x4,self.x8,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x8,self.x7,self.x9))
        if self.x8==0:
            return ((self.x1,self.x2,self.x3,self.x4,self.x8,self.x6,self.x7,self.x5,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x8,self.x7,self.x9),(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x7,self.x9,self.x8))
        if self.x9==0:
            return ((self.x1,self.x2,self.x3,self.x4,self.x5,self.x9,self.x7,self.x8,self.x6),(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x7,self.x9,self.x8))

    #equality to check when current state equals the goal state
    def __eq__(self,other):
        if (self.x1==other.x1 and self.x2==other.x2 and self.x3==other.x3 and self.x4==other.x4 and self.x5==other.x5 and self.x6==other.x6 and self.x7==other.x7 and self.x8==other.x8):
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

class bestState1(State):
    def __hash__(self):
        n = 0
        if not self.x1==0:
            n +=1
        if not self.x2==1:
            n+=1
        if not self.x3==2:
            n+=1
        if not self.x4==3:
            n+=1
        if not self.x5==4:
            n+=1
        if not self.x6==5:
            n+=1
        if not self.x7==6:
            n+=1
        if not self.x8==7:
            n+=1
        return n
    def __gt__(self,other):
        if self.__hash__() > other.__hash__():
            return True
        elif self.__hash__() < other.__hash__():
            return False
        else:
            return True

class bestState2(State):
    def __hash__(self):
        n = 0
        if not self.x1==0:
            if self.x1==1:
                n+=1
            if self.x1==2:
                n+=2
            if self.x1==3:
                n+=1
            if self.x1==4:
                n+=2
            if self.x1==5:
                n+=3
            if self.x1==6:
                n+=2
            if self.x1==7:
                n+=3
            if self.x1==8:
                n+=4
        if not self.x2==1:
            if self.x2==2:
                n+=1
            if self.x2==3:
                n+=2
            if self.x2==4:
                n+=1
            if self.x2==5:
                n+=2
            if self.x2==6:
                n+=3
            if self.x2==7:
                n+=2
            if self.x2==8:
                n+=3
        if not self.x3==2:
            if self.x3==1:
                n+=1
            if self.x3==3:
                n+=3
            if self.x3==4:
                n+=2
            if self.x3==5:
                n+=1
            if self.x3==6:
                n+=4
            if self.x3==7:
                n+=3
            if self.x3==8:
                n+=2
        if not self.x4==3:
            if self.x4==1:
                n+=2
            if self.x4==2:
                n+=3
            if self.x4==4:
                n+=1
            if self.x4==5:
                n+=2
            if self.x4==6:
                n+=1
            if self.x4==7:
                n+=2
            if self.x4==8:
                n+=3
        if not self.x5==4:
            if self.x5==1:
                n+=1
            if self.x5==2:
                n+=2
            if self.x5==3:
                n+=1
            if self.x5==5:
                n+=1
            if self.x5==6:
                n+=2
            if self.x5==7:
                n+=1
            if self.x5==8:
                n+=2
        if not self.x6==5:
            if self.x6==1:
                n+=2
            if self.x6==2:
                n+=1
            if self.x6==3:
                n+=2
            if self.x6==4:
                n+=1
            if self.x6==6:
                n+=3
            if self.x6==7:
                n+=2
            if self.x6==8:
                n+=1
        if not self.x7==6:
            if self.x7==1:
                n+=3
            if self.x7==2:
                n+=4
            if self.x7==3:
                n+=1
            if self.x7==4:
                n+=2
            if self.x7==5:
                n+=3
            if self.x7==7:
                n+=1
            if self.x7==8:
                n+=2
        if not self.x8==7:
            if self.x8==1:
                n+=2
            if self.x8==2:
                n+=3
            if self.x8==3:
                n+=2
            if self.x8==4:
                n+=1
            if self.x8==5:
                n+=2
            if self.x8==6:
                n+=1
            if self.x8==8:
                n+=1
        if not self.x9==8:
            if self.x9==1:
                n+=3
            if self.x9==2:
                n+=2
            if self.x9==3:
                n+=3
            if self.x9==4:
                n+=2
            if self.x9==5:
                n+=1
            if self.x9==6:
                n+=2
            if self.x9==7:
                n+=1
        return n
