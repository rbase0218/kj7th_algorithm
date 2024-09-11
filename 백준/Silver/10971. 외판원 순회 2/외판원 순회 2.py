import sys

# 도시 수를 입력 받는 메서드
city_count = int(input())
# 도시의 이동 cost를 가지고 있는 행렬
city_matrix = [list(map(int, input().split())) for _ in range(city_count)]
# 도시 Visit 여부를 파악한다.
visit_city = [False] * city_count
cost = sys.maxsize

def dfs(start_index, curr_index, walk_all_cost):
    global cost
    
    if walk_all_cost > cost:
        return
    
    # 도착한 장소가 시작 지점이면서, 방문하지 않은 도시가 없을 경우
    if start_index == curr_index and False not in visit_city:
        if walk_all_cost < cost:
            cost = walk_all_cost
        return
    
    for i in range(city_count):
        if city_matrix[curr_index][i] != 0 and visit_city[i] == False:
            visit_city[i] = True
            dfs(start_index, i, walk_all_cost + city_matrix[curr_index][i])
            visit_city[i] = False
            
dfs(0, 0, 0)
print(cost)