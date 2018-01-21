
from table_generator import *;


def my_parser(user_string,grammar):
    my_table=new_table(list(grammar));
    result = [];

    stack = ['0'];
    list_of_symbols = ['$'];
    input_list = (list(user_string)).append("$");


    try:

        situtaion = my_table[int(stack[-1])][input_list[0]];

        while situtaion != "":

            step_state = [str(stack), str(list_of_symbols), str(input_list), situtaion];

            if situtaion.startswith('s'):
                stack.append(situtaion[1:]);
                list_of_symbols.append(input_list.pop(0));
                situtaion = my_table[int(stack[-1])][input_list[0]];
            elif situtaion.startswith("r"):
                situtaion_before = situtaion[:];
                l_for_poping = len(grammar[int(situtaion_before[1:]) - 1].split("->")[1].strip().split(" "));
                epsilon = grammar[int(situtaion_before[1:]) - 1].split("->")[1].replace(" ", "");
                if epsilon != "e":
                    stack=stack[0:-l_for_poping];
                    #for j in range(l_for_poping):
                    #    stack.pop()
                num_upcoming_situtaion = my_table[int(stack[-1])][
                    grammar[int(situtaion_before[1:]) - 1].split("->")[0].strip()];
                stack.append(num_upcoming_situtaion);
                list_of_symbols = list_of_symbols[0:len(list_of_symbols) - l_for_poping];
                symbol_coming = grammar[int(situtaion_before[1:]) - 1][0];
                list_of_symbols.append(symbol_coming);
                situtaion = my_table[int(stack[-1])][input_list[0]];
            elif situtaion.startswith("a"):
                situtaion = my_table[int(stack[-1])][input_list[0]];
                break;

            result.append(step_state);
        else:
            step_state = [str(stack),str(list_of_symbols),str(input_list),"reject"];

        result.append(step_state);


    except Exception as my_exception:
        return None;

    return result;
