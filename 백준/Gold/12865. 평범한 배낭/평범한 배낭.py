import sys

def knapSack(b_w, its):
    # Item[0] : Weight
    # Item[1] : Cost
    
    # Item Count 만큼 돌려준다
    for item in its:
        # 역순으로 접근해서 최대값부터 1까지 -1
        for i in range(b_w, 0, -1):
            if item[0] <= i:
                dp[i] = max(dp[i], dp[i - item[0]] + item[1])
    return dp[b_w]
    
if __name__ == '__main__':
    item_count, bag_weight = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(item_count)]
    
    dp = [0 for _ in range(bag_weight + 1)]
    print(knapSack(bag_weight, items))