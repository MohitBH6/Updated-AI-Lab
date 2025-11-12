Objective

To understand and implement problem-solving using logic programming in Prolog through:

The Block World Problem, which demonstrates reasoning about world states and actions.

The Monkey-Banana Problem, which models goal-based reasoning using predicates and logical rules.

🧩 1. Block World Problem
🧠 Aim

To simulate the Block World using Prolog, where a robot or agent manipulates blocks stacked on each other or on a table to reach a desired goal state.

🧱 Problem Description

You have a few blocks (e.g., A, B, C) that can be:

On top of another block, or

On the table.

The goal is to transform an initial configuration into a goal configuration using valid actions like:

move(X, Y): move block X onto block Y

move(X, table): move block X onto the table

🧩 Initial State Example
A is on B
B is on table
C is on table

🎯 Goal State
B is on C
A is on B
C is on table


Monkey-Banana Problem
🧠 Aim

To model the Monkey-Banana Problem using Prolog, where the monkey tries to get the banana by reasoning about its actions.

🍌 Problem Description

A monkey is in a room with:

A banana hanging from the ceiling (out of reach).

A box in the room that the monkey can climb.

The monkey can:

Walk to different locations.

Push the box.

Climb onto the box.

Grab the banana when under it and on the box.

The goal is for the monkey to get the banana.