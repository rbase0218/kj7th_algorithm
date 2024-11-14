if __name__ == "__main__":
    n = input()
    alphabetStr = "abcdefghijklmnopqrstuvwxyz"

    alphabet = []
    # -1로 모든 값을 초기화
    for i in range(26):
        alphabet.append(-1);
    
    idx = 0
    for j in range(len(alphabetStr)):
        try:
            idx = n.index(alphabetStr[j])
        except ValueError:
            continue

        if idx != -1:
            alphabet[j] = idx;
    
    print(*alphabet);