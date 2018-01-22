
import re;


class myclass:
    def __init__(self):
        self.sl = [];
        self.name = " ";
        self.fro = " ";
        self.on = " ";
        self.D = {};
    def setname(self, nu):
        self.name = str(nu);
    def setfron(self, fr, o):
        self.fro = fr;
        self.on = o;
    def __eq__(self,it):
        if self.sl == it.sl:
            return 1;
        else:
            return 0;


def findSym(a):
    temp_list = []
    for i in a.sl:
        reg_result = re.search(".*[.](.).*", i);
        if reg_result:
            if reg_result.group(1) not in temp_list:
                temp_list.append(reg_result.group(1));
    return temp_list;


def sd_function(i):
    reg_result = re.search("(.*)[.](.)(.*)", i);
    return reg_result.group(1) + reg_result.group(2) + '.' + reg_result.group(3);


def cl_function(a, temp, sym):
    temp_list = [];
    for i in a:
        reg_result = re.match('(%s)->.*' % sym, i);
        if reg_result:
            temp.append(reg_result.group());
            temp_list.append(reg_result.group());

    for j in temp:
        if j in a:
            a.remove(j);

    for k in temp_list:
        reg_result = re.search('.*[.](.).*',k);
        if reg_result:
            ch = str(reg_result.group(1));
            if (ch != sym) and (ch.isupper()):
                cl_function(a, temp, ch);




def closures_of_grammar(grammar):
    my_temp_list = [];
    for i in grammar:
        my_temp_list.append(i.replace(" ", ""));
    reg_result = re.search("(.)->.*", my_temp_list[0]);
    ns = 'H' + '->' + reg_result.group(1);
    my_temp_list.insert(0, ns);
    my_temp_list2 = [];
    for i in my_temp_list:
        reg_result = re.search("(.*)->(.*)", i);
        if reg_result.group(2) == 'e':
            my_temp = reg_result.group(1) + '->' + reg_result.group(2) + '.';
            my_temp_list2.append(my_temp);
        else:
            my_temp = reg_result.group(1) + '->' + '.' + reg_result.group(2);
            my_temp_list2.append(my_temp);
    my_temp_list3 = []
    my_temp_list4 = my_temp_list2[:];
    reg_result = re.search(".*[.](.).*", my_temp_list2[0]);
    cl_function(my_temp_list4, my_temp_list3, reg_result.group(1));
    my_temp_list3.insert(0, my_temp_list2[0]);

    my_temp_list5 = [];
    object_1 = myclass();
    object_1.setname('0');
    my_temp_list5.append(object_1)
    for i in my_temp_list3:
        object_1.sl.append(i);
    v_list = [];
    count = 0;
    for i in my_temp_list5:
        if i.name in v_list:
            continue;
        else:
            v_list.append(i.name);
            symlist = findSym(i);
            for sym in symlist:
                object_2 = myclass();
                my_temp_list6 = [];
                for j in i.sl:
                    m1 = re.match('.*[.](.).*', j);
                    if m1 and m1.group(1) == sym:
                        my_temp_list6.append(m1.group());
                my_temp_list7= [];
                for j in my_temp_list6:
                    my_temp_list7.append(sd_function(j));
                for s in my_temp_list7:
                    object_2.sl.append(s);
                    tlist = [];
                    m1 = re.search("(.)->.*[.](.).*", s);
                    if m1:
                        ch1 = m1.group(1);
                        ch2 = m1.group(2);
                        if (ch2.isupper()):
                            my_temp_list4 = my_temp_list2[:];
                            cl_function(my_temp_list4, tlist, ch2);
                    for stri in tlist:
                        object_2.sl.append(stri);
                object_3 = myclass();
                for j in object_2.sl:
                    if j not in object_3.sl:
                        object_3.sl.append(j);
                del (object_2);
                object_3.setfron(i.name, sym);
                flag = 1;
                for j in range(0, len(my_temp_list5)):
                    if my_temp_list5[j].sl == object_3.sl:
                        flag = 0;
                        name = my_temp_list5[j].name[:];
                        object_3.setname(name);
                        break;
                if flag == 1:
                    count += 1;
                    object_3.setname(count);
                my_temp_list5.append(object_3);
    list_of_closure = [];

    for j in range(0, len(my_temp_list5)):
        d = {};
        d['from'] = [my_temp_list5[j].fro];
        d['to'] = [my_temp_list5[j].name];
        d['on'] = [my_temp_list5[j].on];
        for k in my_temp_list5[j].sl:
            m1 = re.search("(.)->(.*)", k);
            str1 = m1.group(1)[:];
            str2 = m1.group(2)[:];
            if str1 in d.keys():
                d[str1].append(insert_space(str2));
            else:
                d[str1] = [insert_space(str2)];
        list_of_closure.append(d);
    return list_of_closure;



def insert_space(mystring):
    temp_string = ""
    for i in mystring:
        temp_string = temp_string + i + ' ';
    return temp_string;




def findSym(a):
    temp_list = []
    for i in a.sl:
        reg_result = re.search(".*[.](.).*", i);
        if reg_result:
            if reg_result.group(1) not in temp_list:
                temp_list.append(reg_result.group(1));
    return temp_list;


def sd_function(i):
    reg_result = re.search("(.*)[.](.)(.*)", i);
    return reg_result.group(1) + reg_result.group(2) + '.' + reg_result.group(3);

