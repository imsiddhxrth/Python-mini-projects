purchases = [] # List to store the purchase amounts
total_points = 0
points = 0
def tier_label(points):
    if points < 100:
        print('Tier = Bronze')
        return "Bronze"
    elif points >= 500:
        print('Tier = Gold')
        return "Gold"
    else:
        print('Tier = Silver')
        return "Silver" 
def earn_points(price):
    return int(price)*3
for purchase in purchases:
    total_points += earn_points(purchase)
print('LOYALTY SUMMARY')
print(f'Total dollar spent: {sum(purchases)}')
print(f'Total points earned: {total_points}')
print(f'Final tier: {tier_label(total_points)}')