revoked = {'1', '2', '3', '4', '5'}
approved = []
denied = []
while True:
    visitors_name = input('Please enter your name: ')
    if visitors_name.lower() == 'done':
        break
    badge_num = input('Please enter your badge number: ')
    if badge_num in revoked:
        denied.append(visitors_name)
        print('ACCESS DENIED')
    else:
        approved.append(visitors_name)
        print('ACCESS GRANTED')

print("Access Summary:")
approved = sorted(approved)
denied = sorted(denied)
print(f'Total number of approved visitors: {len(approved)}')
print(f'Total number of denied visitors: {len(denied)}')