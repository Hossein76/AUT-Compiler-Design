from first import get_first


def follows_of_grammar(grammar):
    no_follow = {};
    follow_dictionary = {};
    g_d = {};
    ordered_symbol = [];
    for i in grammar:
        my_temp = i.split("->");
        my_temp[0] = my_temp[0].replace(" ", "")
        my_temp[0] = my_temp[0].replace("\n", "")
        my_temp[1] = my_temp[1].replace(" ", "")
        my_temp[1] = my_temp[1].replace("\n", "")
        if not (my_temp[0] in ordered_symbol):
            ordered_symbol.append(my_temp[0])
        if (my_temp[0] in  g_d):
            g_d[my_temp[0]].append(my_temp[1]);
        else: g_d[my_temp[0]] = [my_temp[1]];

    first_set = get_first(g_d);

    for i in ordered_symbol[1:]:
        follow_dictionary[i] = [];
    follow_dictionary[ordered_symbol[0]] = ['$'];

    for i in ordered_symbol:
        my_temp = fp_function(g_d, i);
        operation_function(my_temp, first_set, follow_dictionary, no_follow, i);

    for i in no_follow.keys():
        if 0<len(no_follow[i]):
            for j in no_follow[i]:
                for k in follow_dictionary[j]:
                    if not (k in follow_dictionary[i]):
                        follow_dictionary[i].append(k);

    return follow_dictionary;


def fp_function(grammar, s):
    found_ones = {};
    for i in grammar.keys():
        my_temp = [];
        for j in grammar[i]:
            if s in j:
                my_temp.append(j);
        found_ones[i] = my_temp;
    for i in found_ones.keys():
        if 0==len(found_ones[i]):
            del found_ones[i];
    return found_ones;


def operation_function(productions, first_set, follow, no_follow, symbol):
    no_follow[symbol] = []

    for a in productions.keys():
        for b in productions[a]:
            flag = 0;
            i = -1;
            for c in b:
                if (flag == 0):
                    i +=1;
                    if c == symbol:
                        flag = 1;

                        if (i + 1) is len(b):
                            if not (a == b[i]):
                                if len(follow[a]) == 0:
                                    no_follow[symbol].append(a);
                                else:
                                    for d in follow[a]:

                                        if not (d in follow[symbol]):
                                            follow[symbol].append(d);
                            else:
                                if not ("$" in follow[symbol]):
                                    follow[symbol].append("$");

                        else:
                            my_list = [];
                            flag2 = 0;
                            row_nt_num = 0;
                            epsilon_num = 0;
                            for s in range((i + 1), len(b)):
                                if not (b[s].isupper()):
                                    flag2 = 1;
                                    my_list.append(b[s]);
                                    row_nt_num = 0;
                                    epsilon_num = 0;
                                    break;

                                else:
                                    row_nt_num +=1;
                                    epsilon_flag = 0;
                                    for f in first_set[b[s]]:
                                        if f == "e":
                                            epsilon_num +=1;
                                            epsilon_flag = 1;
                                        else:
                                            if not (f in my_list):
                                                my_list.append(f);
                                    if epsilon_flag == 0:
                                        break;
                            if flag2 == 1:
                                for w in my_list:
                                    follow[symbol].append(w);


                            elif   row_nt_num != 0 and   epsilon_num==row_nt_num :

                                for m in follow[a]:
                                    if not (m in follow[symbol]):
                                        follow[symbol].append(m);

                                for q in my_list:
                                    if not (q in follow[symbol]):
                                        follow[symbol].append(q);

                            elif row_nt_num != epsilon_num:
                                for z in my_list:
                                    if not (z in follow[symbol]):
                                        follow[symbol].append(z);

                    else:
                        continue;