# Napisz program, ktory ma podana tablice liczb i pewna wartosc.
# Program ma sprawdzic czy mozna zbudowac podana wartosc z sumy liczb w tablicy.
# Program musi znalezc jak najmniej skladnikow, ktore daja ta wartosc.
# Kazdego skladnika mozna uzyc tylko raz.
def orchard(T, m):
    flaga = False
    i = 0
    while (i * m) <= sum(T):
        target_robocze = (sum(T) % m) + (i * m)
        if subset_sum_problem(T, target_robocze) != -1:
            return subset_sum_problem(T, target_robocze)
    return len(T)


def subset_sum_problem(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  # Suma 0 jest zawsze osiągalna

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target] if dp[n][target] != (target + 1) else -1




