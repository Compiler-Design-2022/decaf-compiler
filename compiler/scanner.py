from lark import Lark, Token, Tree, common
import lark


def scan(code):
	lines = code.split("\n")
	repl = {}
	for i, line in enumerate(lines):
		wrds = line.split()
		if not len(wrds):
			continue
		if wrds[0] == 'define':
			repl[wrds[1]] = ' '.join(wrds[2:])
			lines[i] = ''

		for rep in repl.keys():
			# print(rep)
			lines[i] = lines[i].replace(rep, repl[rep])
			# print(lines[i])

	code = '\n'.join(lines)
	# print(code)
	# print("ss")
	parser = Lark(
			grammar= r"""
				start: (decl)+

				decl: T_KEYWORD
					| T_CHAR
					| T_STRINGLITERAL
					| T_BOOLEANLITERAL
					| T_COMMENT
					| T_ID
					| UNDEFINED_TOKEN
					| T_OPR
					| T_INTLITERAL
					| T_DOUBLELITERAL
					| T_TYPES
					| T_BAD_ID
					| T_INTERFACE
					| T_DEF


				T_CHAR: "(" 
					| ")"
					| "{" 
					| "}"


				T_KEYWORD.2: "return"
					| "else"
					| "if"
					| "while"
					| "for"
					| "implements"
					| "extends"
					| "this"
					| "null"
					| "class"
					| "interface"
					| "void"
					| "public"
					| "protected"
					| "private"
					| "btoi"
					| "itob"
					| "itod"
					| "dtoi"
					| "ReadLine"
					| "ReadInteger"
					| "Print"
					| "NewArray"
					| "new"
					| "continue"
					| "break"
					| "import" 
					
				
				T_INTERFACE.4: "interface"


				T_DEF.2: /\_\_[a-zA-Z]+\_\_/


				T_TYPES.2: "bool"
					| "int"
					| "double"
					| "string"

				T_BOOLEANLITERAL.2: "true"
					| "false"

				T_ID: CNAME	

				T_BAD_ID.3: (T_KEYWORD (/[0-9]+/ | CNAME))
					| T_BOOLEANLITERAL (/[0-9]+/ | CNAME) 
					| (T_TYPES (/[0-9]+/ | CNAME))

	
 				T_OPR: "<="
                    | ">="
                    | "!="
                    | "=="
                    | "!="
                    | /[+*-=()%<>;:!,]/
                    | "||"
                    | "["
                    | "/"
                    | "."
                    | "]"
                    | "&&"
                    | "+="
                    | "-="
                    | "*="
                    | "/="


				

				T_INTLITERAL.2: /0[xX][0-9a-fA-F]+/ 
					| /[0-9]+/
				
				T_DOUBLELITERAL.2: /[0-9]+[\.][0-9]*[eE][+ | -]?[0-9]+/ | /[0-9]+\.[0-9]*/

				T_STRINGLITERAL: /"(?:\\.|[^\\"])*"/

				T_COMMENT: /\/\/.*/
					| /\/\*(^[\*\/]*) \*\//

				UNDEFINED_TOKEN: (T_INTLITERAL CNAME) 
					| (T_DOUBLELITERAL CNAME) 
					| /[#$^~`]+/


				%ignore T_COMMENT



				%import common.WORD
				%import common.CNAME
				%import common.WS

				%ignore WS

			""",
			parser="lalr",
			transformer=None,
			debug=True 
		)
	
	return out_wr(parser.parse(code))


code = """
define SEMICOLON ;
define FOR100 for(i = 0; i < 100; i += 1)

FOR100
Print(i)SEMICOLON
"""
"that had just walked in. Hey, he says, \"aren't you a string?\""


	# T_STRINGLITERAL: /"(?:[^\\"]|\\.)*"/
def out_wr(tree):
	wrs = []
	for wr in tree.children:
		
		if type(wr) == lark.tree.Tree:
			wrs = wrs + out_wr(wr)
			continue


		# print(str(wr), "Sss", wr.type)
		if wr.type == "T_COMMENT":
			continue

		if wr.type == "T_BAD_ID":
			wrs.append("T_ID" + " " + str(wr))
			continue

		if wr.type == "UNDEFINED_TOKEN":
			wrs.append(str(wr.type))
			continue

		if wr.type == "T_OPR" or wr.type == "T_KEYWORD" or wr.type == "T_CHAR" or wr.type == "T_TYPES" or wr.type=="T_INTERFACE" or wr.type=="T_DEF":
			wrs.append(str(wr))
			continue

		wrs.append(str(wr.type) + " " + str(wr))

	return wrs


# print(*scan(code), sep="\n")