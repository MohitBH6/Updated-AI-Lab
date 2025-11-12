% --- State Representation ---
% state(MonkeyPosition, BoxPosition, MonkeyStatus, HasBanana)

% Initial state
initial(state(atdoor, atwindow, onfloor, hasnot)).

% Goal state
goal(state(_, _, _, has)).

% --- Actions ---
move(state(atdoor, Box, onfloor, hasnot), grasp, state(atdoor, Box, onbox, has)) :-
    Box = atdoor.

move(state(atwindow, atwindow, onfloor, hasnot), push, state(atdoor, atdoor, onfloor, hasnot)).

move(state(atdoor, Box, onfloor, hasnot), climb, state(atdoor, Box, onbox, hasnot)).

move(state(atwindow, Box, onfloor, hasnot), walk, state(atdoor, Box, onfloor, hasnot)).

move(state(atdoor, Box, onbox, hasnot), grasp, state(atdoor, Box, onbox, has)).

% --- Recursive Path Finder ---
path(State, []) :- goal(State), write('Monkey got the banana!'), nl.
path(State1, [Move | Rest]) :-
    move(State1, Move, State2),
    write('Monkey performs: '), write(Move), nl,
    path(State2, Rest).
