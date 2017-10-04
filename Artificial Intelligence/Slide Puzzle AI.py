"""
Programming Assignment 1
CSCI 487
Snehasis Mukhopadyay
written by Nathan Rollins
"""

from random import randint

# 3, 2, "B"
# 1, 7, 8
# 6, 5, 4

#define globals for manipulating boxes
GOALSTATE = [1, 2, 3, 4, 5, 6, 7, 8, "B"]
boxes = [3, 2, "B", 1, 7, 8, 6, 5, 4]
ROWSIZE = 3
Q = []
closed = []
state1 = []
state2 = []
state3 = []



class Tree(object):
    def __init__(self):
        self.name = None
        self.children = []
        self.state = None #This will be randomly seeded later for the root node
        self.moves = None
        self.parent = None
        self.depth = 0
        self.stateDist = 0

    def findDist(self, node):
        stateDist = 0
        #take the node and generate a value based on how far away it is from the goal state
        #Yes, I know this is horrible implementation but it was 4:37 am when I wrote this so I didn't care
        #The values of distance are calculated from how far away the object is from its desired state
        if node.state[0] == 1:
            stateDist = stateDist
        elif node.state[0] == 2:
            stateDist = stateDist + 1
        elif node.state[0] == 3:
            stateDist = stateDist + 2
        elif node.state[0] == 4:
            stateDist = stateDist + 3
        elif node.state[0] == 5:
           stateDist = stateDist + 4
        elif node.state[0] == 6:
           stateDist = stateDist + 5
        elif node.state[0] == 7:
           stateDist = stateDist + 6
        elif node.state[0] == 8:
           stateDist = stateDist + 7
        elif node.state[0] == "B":
           stateDist = stateDist + 8

        if node.state[1] == 1:
            stateDist = stateDist + 1
        elif node.state[1] == 2:
            stateDist = stateDist
        elif node.state[1] == 3:
            stateDist = stateDist + 1
        elif node.state[1] == 4:
            stateDist = stateDist + 2
        elif node.state[1] == 5:
           stateDist = stateDist + 3
        elif node.state[1] == 6:
           stateDist = stateDist + 4
        elif node.state[1] == 7:
           stateDist = stateDist + 5
        elif node.state[1] == 8:
           stateDist = stateDist + 6
        elif node.state[1] == "B":
           stateDist = stateDist + 7
         
        if node.state[2] == 1:
            stateDist = stateDist + 2
        elif node.state[2] == 2:
            stateDist = stateDist + 1
        elif node.state[2] == 3:
            stateDist = stateDist
        elif node.state[2] == 4:
            stateDist = stateDist + 1
        elif node.state[2] == 5:
           stateDist = stateDist + 2
        elif node.state[2] == 6:
           stateDist = stateDist + 3
        elif node.state[2] == 7:
           stateDist = stateDist + 4
        elif node.state[2] == 8:
           stateDist = stateDist + 5
        elif node.state[2] == "B":
           stateDist = stateDist + 6

        if node.state[3] == 1:
            stateDist = stateDist + 3
        elif node.state[3] == 2:
            stateDist = stateDist + 2
        elif node.state[3] == 3:
            stateDist = stateDist + 1
        elif node.state[3] == 4:
            stateDist = stateDist
        elif node.state[3] == 5:
           stateDist = stateDist + 1
        elif node.state[3] == 6:
           stateDist = stateDist + 2
        elif node.state[3] == 7:
           stateDist = stateDist + 3
        elif node.state[3] == 8:
           stateDist = stateDist + 4
        elif node.state[3] == "B":
           stateDist = stateDist + 5

        if node.state[4] == 1:
            stateDist = stateDist + 4
        elif node.state[4] == 2:
            stateDist = stateDist + 3
        elif node.state[4] == 3:
            stateDist = stateDist + 2
        elif node.state[4] == 4:
            stateDist = stateDist + 1
        elif node.state[4] == 5:
           stateDist = stateDist
        elif node.state[4] == 6:
           stateDist = stateDist + 1
        elif node.state[4] == 7:
           stateDist = stateDist + 2
        elif node.state[4] == 8:
           stateDist = stateDist + 3
        elif node.state[4] == "B":
           stateDist = stateDist + 4

        if node.state[5] == 1:
            stateDist = stateDist + 5
        elif node.state[5] == 2:
            stateDist = stateDist + 4
        elif node.state[5] == 3:
            stateDist = stateDist + 3
        elif node.state[5] == 4:
            stateDist = stateDist + 2
        elif node.state[5] == 5:
           stateDist = stateDist + 1
        elif node.state[5] == 6:
           stateDist = stateDist
        elif node.state[5] == 7:
           stateDist = stateDist + 1
        elif node.state[5] == 8:
           stateDist = stateDist + 2
        elif node.state[5] == "B":
           stateDist = stateDist + 3

        if node.state[6] == 1:
            stateDist = stateDist + 6
        elif node.state[6] == 2:
            stateDist = stateDist + 5
        elif node.state[6] == 3:
            stateDist = stateDist + 4
        elif node.state[6] == 4:
            stateDist = stateDist + 3
        elif node.state[6] == 5:
           stateDist = stateDist + 2
        elif node.state[6] == 6:
           stateDist = stateDist + 1
        elif node.state[6] == 7:
           stateDist = stateDist
        elif node.state[6] == 8:
           stateDist = stateDist + 1
        elif node.state[6] == "B":
           stateDist = stateDist + 2

        if node.state[7] == 1:
            stateDist = stateDist + 7
        elif node.state[7] == 2:
            stateDist = stateDist + 6
        elif node.state[7] == 3:
            stateDist = stateDist + 5
        elif node.state[7] == 4:
            stateDist = stateDist + 4
        elif node.state[7] == 5:
           stateDist = stateDist + 3
        elif node.state[7] == 6:
           stateDist = stateDist + 2
        elif node.state[7] == 7:
           stateDist = stateDist + 1
        elif node.state[7] == 8:
           stateDist = stateDist
        elif node.state[7] == "B":
           stateDist = stateDist + 1

        if node.state[8] == 1:
            stateDist = stateDist + 8
        elif node.state[8] == 2:
            stateDist = stateDist + 7
        elif node.state[8] == 3:
            stateDist = stateDist + 6
        elif node.state[8] == 4:
            stateDist = stateDist + 5
        elif node.state[8] == 5:
           stateDist = stateDist + 4
        elif node.state[8] == 6:
           stateDist = stateDist + 3
        elif node.state[8] == 7:
           stateDist = stateDist + 2
        elif node.state[8] == 8:
           stateDist = stateDist + 1
        elif node.state[8] == "B":
           stateDist = stateDist

        # add it to the depth
        node.stateDist = node.depth + stateDist


    def generateRandomStates(self):
        possible = [1, 2, 3, 4, 5, 6, 7, 8, "B"]
        self.state = possible
        #generate states by taking a seed state, called possible, and randomly swap its components, storing the result in this node's state property
        for i in range(0, 10):
            j = randint(0, 8)
            possible = self.swap(0, j)
        self.state = possible

        
        
            
    def swap(self, blankSpot, swappingSpot):
        tempBoxes = self.state[:] # copies the current node's state
        tempBoxes[blankSpot], tempBoxes[swappingSpot] = tempBoxes[swappingSpot], tempBoxes[blankSpot] #swaps the two items with each other
        return tempBoxes #returns a new, swapped state array

    
    #this just generates possible child states based on the current state
    def findMoves(self,pName, current):
        #find the Blank in current
        i = current.index("B")
        #check if swap is possible, i.e, not out of bounds, then swap and save it
        if (i - ROWSIZE) >= 0:
            stateUP = self.swap( i, i-ROWSIZE)
        else:
            stateUP = None

        if (i + ROWSIZE) <= 8: 
            stateDOWN = self.swap(i, i+ROWSIZE)
        else:
            stateDOWN = None

        if (i % ROWSIZE != 0):
            stateLEFT = self.swap(i, i-1)
        else:
            stateLEFT = None

        if (i % ROWSIZE != (ROWSIZE-1)):
            stateRIGHT = self.swap( i, i+1)
        else:
            stateRIGHT = None
        #add the states to an array for keeping
        if stateUP != None:
            stateUP.append(pName)
            stateUP.append("up")
        if stateDOWN != None:
            stateDOWN.append(pName)
            stateDOWN.append("down")
        if stateLEFT != None:
            stateLEFT.append(pName)
            stateLEFT.append("left")
        if stateRIGHT != None:
            stateRIGHT.append(pName)
            stateRIGHT.append("right")
        
        States = [stateUP, stateDOWN, stateLEFT, stateRIGHT] 

        return States # return array of all new possible states to be used to create children
                
    def printTreePath(self, node):
        #function that prints all nodes in this tree, starting at the end node and working its way through its parents.
        path = []
        path.append(node)
        keepGoing = True
        while keepGoing:
            if node.parent == None:
                keepGoing = False
                return path
            else:
                node = node.parent
                path.append(node)
                
                
                

    def makeChildren(self):
        self.moves = self.findMoves(self.name, self.state) #root.moves is now filled with new possible states
        for move in self.moves: # now we create the children based off these moves
            if move != None:
                a = Tree()
                a.name = move[10] #give them each an appropiate name
                a.state = move[:9] #assign them their state
                a.parent = self #keep track of their parent node
                self.children.append(a) #store them in the .children array


    def BFS(self, rootNode):
        Q.append(rootNode) # start by placing the head into the Q (see what I did there?)
        Q[0].depth = 0
        keepGoing = True
        
        while keepGoing:
            Q[0].makeChildren()
            if Q[0].state == GOALSTATE: #if the head node is a goal state, then we done
                keepGoing = False
                print("YAY")
                print (Q[0].printTreePath(Q[0]))
            if Q[0].depth > 10:
                keepGoing = False
            for child in Q[0].children: # Otherwise we continue
                if child not in Q:
                    if child not in closed: #these make sure the node hasnt been used before.
                        Q.append(child)
                        child.depth = Q[0].depth + 1 #keep track of depth
            closed.append(Q[0])
            del Q[0]  #advance the queue
            

            

    def Astar(self, rootNode):
        Q.append(rootNode)
        Q[0].depth = 0
        keepGoing = True
        #gotta keep track of each node's h(n)
        
        while keepGoing:
            Q[0].makeChildren()
            distances = []
            if Q[0].state == GOALSTATE: #if the head node is a goal state, then we done
                keepGoing = False
                print("YAY")
                print (Q[0].printTreePath(Q[0]))
            if Q[0].depth > 10:
                keepGoing = False

            for child in Q[0].children: # Otherwise we continue
                child.findDist(child) #here we find a child's distance, and track them
                distances.append(child.stateDist)
                child.depth = Q[0].depth + 1

            #we now compare the distances and find which node is the best to take
            minimum = min(distances)
            target = distances.index(minimum)
            print(distances)
            Q.append(Q[0].children[target])
            closed.append(Q[0])
            del Q[0]  #advance the queue
               
              
                
      



def main():

    root1 = Tree()
    root1.generateRandomStates()
    root1.name = "root1"
    root1.BFS(root1)
    root1.Astar(root1)

    root2 = Tree()
    root2.generateRandomStates()
    root2.name = "root2"
    root2.BFS(root2)
    root2.Astar(root2)

    root3 = Tree()
    root3.generateRandomStates()
    root3.name = "root3"
    root3.BFS(root3)
    root3.Astar(root3)
    
   
 




if __name__ == "__main__":
  main()

