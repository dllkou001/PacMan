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
    return [s, s, w, s, w, w, s, w]

def traverse(fringe, problem):
    def find_path(v):
        path = []
        for item in v:
            path.append(item[1])
        return path
    fringe.push([(problem.getStartState(), None, 0)])
    visited = set()
    while not fringe.isEmpty():
        v = fringe.pop()
        if problem.isGoalState(v[-1][0]):
            return find_path(v[1:])
        if v[-1][0] not in visited:
            visited.add(v[-1][0])
            suc = problem.getSuccessors(v[-1][0])
            for child in suc:
                fringe.push(v + [(child[0], child[1], child[2] + v[-1][2])])

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("start:", problem.getstartstate())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))"""

    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))"""


    """successors = problem.getSuccessors(problem.getStartState())
    visitedPositions = []
    stack = util.Stack()
    for s in successors:
        dfsUtil(problem, s, visitedPositions, stack)
        if(stack.isEmpty() == False):
            stack.pop()

    nodes = []
    if(not stack.isEmpty()):
        nodes = stack.list

    directions = []
    for action in nodes:
        directions.append(action[1])

    return directions
    util.raiseNotDefined()"""
    """fringe = util.Stack()
    return traverse(fringe, problem)"""
    fringe = util.Stack();
    def find_path(v):
        """print("Stack: ", v)"""
        list = v.list[-1]
        path = []
        for item in list:
            """print("Item added:", item[1])"""
            if(item[1] != None):
                path.append(item[1])
        return path
    fringe.push((problem.getStartState(), None, 0))
    visited = set()
    correctNodes = util.Stack();
    correctNodes.push([(problem.getStartState(), None, 0)])
    while not fringe.isEmpty():
        v = fringe.pop()
        """print("Node: ", v)"""
        travelledNode = correctNodes.pop()
        """print("Travelled node: ",travelledNode)"""
        if problem.isGoalState(v[0]):
            """print("Navigation: ", correctNodes.list[-1])"""
            correctNodes.push(travelledNode)
            return find_path(correctNodes)
        if v[0] not in visited:
            visited.add(v[0])
            """print("Visited node: ", v[0])"""
            suc = problem.getSuccessors(v[0])
            """print("Successors: ", suc)"""
            for child in suc:
                """print("Child: ", child)"""
                fringe.push(child)
                list = []
                list.append(child)
                navigation = travelledNode + list
                correctNodes.push(navigation)


def dfsUtil(problem, node, visitedList, stack):
    if (problem.isGoalState(node[0]) == True):
        return stack;
    if(not visitedList.__contains__(node[0])):
        visitedList.append(node[0])
        stack.push(node)
        """if(problem.isGoalState(node[0]) == True):
            return stack;"""
        successors = problem.getSuccessors(node[0])
        if len(successors) == 0:
            if not stack.isEmpty():
                stack.pop()
                return stack
        else:
            for s in successors:
                dfsUtil(problem, s, visitedList, stack)
                if not stack.isEmpty():
                    stack.pop()
    return stack


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


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
