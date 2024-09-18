num = int(input())
tree_edge = [input() for _ in range(num)]


# Text를 추가해서 반환 값으로 해당 Text의 Index를 반환한다.
def find_index(text : str) -> int:    
    for i, item in enumerate(tree_edge):
        if item[0] == text:
            return i
    return -1

# Pre Order -> A B C
# In Order -> B A C
# Post Order -> B C A
def preorder(text : str):
    if text == '.':
        return
    
    result = find_index(text)
    if result == -1:
        return
    
    print(text, end = '')
    preorder(tree_edge[result][2])
    preorder(tree_edge[result][4])

def inorder(text : str):
    if text == '.':
        return
    
    result = find_index(text)
    if result == -1:
        return
    
    inorder(tree_edge[result][2])
    print(text, end = '')
    inorder(tree_edge[result][4])
    
def postorder(text : str):
    if text == '.':
        return
    
    result = find_index(text)
    if result == -1:
        return
    
    postorder(tree_edge[result][2])
    postorder(tree_edge[result][4])
    print(text, end = '')
    
preorder('A')
print('')
inorder('A')
print('')
postorder('A')