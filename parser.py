from lark import Lark 


decaf_parser = Lark(
	grammar = r"""
		begin: (declaration)+

		declaration: function_decl
			| variable_decl
			| class_decl
			| interface_decl


		function_decl: func_ident statement

		variable_decl: variable ";"

		variable: type identifier

		class_decl: "class" identifier "{" (field)* "}"
			| "class" identifier "extends" identifier "{" (field)* "}"
			| "class" identifier "implements" identifier "{" (field)* "}"
			| "class" identifier "extends" identifier "implements" identifier "{" (field)* "}"

		field: variable_decl
			| function_decl


		interface_decl: "interface" identifier "{" (func_ident ";")* "}" 

		func_ident: type identifier params
		| "void" identifier params 

		params: "(" variable ("," variable)* ")"


		statem: ";" 
			| expr ";"
			| if_st
			| for_st
			| while_st
			| break_st
			| return_st
			| print_st
			| statement


		if_st: "if" "(" expr ")" statem 
			| "if" "(" expr ")" statem "else" statem


		for_st: "for" "(" (expr)? ";" expr ";" (expr)? ")" statem


		while_st: "while" "(" expr ")" statem

		break_st: "break" ";"

		return_st: "return" ";"
			| "return" expr ";"

		print_st: "Print" "(" expr ("," expr)* ")" ";"

		



	"""
	)