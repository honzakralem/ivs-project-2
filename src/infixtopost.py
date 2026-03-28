#!/bin/python3

from mathlib import *
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
#@return True if operand is a number
#
def is_operand(operand):
    try: 
        value = float(operand)
    except ValueError:
        return False
    else:
        return True 

##
#@return True if operator is one of +-*/^
#
def is_operator(operator):
    return operator in "+-^*/"


def InfixToPostFix(parse_string):
    stack_of_operators = []
    output_postfix=""
    tokens = parse_string.split()
    
    #ITERATE EXPRESSION
    for i in tokens:
        
        #IF SYMBOL IS OPERAND
        if is_operand(i):
            output_postfix+=i + " "
        
        #IF SYMBOL LEFT PARENTHESIS
        elif i =="(":
            stack_of_operators.append("(")

        #IF SYMBOL RIGHT PARENTHESIS
        elif i == ")":
            while stack_of_operators[-1] != "(":
                output_postfix+=stack_of_operators[-1] + " "
                stack_of_operators.pop()           
            stack_of_operators.pop()
        
        #IF SYMBOL OPERATOR
        elif is_operator(i):
            
            operator_precedence=eval_precedence(i)

            if len(stack_of_operators) == 0:
                stack_of_operators.append(i)
            
            elif len(stack_of_operators) != 0:
                last_operator_precedence=eval_precedence(stack_of_operators[-1])
                
                if operator_precedence > last_operator_precedence:
                    stack_of_operators.append(i)

                elif operator_precedence <= last_operator_precedence:
                    while operator_precedence <= last_operator_precedence and len(stack_of_operators) > 0:
                        output_postfix+=stack_of_operators[-1] + " "
                        stack_of_operators.pop()
                        if len(stack_of_operators) > 0:
                            last_operator_precedence=eval_precedence(stack_of_operators[-1])
                    stack_of_operators.append(i)

    for i in range(len(stack_of_operators)):
        output_postfix+=stack_of_operators.pop() + " "
    
    return output_postfix

def eval_postfix(postfix_string):
    if not isinstance(postfix_string, str):
        raise TypeError
    
    tokens = postfix_string.split()
    operands_stack = []
    

    for token in tokens:

        if is_operand(token):
            operands_stack.append(token)
        
        elif is_operator(token):
            
            match token:
                case "+":
                    operand1 = float(operands_stack.pop())
                    operand2 = float(operands_stack.pop())
                    result = add(operand1,operand2)
                    operands_stack.append(result)
                case "-":
                    operand1 = float(operands_stack.pop())
                    operand2 = float(operands_stack.pop())
                    result = sub(operand2,operand1)
                    operands_stack.append(result)
                case "*":
                    operand1 = float(operands_stack.pop())
                    operand2 = float(operands_stack.pop())
                    result = mul(operand1,operand2)
                    operands_stack.append(result)
                case "/":
                    operand1 = float(operands_stack.pop())
                    operand2 = float(operands_stack.pop())
                    result = div(operand2,operand1)
                    operands_stack.append(result)
        
    final_result = float(operands_stack.pop())
    return final_result


if __name__ == "__main__":
    parse_string = "2 * 3 * ( 5 - 1 ) + -10.2 / 2"
    output = InfixToPostFix(parse_string)
    result = eval_postfix(output)
    print(output)
    print(result)


#Todo
#Zkusit zakomponovat sqt() a pow() a bodouci ln() jako operator
#Evaluation 