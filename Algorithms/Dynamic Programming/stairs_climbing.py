import sys


def get_num_of_ways_to_climb(n):
    dp = [1 for i in range(n + 1)]
    for i in range(len(dp)):
        if i < 2:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        print(get_num_of_ways_to_climb(int(line)))
