
# 自顶向下递归
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float("-inf")
    # for i in range(1, n):
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


# 带备忘录的自顶向下
def memoized_cut_rod(p, n):
    memo = [float("-inf") for i in range(n+1)]
    return memoized_cut_rod_aux(p, n, memo)

def memoized_cut_rod_aux(p, n, memo):
    if memo[n] >= 0:
        return memo[n]
    if n == 0:
        q = 0
    # elif q == float("-inf"):
    else:
        q = float("-inf")
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, memo))
    memo[n] = q
    return q

def bottom_up_cut_rod(p, n):
    memo = [float("-inf") for i in range(n + 1)]
    memo[0] = 0
    for j in range(1, n+1):
        q = float("-inf")
        for i in range(1, j + 1):
            q = max(q, p[i] +  memo[j - i])
        memo[j] = q
    return memo[n]


def extended_bottom_up_cut_rod(p, n):
    # memo, s = [float("-inf") for i in range(n + 1)], [float("-inf") for i in range(n + 1)]
    memo, s = [None for i in range(n + 1)], [None for i in range(n + 1)]
    memo[0] = 0
    for j in range(1, n + 1):
        q = float("-inf")
        for i in range(1,j + 1):
            if q < p[i] + memo[j - i]:
                q= p[i] + memo[j - i]
                s[j] = i
            memo[j] = q
    return memo, s

def print_cut_rod_solution(p, n):
    memo, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n], end = " ")
        n -= s[n]
    print()

# n = 4
# memo = [float("-inf") for i in range(4)]
# print(memo)

prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(cut_rod(prices, 4))
print(memoized_cut_rod(prices, 4))
print(bottom_up_cut_rod(prices, 4))
# print(extended_bottom_up_cut_rod(prices, 4))
print(print_cut_rod_solution(prices, 4))