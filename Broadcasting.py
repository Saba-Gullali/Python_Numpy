import numpy as np

# without numpy
prices1D= [100,200,300,400,500]
discount_1d = 10

final_prices = []
for price in prices1D:
    final = price - (price * discount_1d/100)
    final_prices.append(final)

print(f"final prices without numpy: {final_prices}")

# using numpy:
prices_1D = np.array([100,200,300,400,500])
discount_1D = 10
final_1D = prices_1D - (prices_1D * discount_1D/100)
print(f"the final prices using numpy : {final_1D}")

# 2d
 # Prices: rows = stores, columns = products
prices_2D = np.array([
    [100, 200, 300],
    [120, 180, 260],
    [90, 210, 330]
])

# Discounts per product (in %)
discounts_2D = np.array([10, 20, 5])  # means 10%, 20%, 5%

final_prices_2D = prices_2D - (prices_2D * discounts_2D/100)

print(final_prices_2D)

# 3D
prices_3D = np.array([
    [
        [100, 200, 300],
        [120, 180, 260],
        [90, 210, 330]
    ],
    [
        [105, 195, 310],
        [115, 175, 250],
        [95, 205, 340]
    ]
])

# Discounts: same shape as prices
discounts_3D = np.array([
    [
        [10, 20, 5],
        [15, 25, 10],
        [5,  15, 8]
    ],
    [
        [12, 18, 6],
        [14, 22, 9],
        [7,  17, 5]
    ]
])

final_prices_3D = prices_3D -(prices_3D * discounts_3D/100)
print(final_prices_3D)























































































































































































































