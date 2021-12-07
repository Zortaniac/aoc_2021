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

change(A, B, C) :- A < B, C = increased. 
change(A, B, C) :- B < A, C = decreased. 
change(A, B, C) :- A = B, C = no_change. 

calculate_changes([], _, []).
calculate_changes([I|IL], L, [O|OL]) :- change(L, I, O), calculate_changes(IL, I, OL), !.

count_increases([], 0).
count_increases([I|IS], C) :- I = increased, count_increases(IS, C1), C is C1 + 1, !.
count_increases([I|IS], C) :- \+(I = increased), count_increases(IS, C), !.

calculate_sliding_window([_|[_]], []).
calculate_sliding_window([A|[B|[C|IS]]], [O|OS]) :- O is A + B + C, calculate_sliding_window([B|[C|IS]], OS).

run1(C) :- 
    get_flatten_rows_data('day_1.txt', [L|LS]),
    calculate_changes([L|LS], L, RS),
    count_increases(RS, C).

run2(C) :- 
    get_flatten_rows_data('day_1.txt', LS),
    calculate_sliding_window(LS, [O|OS]),
    calculate_changes([O|OS], O, RS),
    count_increases(RS, C), !.

