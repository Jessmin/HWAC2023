#买3件物品，花最多钱,100
# [19,23,4,...]
import numpy as np
def maximize_spending(prices, budget):
    n = len(prices)

    # 创建一个三维数组 dp，dp[i][j][k] 表示前 i 个物品中选择了 j 个物品，总花费为 k 时的最大花费
    dp = [[[0 for _ in range(budget + 1)] for _ in range(4)] for _ in range(n + 1)]

    # 动态规划主体
    for i in range(1, n + 1):#items
        for j in range(1, 4):#3
            for k in range(1, budget + 1):#1-50
                price_item_idx = i-1
                # 不购买第 i 个物品
                dp[i][j][k] = dp[price_item_idx][j][k]
                # 购买第 i 个物品
                if k >= prices[i - 1]:
                    print(f"k={k},{dp[price_item_idx][j - 1][k - prices[price_item_idx]]}")
                    #dp[price_item_idx][j - 1][k - prices[price_item_idx]]这个存的是之前的花费，不够的话就说明之前没买，这个值就是0
                    #如果k-prices[idx-1]有值，说明买了别的，再求最大值
                    dp[i][j][k] = max(dp[i][j][k], dp[price_item_idx][j - 1][k - prices[price_item_idx]] + prices[price_item_idx])

    # 从 dp[n][3][budget] 中获取最大花费 取最后的即可
    max_spending = dp[n][3][budget]

    if max_spending > 0:
        print(f"最大花费为 {max_spending}")
    else:
        print("无法购买三个物品使得花费不超过预算。")
    

# 示例
prices = [23,26,36,27]
budget = 78
maximize_spending(prices, budget)
