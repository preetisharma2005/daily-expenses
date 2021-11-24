items = 0
total_amount = 0
all_items = {}

x = input('Do you want to enter item? y/Quit ')
while x == 'y':
    item_list = input('Enter item name: ')
    if item_list == 'q':
        break
    else:
        price = input('Enter price of item: ')
        price = int(price)
        items += 1
        print(item_list, ':', price)
        total_amount = total_amount + price
        all_items[item_list] = price

print('\n******************************** \n')

for i in all_items:
    print(f'{i} : {str(all_items.get(i))}')

print('\n******************************** \n')

print('You bought', items, 'items and spent', total_amount, '.')