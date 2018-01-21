
import copy
from closure_rules import closures_of_grammar
from follow import follows_of_grammar;


def r_function(a, b, c, d, grammar, f_set):
    temp2 = int(c)
    temp1 = ((b.split('.'))[0]).replace(' ', '');
    for g in grammar:
        if a == g[0] and temp1 == g[1]:
            for i in f_set[a]:
                if d[temp2][i] == '':
                    d[temp2][i] = 'r' + str(grammar.index(g) + 1);
                elif d[temp2][i] == 'r' + str(grammar.index(g) + 1):
                    pass;
                else:
                    d[temp2][i] = d[temp2][i] + " " + 'r' + str(grammar.index(g) + 1);
            return d;




def s_function(a, b, c, d, f):
    for t in f:
        if b in t['from']:
            if a in t['on']:
                if a.isupper():
                    if d[c][a] == '':
                        d[c][a] = t['to'][0];
                    elif d[c][a] == t['to'][0]:
                        pass;
                    else:
                        d[c][a] = d[c][a] + t['to'][0];
                else:
                    if d[c][a] == '':

                        d[c][a] = 's' + t['to'][0];
                    elif d[c][a] == 's' + t['to'][0]:
                        pass;
                    else:
                        d[c][a] = d[c][a] + 's' + t['to'][0];

    return d;



def new_table(grammar1):
    grammar_list = grammar1[:]
    closure_set = closures_of_grammar(grammar1)

    grammar = [];
    for i in grammar_list:
        my_temp = i.split("->");
        grammar.append(my_temp);
        grammar[-1][0] = grammar[-1][0].replace(' ', '');
        grammar[-1][1] = grammar[-1][1].replace(' ', '');


    f_set = follows_of_grammar(grammar1)

    bishtarin = 0
    for i in closure_set:
        if int((i['to'])[0])-bishtarin >0 :
            bishtarin = int((i['to'])[0]);

    my_dictionary = {};
    my_dictionary['$'] = '';
    for g in grammar:
        my_dictionary[g[0]] = '';
        for i in list(g[1]):
            my_dictionary[i] = '';
    my_table = [];
    # e ''
    del my_dictionary['e'];
    del my_dictionary[''];

    for i in range( bishtarin + 1):
        my_table.append(copy.deepcopy(my_dictionary));

    for cs in closure_set:
        my_temp_k = cs['to'][0];
        my_temp_i = int(my_temp_k);
        for temp_itr in cs.items():
            for temp_itr2 in temp_itr[1]:
                if '.' in temp_itr2:
                    pod = temp_itr2.index('.');
                    if pod+2 < (len(temp_itr2) ):
                        my_table = s_function(temp_itr2[pod + 2], my_temp_k, my_temp_i, my_table, closure_set);
                    elif pod +2== len(temp_itr2) :
                        if len(temp_itr2) == 4:

                            my_temp_r = ((temp_itr2.split('.'))[0]).split(' ');
                            if  'H'==temp_itr[0]  and   grammar[0][0]== my_temp_r[0]:
                                my_table[my_temp_i]['$'] = 'accept';
                            else:
                                my_table = r_function(temp_itr[0], temp_itr2, my_temp_k, my_table, grammar, f_set);
                        else:
                            my_table = r_function(temp_itr[0], temp_itr2, my_temp_k, my_table, grammar, f_set);
    return my_table;

