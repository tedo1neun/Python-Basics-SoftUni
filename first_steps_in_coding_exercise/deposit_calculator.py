deposit_amount = float(input())
term = int(input())
annual_interest_rate = float(input())
total_amount = deposit_amount + term * ((deposit_amount * annual_interest_rate/100)/12)
print(total_amount)