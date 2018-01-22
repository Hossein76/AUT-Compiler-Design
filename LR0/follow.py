import re;


class firstclass:
    def __init__(self):
        pass;

    def get_first(self,grammar):
        first_dictionary = {};
        for i in grammar.keys():
            first_dictionary[i] = self.fl_function(i, grammar, first_dictionary);

        for i in first_dictionary:
            first_dictionary[i] = list(set(first_dictionary[i]));

        self.ce_function(grammar, first_dictionary);
        return first_dictionary;

    def fl_function(self,nt, grammar, first):

        first_list = [];
        for i in grammar[nt]:

            reg_result = re.search("[A-Z]+", i);
            if reg_result:
                if reg_result.start() > 0:
                    first_list.append(i[0]);
                elif reg_result.start() == 0:
                    temp = self.ns_function(i, first, grammar);
                    if temp:
                        first_list = first_list + temp;

            else:
                if i is not "e":
                    first_list.append(i[0]);

        if "e" in grammar[nt]:
            if "e" not in first_list:
                first_list.append("e");

        return first_list;

    def ns_function(self,production, first, grammar):
        first_list = [];
        for i in production:
            if i in first:
                first_list = first_list + first[i];

            else:
                if i.isupper():
                    first_list = first_list + self.fl_function(i, grammar, first);
                else:
                    return first_list;

            if len(production) > 1:

                if "e" in grammar[i]:
                    for j in range(first_list.count("e")):
                        first_list.remove("e");

                    if production.index(i) + 1 < len(production) and production[production.index(i) + 1:][
                        0].isupper():
                        temp = self.fl_function(production[production.index(i) + 1:][0], grammar, first);
                        first_list = first_list + temp;
                        if "e" in temp:
                            continue;
                        else:
                            return first_list;

                    elif production.index(i) + 1 < len(production) and production[production.index(i) + 1:][
                        0].islower():
                        first_list.append(production[production.index(i) + 1:][0]);
                        return first_list;
                else:
                    return first_list;

        return first_list;

    def ce_function(self,grammar, first):
        for nt in grammar.keys():
            for i in grammar[nt]:
                reg_result = re.match("[A-Z]+", i);
                if reg_result:
                    if reg_result.end() == len(i):
                        epsilon = True;
                        for symbol in i:
                            if 'e' not in first[symbol]:
                                epsilon = False;
                                break;
                        if epsilon:
                            if 'e' not in first[nt]:
                                first[nt].append('e');
                        else:
                            if 'e' in first[nt]:
                                first[nt].remove('e');








def follows_of_grammar(grammar):
    my_object=firstclass();
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

    first_set = my_object.get_first(g_d);

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
    keys_temp_list = []
    for i in found_ones.keys():
        if 0==len(found_ones[i]):
            keys_temp_list.append(i);
    for i in keys_temp_list:
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