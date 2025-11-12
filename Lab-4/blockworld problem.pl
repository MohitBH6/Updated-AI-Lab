% --- Facts: Initial Configuration ---
on(a, b).
on(b, table).
on(c, table).

% --- Rules: Legal Moves ---
clear(X) :- not(on(_, X)).

move(X, Y) :-
    clear(X),
    clear(Y),
    on(X, Z),
    retract(on(X, Z)),
    assert(on(X, Y)),
    write('Moved '), write(X), write(' from '), write(Z), write(' to '), write(Y), nl.

move(X, table) :-
    clear(X),
    on(X, Y),
    retract(on(X, Y)),
    assert(on(X, table)),
    write('Moved '), write(X), write(' from '), write(Y), write(' to table'), nl.

% --- Goal Test ---
goal_state :-
    on(b, c),
    on(a, b),
    on(c, table),
    write('Goal state achieved!'), nl.
