#calculate your daily expenses.

items = 0
total_amount = 0
x = input('Do you want to enter item? y/Quit ')
while x == 'y':
    item_list = input('Enter item name: ')
    if item_list == 'q':
        break
    else:
        prize = input('Enter prize of item: ')
        prize = int(prize)
        items += 1
        print(item_list, ':', prize)
        total_amount = total_amount + prize

print('You bought', items, 'items and spend', total_amount, '.')
