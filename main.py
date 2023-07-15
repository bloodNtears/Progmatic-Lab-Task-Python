def generate_expressions(digits, expression, target):
	if not digits:
		if eval(expression) == target:
			expression = expression[1:] if expression[0] == "+" else expression
			print(expression + '=' + str(eval(expression)))
		return

	generate_expressions(digits[1:], expression + "+" + digits[0], target)
	generate_expressions(digits[1:], expression + "-" + digits[0], target)
	generate_expressions(digits[1:], expression + digits[0], target)


target = 200
digits = "9876543210"

generate_expressions(digits, "", target)
