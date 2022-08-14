from lark import Lark 





def parse(code):

    lines = code.split("\n")
    repl = {}
    decaf_parser = Lark(
    grammar = r"""
        begin: (declaration)+

        declaration: function_decl
            | variable_decl
            | class_decl
            | interface_decl


        function_decl: func_ident statement

        variable_decl: variable ";"

        variable: typer identifier

        class_decl: "class" identifier "{" (field)* "}"
            | "class" identifier "extends" identifier "{" (field)* "}"
            | "class" identifier "implements" multiple_id "{" (field)* "}"
            | "class" identifier "extends" identifier "implements" multiple_id "{" (field)* "}"

        field: (access_rule)? variable_decl
            | (access_rule)? function_decl


        multiple_id: identifier ("," identifier)* 

        interface_decl: "interface" identifier "{" (func_ident ";")* "}" 

        func_ident: typer identifier params
            | "void" identifier params 

        params: "(" variable ("," variable)* ")" 
            | "(" ")"


        statem: ";" 
            | expr ";"
            | if_st
            | for_st
            | while_st
            | break_st
            | return_st
            | print_st
            | statement
            | "continue" ";"


        if_st: "if" "(" expr ")" statem 
            | "if" "(" expr ")" statem "else" statem


        for_st: "for" "(" (expr)? ";" expr ";" (expr)? ")" statem


        while_st: "while" "(" expr ")" statem

        break_st: "break" ";"

        return_st: "return" ";"
            | "return" expr ";"

        print_st: "Print" param_expr_ne ";"

        param_expr_ne: "(" expr ("," expr)* ")"


        statement: "{" (variable_decl)* (statem)* "}" 
            | "{" "}"



        expr: constant
            | expr bin_op expr
            | un_op expr
            | identifier param_expr
            | expr "." identifier param_expr
            | this
            | identifier "=" expr
            | expr "." identifier "=" expr 
            | expr "[" expr "]" "=" expr 
            | "ReadInteger" "(" ")"
            | "ReadLine" "(" ")"
            | "new" identifier
            | "import"
            | "NewArray" "(" expr "," typer ")"
            | cast_types
            | identifier
            | expr "." identifier
            | expr "[" expr "]" "." identifier param_expr 
            | "(" expr ")"
            | identifier "=" identifier "[" identifier "]"
            | "new" identifier "[" expr "]"
            | identifier "[" expr "]" "=" expr
            | identifier "[" expr "]" "=" identifier "[" expr "]"
            | identifier "[" expr "]" bin_op expr
            | identifier "[" expr "]" "." identifier "(" ")"

            


        this.2: "this"


        

        cast_types: "itod" "(" expr ")"
            | "btoi" "(" expr ")"
            | "itob" "(" expr ")"
            | "dtoi" "(" expr ")"


        param_expr: "(" expr ("," expr)* ")"
            | "(" ")"

        un_op: "-" 
            | "!"

        bin_op: "+"
            | "-"
            | "*"
            | "/"
            | "%"
            | "<"
            | ">"
            | "<="
            | ">="
            | "=="
            | "!="
            | "&&"
            | "||"


        typer: types
            | identifier
            | types "[" "]" 
            | identifier "[" "]"


        constant: "null"
            | integer
            | double
            | boolean
            | string


        integer: /[0-9]+/
            | /0[xX][0-9a-fA-F]+/

        boolean.2: "true"
            | "false"

        double.2:  /(\d)+\.(\d)*(([Ee])(\+|\-)?(\d)+)?/ 
            | /(\d)+\./

        string: /"(?:\\.|[^\\"])*"/

        identifier: /(?!(else|void|class|string|dtoi|itob|itod|btoi|this|return|int|if|continue|break|bool|double)\b)[a-zA-Z][a-zA-Z0-9_]{0,50}/

        types: "int"
            | "double" 
            | "bool"
            | "string"

        COMMENT: /\/\/.*/
            | /\/\*(\*(?!\/)|[^*])*\*\//


        access_rule: "private"
            | "public" 
            | "protected"



        %ignore COMMENT
        %import common.WS
        %import common.WORD
        %ignore WS

    """,
        start="begin",
        parser="lalr",
        debug=True
    )
    for i, line in enumerate(lines):
            wrds = line.split()
            if not len(wrds):
                continue
            if wrds[0] == 'import':
                with open("./tests/"+wrds[1][1:-1], 'r') as file:
                    data = file.read()
                    try:
                        decaf_parser.parse(data)
                    except:
                        return False

                lines[i] = ''

    code = '\n'.join(lines)

    try:
        decaf_parser.parse(code)
    except:
        return False
    return True





