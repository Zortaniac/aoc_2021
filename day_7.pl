read_file(S) :-
    open('day_7.txt', read, Str),
    read_line_to_string(Str, S),
    close(Str).

parse([], []).
parse([I|IS], [N|NS]) :-
    number_string(N, I), parse(IS, NS).


move([], _, 0).
move([A|AS], P, C) :- move(AS, P, C1), abs(A-P, D), C is C1 + D.

minimum(A, B, A) :- A < B, !.
minimum(_, B, B).

find_min(NS, 0, C) :- move(NS, 0, C), !.
find_min(NS, P, C) :- P1 is P-1, move(NS, P, CP), find_min(NS, P1, CM), minimum(CP, CM, C).

run1(C) :-
    read_file(S),
    split_string(S, ",", "\s", SS),
    parse(SS, NS),
    max_list(NS, P),
    find_min(NS, P, C).

calc_dist(A, P, O) :- abs(A-P, N), O is (N * (N+1)) / 2.

move2([], _, 0).
move2([A|AS], P, C) :- move2(AS, P, C1), calc_dist(A, P, D), C is C1 + D.

find_min2(NS, 0, C) :- move2(NS, 0, C), !.
find_min2(NS, P, C) :- P1 is P-1, move2(NS, P, CP), find_min2(NS, P1, CM), minimum(CP, CM, C).

run2(C) :-
    read_file(S),
    split_string(S, ",", "\s", SS),
    parse(SS, NS),
    max_list(NS, P),
    find_min2(NS, P, C).
