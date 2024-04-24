#
# Complete the 'pol_notation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY tokens as parameter.
#

def pol_notation(tokens):
    # Write your code here
    stack = []
    operators = ['+','-','*','/']
    # res = 0

    for toke in tokens:
        print(stack)
        if toke not in operators:
            stack.append(int(toke))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if toke == '+':
                stack.append(num2 + num1)
            if toke == '-':
                stack.append(num2 - num1)
            if toke == '*':
                stack.append(num2 * num1)
            if toke == '/':
                res = num2 // num1
                if res < 1:
                    res = 0
                stack.append(res)

    return stack[0]
