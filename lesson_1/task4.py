def bank(sum_deposit, years, interest):
    for i in range(years):
        sum_deposit = sum_deposit + (sum_deposit * interest / 100)
    return sum_deposit
