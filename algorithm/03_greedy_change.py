import sys

input = sys.stdin.readline

n = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin # 몫
  n %= coin # 나머지

print(count)

# 화폐의 종류가 K개라고 할 때 시간 복잡도는 O(K)
# => 이 알고리즘의 시간 복잡도는 동전의 총 종류에만 영향을 받고, 거슬러 줘야 하는 금액의 크기와는 무관하다

# 그리디 알고리즘의 정당성
# 대부분의 문제는 그리디 알고리즘을 이용했을 때 '최적의 해'를 찾을 수 없을 가능성이 다분하다.
# 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.
# 대부분의 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.
# 어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해보자.
# 만약 오랜 시간을 고민해도 그리디 알고리즘으로 해결 방법을 찾을 수 없다면, 그때는 다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지를 재차 고민해보는 것도 한 방법이다.
# 실제로 거스름돈 문제에서 동전(화폐)의 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우에는 그리디 알고리즘으로는 해결할 수 없다.
# 화폐의 단위가 무작위로 주어진 문제는 다이나믹 프로그래밍으로 해결할 수 있다.