stack = []

def push(count: int):
    stack.append(count)
    
def pop() -> int:
    if empty() == 1:
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)
    
def empty()-> int:
    if len(stack) <= 0:
        return 1
    else:
        return 0
    
def top():
    if empty() == 1:
        print('-1')
    else:
        print(stack[len(stack) - 1])

command_count = int(input())
for i in range(command_count):
    command = input()
    if command[1] == 'u':
        push(int(command.split(' ')[1]))
    elif command == 'pop':
        print(pop())
    elif command == 'size':
        print(size())
    elif command == 'empty':
        print(empty())
    elif command == 'top':
        top()