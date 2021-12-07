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

bin_to_dec(['0'], 0, 0).
bin_to_dec(['1'], 0, 1).
bin_to_dec(['0'|LS], P, Z) :- bin_to_dec(LS, P1, Z), P is P1+1.
bin_to_dec(['1'|LS], P, Z) :- bin_to_dec(LS, P1, Z1), P is P1+1, Z is Z1 + 2^P.

numbers_strings([], []).
numbers_strings([N|NS], [S|SS]) :- number_string(N, S), numbers_strings(NS, SS).

strings_chars([], []).
strings_chars([S|SS], [C|CC]) :- string_chars(S, C), strings_chars(SS, CC).

find_bin_pos(N, P, P) :- N < 2^P, !.
find_bin_pos(N, PI, PO) :- P1 is PI + 1, find_bin_pos(N, P1, PO).

bins_to_decs([], []).
bins_to_decs([B|BS], [D|DS]) :- string_chars(B, BC), bin_to_dec(BC, _, D), bins_to_decs(BS, DS).

calc(1, 0, [1]).
calc(0, 0, [-1]).
calc(N, P, [O|OS]) :- N < 2^P, O is -1, P1 is P-1, calc(N, P1, OS).
calc(N, P, [O|OS]) :- N1 is N - (2^P), O is 1, P1 is P-1, calc(N1, P1, OS).

calc_list([], [], _).
calc_list([I|LI], [O|LO], P) :- calc(I, P, O), calc_list(LI, LO, P).

zip_elems([], [], []).
zip_elems([E|LS], [], [[E]|OS]) :- zip_elems(LS, [], OS), !.
zip_elems([E|LS], [I|IS], [O|OS]) :- append(I, [E], O), zip_elems(LS, IS, OS).

sum_lists([], [], []).
sum_lists([A|AS], [B|BS], [C|CS]) :- C is A + B, sum_lists(AS, BS, CS).

process_lists([], A, A).
process_lists([I|LI], IS, OS) :- sum_lists(I, IS, OS1), process_lists(LI, OS1, OS).

calc_to_number([I], 0, 0) :- I < 0, !.
calc_to_number([_], 0, 1).
calc_to_number([I|LS], P, N) :- I < 0, calc_to_number(LS, P1, N), P is P1+1, !.
calc_to_number([_|LS], P, N) :- calc_to_number(LS, P1, N1), P is P1+1, N is N1 + 2^P, !.

pos_to_num(0, 1).
pos_to_num(P, N) :- P1 is P -1, pos_to_num(P1, N1), N is N1 + 2^P.

run1(PC) :- 
    get_flatten_rows_data('day_3.txt', NS),
    numbers_strings(NS, SS),
    bins_to_decs(SS, BS), 
    max_list(BS, M),
    find_bin_pos(M, 0, P),
    calc_list(BS, [X|XS], P-1),
    process_lists(XS, X, O),
    calc_to_number(O, _, GR),
    pos_to_num(P-1, N),
    ER is GR xor N,
    PC is GR * ER, !.

compute_bit_position([], 0).
compute_bit_position([[X|_]|LS], O) :- compute_bit_position(LS, O1), O is O1 + X.

filter(_, [], []).
filter(F, [[I|_]|LS], OS) :- F < 0, I > 0, filter(F, LS, OS), !.
filter(F, [[I|IS]|LS], [[I|IS]|OS]) :- F < 0, I < 0, filter(F, LS, OS), !.
filter(F, [[I|_]|LS], OS) :- I < 0, filter(F, LS, OS), !.
filter(F, [[I|IS]|LS], [[I|IS]|OS]) :- filter(F, LS, OS), !.

trim([], []).
trim([[_|I]|LS], [I|OS]) :- trim(LS, OS).

walk_ogr([[]], []).
walk_ogr(XS, [O|OS]) :- 
    compute_bit_position(XS, O),
    filter(O, XS, XS1),
    trim(XS1, XS2),
    walk_ogr(XS2, OS).

filter2(_, [], []).
filter2(F, [[I|_]|LS], OS) :- F > 0, I < 0, filter2(F, LS, OS), !.
filter2(F, [[I|IS]|LS], [[I|IS]|OS]) :- F > 0, I > 0, filter2(F, LS, OS), !.
filter2(F, [[I|_]|LS], OS) :- I > 0, filter2(F, LS, OS), !.
filter2(F, [[I|IS]|LS], [[I|IS]|OS]) :- filter2(F, LS, OS), !.

walk_csr([X], X).
walk_csr(XS, [O1|OS]) :- 
    compute_bit_position(XS, O),
    O1 is (O*(-1))-1,
    filter2(O1, XS, XS1),
    trim(XS1, XS2),
    walk_csr(XS2, OS), !.

run2(O) :- 
    get_flatten_rows_data('day_3.txt', NS),
    numbers_strings(NS, SS),
    bins_to_decs(SS, BS), 
    max_list(BS, M),
    find_bin_pos(M, 0, P),
    calc_list(BS, XS, P-1),
    walk_ogr(XS, OOGR),
    calc_to_number(OOGR, _, OGR),
    walk_csr(XS, OCSR),
    calc_to_number(OCSR, _, CSR),
    O is OGR * CSR, !.

