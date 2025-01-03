def uniquePaths(m, n):
    if m <= n or n <= 0:
        return 0
    dp = [[0] * n] * m

    for i in range(m):
        for j in range(n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m-1][n - 1]


arr = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]


def uniquePaths(array):
    m = len(array)
    n = len(array[0])
    if m <= 0 or n <= 0:
        return 0
    dp = [[0] * n] * m

    for i in range(m):
        for j in range(n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + array[i][j]
    return dp[m-1][n-1]
print(uniquePaths(arr))


def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0]*n1]*n2
    for i in range(n1):
        for j in range(n2):
            if word1[i-1] == word2[j-1]:
                dp[i,j] = dp[i-1][j-1]
            else:
                dp[i,j] = min(min(dp[i-1][j-1], dp[i][j-1]),dp[i-1][j]) + 1

        return dp[n1][n2]



