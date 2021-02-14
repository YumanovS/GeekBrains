total_sum = 0
sum_number_ranks = 0
sum_number_mod7 = 0

for number in range(1,1001,2):
    temp_number = t_number = number**3
    total_sum += temp_number
    while temp_number != 0:
        sum_number_ranks += (temp_number % 10)
        temp_number = temp_number // 10
    if sum_number_ranks % 7 == 0:
        print(f"число: {t_number} sum: {sum_number_ranks} (cube of {number})")
        sum_number_mod7 += t_number
    sum_number_ranks = 0
print("total sum of cubes: ", total_sum)
print("total sum div 7: ", sum_number_mod7)