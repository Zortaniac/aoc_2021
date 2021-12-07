:- use_module(library(apply)).
:- use_module(library(csv)).

get_rows_data(File, Lists):-
  csv_read_file(File, Rows, []),
  rows_to_lists(Rows, Lists).

rows_to_lists(Rows, Lists):-
    maplist(row_to_list, Rows, Lists).
  
row_to_list(Row, List):-
Row =.. [row|List].

is_list([]).
is_list([_|L]) :- is_list(L).

flatten([], []).
flatten([E|L1], [E|L2]) :- \+(is_list(E)), flatten(L1, L2).
flatten([E|L1], L2) :- is_list(E), flatten(E, L2A), flatten(L1, L2B), append(L2A, L2B, L2). 

get_flatten_rows_data(File, List) :- get_rows_data(File, Lists), flatten(Lists, List), !.

parse([], []).
parse([I|IS], [[A, N]|OS]) :-
    split_string(I, "\s", "\s", [AS|[NS|[]]]),
    atom_string(A, AS), number_string(N, NS), parse(IS, OS).

simulate([], 0, 0).
simulate([[forward, N]|TS], P, D):- simulate(TS, P1, D), P is P1 + N.
simulate([[up, N]|TS], P, D):- simulate(TS, P, D1), D is D1 - N.
simulate([[down, N]|TS], P, D):- simulate(TS, P, D1), D is D1 + N.

run1(S) :- 
    get_flatten_rows_data('day_2.txt', SS),
    parse(SS, TS),
    simulate(TS, P, D),
    S is P * D, !.

simulate2([], _, 0, 0).
simulate2([[forward, N]|TS], A, P, D):- simulate2(TS, A, P1, D1), P is P1 + N, D is D1 + (A*N).
simulate2([[up, N]|TS], A, P, D):- A2 is A - N, simulate2(TS, A2, P, D).
simulate2([[down, N]|TS], A, P, D):- A2 is A + N, simulate2(TS, A2, P, D).

run2(S) :- 
    get_flatten_rows_data('day_2.txt', SS),
    parse(SS, TS),
    simulate2(TS, 0, P, D),
    S is P * D, !.

