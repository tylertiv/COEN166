# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """        
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    """
    Search node object for your convenience.

    This object uses the state of the node to compare equality and for its hash function,
    so you can use it in things like sets and priority queues if you want those structures
    to use the state for comparison.

    Example usage:
    >>> S = Node("Start", None, None, 0)
    >>> A1 = Node("A", S, "Up", 4)
    >>> B1 = Node("B", S, "Down", 3)
    >>> B2 = Node("B", A1, "Left", 6)
    >>> B1 == B2
    True
    >>> A1 == B2
    False
    >>> node_list1 = [B1, B2]
    >>> B1 in node_list1
    True
    >>> A1 in node_list1
    False
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    bfsQueue = util.Queue()
    visited = []

    startState = problem.getStartState()
    S = Node(startState, None, None, 0)
    currentNode = S

    found = problem.goalTest(currentNode.state)
    while not found:
        actions = problem.getActions(currentNode.state)                         #get list of possible actions from current state

        for action in actions:                                                  #for each action, queue the resulting state as a node
            nextState = problem.getResult(currentNode.state, action)
            nextCost = problem.getCost(currentNode.state, action)
            nextNode = Node(nextState, currentNode, action, nextCost)
            if(not nextNode in visited):                                        #check if already visited this node, only add it if you haven't (graph search)
                bfsQueue.push(nextNode)

        visited.append(currentNode)                                             #add current node to visited list (graph search)
        currentNode = bfsQueue.pop()                                            #get next state from front of queue
        found = problem.goalTest(currentNode.state)                             #checks loop condition -- will break loop if new state is the goal state

    actionList = []
    while currentNode != S:                                                    #traverse back up the tree to find action list
        actionList.insert(0, currentNode.action)
        currentNode = currentNode.parent
    
    return actionList

    
def depthFirstSearch(problem): 

    "*** YOUR CODE HERE ***" 

    dfsStack = util.Stack()
    visited = []

    startState = problem.getStartState()
    S = Node(startState, None, None, 0)
    currentNode = S

    dfsStack.push(currentNode)
    actionList = dfsHelper(problem, visited, dfsStack)
    return actionList

def dfsHelper(problem, visited, stack):
    currentNode = stack.pop()
    visited.insert(0, currentNode.state)

    if problem.goalTest(currentNode.state):                 #found goal state
        actionList = []
        while currentNode.state != problem.getStartState():
            actionList.insert(0, currentNode.action)
            currentNode = currentNode.parent
        return actionList                                   #so, we create a list of actions to get there and return it
    else:
        actions = problem.getActions(currentNode.state)     #find actions at current state
        for action in actions:                              #for each possible action
            nextState = problem.getResult(currentNode.state, action)
            if not nextState in visited:    #if it is not a state that we already visited, add to stack and recusively call this function
                nextCost = problem.getCost(currentNode.state, action)
                nextNode = Node(nextState, currentNode, action, nextCost)
                stack.push(nextNode)        #stack -- LIFO 
                result = dfsHelper(problem, visited, stack) #recursively call this function to search the entire branch before continueing this for loop
                if not(result=="done"):     #if we got "done" returned, we know it was a bad branch that didn't have goal node
                    return result
        return "done"                       #if we made it here, branch must be ended, so we return done for this branch and 


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth. Begin with a depth of 1 and increment depth by 1 at every step.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.goalTest(problem.getStartState()))
    print("Actions from start state:", problem.getActions(problem.getStartState()))

    Then try to print the resulting state for one of those actions
    by calling problem.getResult(problem.getStartState(), one_of_the_actions)
    or the resulting cost for one of these actions
    by calling problem.getCost(problem.getStartState(), one_of_the_actions)

    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def UniformCostSearch(problem):
    """Search the node that has the lowest path cost first."""
    "*** YOUR CODE HERE ***"  
    util.raiseNotDefined()
    

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
