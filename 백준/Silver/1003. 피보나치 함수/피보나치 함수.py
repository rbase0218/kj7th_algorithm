import sys

if __name__ == "__main__":
    num = int(input())
    numbers = [int(input()) for _ in range(num)]
    
    for i in numbers:
        answer = [ [0] * 2 for _ in range(40 + 1)]

        answer[0][0] = 1
        answer[1][1] = 1
        
        for j in range(2, max(numbers) + 1):
            answer[j][0] = answer[j - 2][0] + answer[j - 1][0]
            answer[j][1] = answer[j - 2][1] + answer[j - 1][1]        
            
        print(answer[i][0], answer[i][1])