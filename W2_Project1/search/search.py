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

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    from game import Directions
    usedList = util.Counter()
    fringe = util.Stack()
    path = util.Stack()
    
    # First checks to see if the initial state is a goal state. If it is, return that state
    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState()
    # If the initial state is not a goal state, begin iterating through the tree
    else:
        fringe.push(problem.getStartState())
        while not fringe.isEmpty():
            currentNode = fringe.peek()
            usedList[currentNode] = 1

            # Selects the next available branch and the direction used to reach that branch
            branch = 0 
            while usedList[problem.getSuccessors(currentNode)[branch][0]] != 0 and branch < (len(problem.getSuccessors(currentNode)) - 1):
                branch += 1
            currentDirection = problem.getSuccessors(currentNode)[branch][1]
            currentNode = problem.getSuccessors(currentNode)[branch][0]

            # Backtracks through the fringe if all branches have already been selected
            if usedList[currentNode] != 0:
                fringe.pop()
                path.pop()
            # If the branch is unused, save the direction and push it onto the fringe.
            # Return the path if this branch is a goal state
            else:
                path.push(currentDirection)
                if problem.isGoalState(currentNode):
                    return path.list 
                usedList[currentNode] = 1
                fringe.push(currentNode)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from game import Directions
    usedList = util.Counter()
    fringe = util.Queue()
    path = util.Stack()
    
    # First checks to see if the initial state is a goal state. If it is, return that state
    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState()
    # If the initial state is not a goal state, begin iterating through the tree
    else:
        fringe.push(problem.getStartState())
        while not fringe.isEmpty():
            currentNode = fringe.peek()
            print currentNode
            usedList[currentNode] = 1

            print "FRINGE", fringe

            while usedList[fringe.peek]
            ### currentDirection = problem.getSuccessors(currentNode)[branch][1]
            currentNode = problem.getSuccessors(currentNode)[branch][0]

            if usedList[currentNode] != 0:
                print "Removing", fringe.peek()
                successors = problem.getSuccessors(fringe.pop())
                for successor in successors:
                    print "Adding", successor
                    usedList[successor] = 1
                    fringe.push(successor)
            # If the branch is unused, save the direction and push it onto the fringe.
            # Return the path if this branch is a goal state
            else:
                ### path.push(currentDirection)
                print "NODE UNUSED", currentNode
                if problem.isGoalState(currentNode):
                    return path.list 
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
