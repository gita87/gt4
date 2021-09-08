'''
def greet_with_name(name, location) :
    print(f"hello, {name}?")
    print(f"Are You from {location}?")

greet_with_name("Gita", "Bali")
'''
#Write your code below this line 👇

import math
'''
def paint_calc (height, width, cover) :
    height = test_h
    widht = test_w
    cover = coverage
    can_needed = math.ceil(height * widht / cover)
    print(f"All paint can you need is {can_needed}")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''
def hitung_rmse (data_asli, data_prediksi) :
    summation = 0
    n = len(data_asli)
    for i in range(0, n):
        difference = data_asli[i] - data_prediksi[i]
        squared_difference = difference ** 2
        summation = summation + squared_difference
    mse = summation / n
    rmse = mse ** 0.5
    print('mse adalah : ', mse)
    print('rmse adalah : ', rmse)


data_asli = [2, 3, 4, 5, 6]
data_prediksi = [4, 3, 5, 5, 3]

mse, rmse = hitung_rmse(data_asli, data_prediksi)

