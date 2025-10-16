# Mamy dana sume pieniedzy ktora nalezy osiagnac z nominalow znajdujacych sie w tablicy
# Przyjmujemy ze ilosc sztuk kazdego z nominalow jest nieograniczona
# Cel jest taki, by ta sume osiagnac uzywajac jak najmniejszej ilosci sztuk poszczegolnych nominalow

def coin_change_problem(amount, coins):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != (amount + 1) else -1

