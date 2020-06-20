def onp(exp):
    output = ""    
    stack = []
    op_key = {'+':0,'-':0,'*':1,'/':2,'^':3}

    for i in range(0,len(exp)):
        if(exp[i] in op_key.keys()):
            while(len(stack)>0 and stack[len(stack)-1] != '(' and op_key[exp[i]]<=stack[len(stack)-1]):
                output += stack.pop()
            stack.append(exp[i])
        elif exp[i] == '(':
            stack.append('(')
        elif exp[i] == ')':
            while(len(stack)>0 and stack[len(stack)-1]!='('):
                output += stack.pop()
            if(len(stack)>0):
                stack.pop()
        else:
            output += exp[i]

    return output

T = int(input())
op = []
while T>0:
    exp = input()
    op.append(onp(exp))
    T-=1
for i in range(0,len(op)):
    print(op[i])