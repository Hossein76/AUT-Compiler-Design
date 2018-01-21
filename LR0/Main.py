from string_parser import *;


grammar_path="Test_Case.txt";
grammar=[];

f=open(grammar_path,"r");

for i in list(f):
    temp=i.split("\n");
    if(temp[0]!=""):
        grammar.append(temp[0]);
f.close();
user_string="";
my_parser(user_string,grammar);



