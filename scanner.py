from lark import Lark, Token, Tree, common
import lark


def scan(code):
	parser = Lark(
			grammar= r"""
				start: (decl)+

				decl: T_KEYWORD
					| T_OTHERS
					| T_STRINGLITERAL
					| T_BOOLEANLITERAL
					| T_COMMENT
					| T_ID
					| UNDEFINED_TOKEN
					| T_OPR
					| T_INTLITERAL
					| T_DOUBLELITERAL
					| T_TYPES

				T_OTHERS: "(" 
					| ")"
					| "{" 
					| "}"


				T_KEYWORD: "return"
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
					| "interface"
					

				T_TYPES: "bool"
					| "int"
					| "double"
					| "string"

				T_BOOLEANLITERAL: "true"
					| "false"

				T_ID: CNAME	
					| T_KEYWORD (/[0-9]+/ | CNAME)
					| T_BOOLEANLITERAL (/[0-9]+/ | CNAME)

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
					



				

				T_INTLITERAL: /0[xX][0-9a-fA-F]+/ 
					| /[0-9]+/
				
				T_DOUBLELITERAL: /[0-9]+[\.][0-9]*[eE][+ | -]?[0-9]+/ | /[0-9]+\.[0-9]*/

				T_STRINGLITERAL: /"(?:[^\\"]|\\.)*"/

				T_COMMENT: /\/\/.*/
					| /\/\*(^[\*\/]*) \*\//

				UNDEFINED_TOKEN: (T_INTLITERAL CNAME) | (T_DOUBLELITERAL CNAME) | /[#$^~`]+/


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






def out_wr(tree):
	wrs = []
	for wr in tree.children:
		if type(wr) == lark.tree.Tree:
			wrs = wrs + out_wr(wr)
			continue

		if wr.type == "T_COMMENT":
			continue

		if wr.type == "T_ID":
			wrs.append(str(wr.type) + " " + str(wr))
			continue

		if wr.type == "UNDEFINED_TOKEN":
			wrs.append(str(wr.type))
			continue

		if wr.type == "T_OPR" or wr.type == "T_KEYWORD" or wr.type == "T_OTHERS" or wr.type == "T_TYPES":
			wrs.append(str(wr))
			continue

		wrs.append(str(wr.type) + " " + str(wr))

	return wrs


