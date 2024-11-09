import sys
input = sys.stdin.readline

if __name__ == "__main__":
    c = int(input())
    t = list(map(int, input().split()))
    ls = set(range(0, c))
    ac = int(input())
    
    curr_sum = sum(t)
    
    print(curr_sum)
    for i in range(0, ac):
        s = list(map(int, input().split()))
        if s[0] == 1:
            new = s[2]
            if s[1] - 1 in ls:
                curr_sum = curr_sum - t[s[1] - 1] + new
            t[s[1] - 1] = new
        else:
            if s[1] - 1 in ls:
                ls.remove(s[1] - 1)
                curr_sum -= t[s[1] - 1]
            else:
                ls.add(s[1] - 1)
                curr_sum += t[s[1] - 1]
        print(curr_sum)