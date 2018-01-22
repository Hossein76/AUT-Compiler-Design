from string_parser import my_parser;


grammar_path="g3.txt"; #g1.txt g2.txt g3.txt

                       #  A->bA  it is wrong ... put empty space between b and A
                       #  A->b A it is correct


user_string="bbbbbd";  # your input string







grammar=[];

f=open(grammar_path,"r");

for i in list(f):
    temp=i.split("\n");
    if(temp[0]!=""):
        grammar.append(temp[0]);
f.close();
final_result=( my_parser(user_string,grammar))

if(final_result!=None):
    for i in final_result:
        print(i);

