Objective

To understand and implement informed search algorithms and state-space representation through:

A* (A-star) Search Algorithm – to find the optimal path using cost and heuristics.

Water Jug Problem – to find a sequence of operations to get the desired amount of water using search strategies.

🧠 1. A* Algorithm
Aim:

To solve the 8 Puzzle Problem using the A* (A-star) search algorithm with heuristic functions.

Theory:

A* is an informed search algorithm that combines both the actual cost and estimated cost to reach the goal.
It uses a function:

f(n) = g(n) + h(n)


Where:

g(n) = cost to reach the current node.

h(n) = estimated cost to reach the goal (heuristic).

f(n) = total estimated cost of the path through node n.

A* guarantees the optimal solution if the heuristic used is admissible (never overestimates the cost).

Common Heuristics for 8 Puzzle:

Misplaced Tiles Heuristic – counts tiles not in place.

Manhattan Distance Heuristic – sums distance of tiles from their goal positions.

🧮 Steps:

Start with the initial state.

Compute f(n) = g(n) + h(n) for all possible moves.

Select the state with the minimum f(n).

Continue until the goal state is reached.

Track the path from the start to the goal.

🧩 Example

Initial State:

1 2 3
4 0 6
7 5 8


Goal State:

1 2 3
4 5 6
7 8 0


Water Jug Problem
Aim:

To measure a specific amount of water using two jugs of different capacities.

Theory:

The Water Jug Problem is a constraint satisfaction problem that can be solved using state-space search.
Each state represents the amount of water in both jugs.
Operators represent actions such as:

Fill a jug completely.

Empty a jug completely.

Pour water from one jug to another until one is full or empty.

Example Problem:

Given:

Jug A = 4 liters

Jug B = 3 liters

Goal = 2 liters in Jug A

Possible Operations:

Fill Jug A

Fill Jug B

Empty Jug A

Empty Jug B

Pour A → B

Pour B → A

🧩 State Representation:

Each state can be represented as a pair (x, y)
where
x = water in Jug A
y = water in Jug B

🧠 Algorithm Steps:

Start from the initial state (0, 0).

Apply all valid operations.

Avoid repeating previously visited states.

Stop when the goal (2, y) is reached.
