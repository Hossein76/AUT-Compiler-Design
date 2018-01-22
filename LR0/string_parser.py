
from table_generator import new_table;


def my_parser(user_string,grammar):
    my_table=new_table(list(grammar));
    result = [];

    my_stack = ['0'];
    list_of_symbols = ['$'];
    input_list = (list(user_string));
    input_list.append('$')
    print(input_list)
    print(my_stack)


    try:

        situtaion = my_table[int(my_stack[-1])][input_list[0]];
        while situtaion != "":

            step_state = [str(my_stack), str(list_of_symbols), str(input_list), situtaion];

            if situtaion.startswith('s'):
                my_stack.append(situtaion[1:]);
                list_of_symbols.append(input_list.pop(0));
                situtaion = my_table[int(my_stack[-1])][input_list[0]];
            elif situtaion.startswith("r"):
                situtaion_before = situtaion[:];
                l_for_poping = len(grammar[int(situtaion_before[1:]) - 1].split("->")[1].strip().split(" "));
                epsilon = grammar[int(situtaion_before[1:]) - 1].split("->")[1].replace(" ", "");
                if epsilon != "e":
                    for j in range(l_for_poping):
                        my_stack.pop()
                num_upcoming_situtaion = my_table[int(my_stack[-1])][grammar[int(situtaion_before[1:]) - 1].split("->")[0].strip()];
                my_stack.append(num_upcoming_situtaion);
                list_of_symbols = list_of_symbols[0:len(list_of_symbols) - l_for_poping];
                symbol_coming = grammar[int(situtaion_before[1:]) - 1][0];
                list_of_symbols.append(symbol_coming);
                situtaion = my_table[int(my_stack[-1])][input_list[0]];
            elif situtaion.startswith("a"):
                situtaion = my_table[int(my_stack[-1])][input_list[0]];
                break;

            result.append(step_state);
        else:
            step_state = [str(my_stack),str(list_of_symbols),str(input_list),"reject"];
        result.append(step_state);


    except Exception as my_exception:
        print("something went wrong");
        return None;

    return result;
