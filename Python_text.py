def calculate(expression):
    stack = []
    num = 0
    sign = '+'
    
    for i in range(len(expression)):
        ch = expression[i]
        
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in "+-*/" or i == len(expression) - 1:
            
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                if num == 0:
                    return "Error: Division by zero"
                stack.append(int(stack.pop() / num)) 
            
            sign = ch
            num = 0
    
    return sum(stack)


x = input().strip()
x = x.replace(" ", "")
print(calculate(x))