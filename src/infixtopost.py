#!/bin/python3

##
#@brief Function to evaluate operator precendcde
#
def eval_precedence(operator):
    if operator == "(": 
        return 0
    elif operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    elif operator == "^":
        return 3

##
#@return True if operand is a digit
#
def is_operand(operand):
    return operand.isdigit()

##
#@return True if operator is one of +-*/^
#
def is_operator(operator):
    return operator in "+-^*/"

def InfixToPostFix(parse_string):
    stack_operator = []
    return_post=""
    tokens = parse_string.split()
    #ITERATE EXPRESSION
    for i in tokens:
        
        #IF SYMBOL IS OPERAND
        if is_operand(i):
            return_post+=i + " "
        
        #IF SYMBOL LEFT PARENTHESIS
        elif i =="(":
            stack_operator.append("(")

        #IF SYMBOL RIGHT PARENTHESIS
        elif i == ")":
            while stack_operator[-1] != "(":
                return_post+=stack_operator[-1] + " "
                stack_operator.pop()           
            stack_operator.pop()
        
        #IF SYMBOL OPERATOR
        elif is_operator(i):
            
            operator_precedence=eval_precedence(i)

            if len(stack_operator) == 0:
                stack_operator.append(i)
            
            elif len(stack_operator) != 0:
                last_operator_precedence=eval_precedence(stack_operator[-1])
                
                if operator_precedence > last_operator_precedence:
                    stack_operator.append(i)

                elif operator_precedence <= last_operator_precedence:
                    while operator_precedence <= last_operator_precedence and len(stack_operator) > 0:
                        return_post+=stack_operator[-1] + " "
                        stack_operator.pop()
                        if len(stack_operator) > 0:
                            last_operator_precedence=eval_precedence(stack_operator[-1])
                    stack_operator.append(i)

    for i in range(len(stack_operator)):
        return_post+=stack_operator.pop() + " "
    
    return return_post

parse_string = "2 ^ 3 * ( 5 - 1 ) + 10 / 2"
output = InfixToPostFix(parse_string)
print(output)
