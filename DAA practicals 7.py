def coin_change(coins, amount):
    # Initialize DP array with a large value
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Fill the DP table
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed, return -1
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
coins = [1, 2, 5]
amount = 11

result = coin_change(coins, amount)

if result != -1:
    print(f"Minimum coins required: {result}")
else:
    print("Amount cannot be formed with the given coins.")
