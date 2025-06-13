#| Задание!| 1.  Номер самого дорого заказа за июль.
import json
with open('../Work_Skillfactory/orders_july_2023.json', 'r') as my_file:
    orders_july_2023 = json.load(my_file)
#print(orders_july_2023)
max_price = 0
max_order = ''
quantity_orders_max_price=0
num_orders_max_price=[]
for order_num, orders_data in orders_july_2023.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
#print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
#----------------------------------------------------------------------------------------------------------------------#
for order_num, orders_data in orders_july_2023.items():
    price = orders_data['price']
    if price==max_price:
        quantity_orders_max_price+=1
        num_orders_max_price.append(order_num)
print('#| Задание!| 1.  Номер самого дорого заказа за июль.')
print(f'Максимально возможная цена: {max_price}, кол-во заказов с максимальной ценой: {quantity_orders_max_price}, номера заказов с максимальной ценой {num_orders_max_price}')

#| Задание!| 2. Номер заказа с самым большим количеством товаров.
with open('../Work_Skillfactory/orders_july_2023.json', 'r') as my_file:
    orders_july_2023 = json.load(my_file)
#print(orders_july_2023)
max_quantity = 0
max_order = ''
quantity_max_quantity=0
list_quantity_max_order=[]
for order_num, orders_data in orders_july_2023.items():
    quantity=orders_data['quantity']
    if quantity>max_quantity:
        max_quantity=quantity
        max_order=order_num
#print(f'номер заказа с самым большим количеством товаров в нем: {max_order}, количество товаров в заказе: {max_quantity}')
#----------------------------------------------------------------------------------------------------------------------#
for order_num, orders_data in orders_july_2023.items():
    quantity = orders_data['quantity']
    if quantity==max_quantity:
        quantity_max_quantity += 1
        list_quantity_max_order.append(order_num)
print()
print('#| Задание!| 2. Номер заказа с самым большим количеством товаров.')
print(f'Cамое большое кол-во товаров в 1 заказе: {max_quantity}, кол-во заказов с максимальным кол-вом товаров: {quantity_max_quantity}, номера заказов с максимальным кол-вом товаров: {list_quantity_max_order}')

#| Задание!| 3. В какой день в июле было сделано больше всего заказов?
date_max_order=''
date_order={}
for order_num, orders_data in orders_july_2023.items():
    date=orders_data['date']
    if date in date_order:
        date_order[date] +=1
    else:
        date_order[date]=1
date_max_count_order=max(date_order, key=date_order.get)
print()
print('#| Задание!| 3. В какой день в июле было сделано больше всего заказов?')
print(date_order)
print(f'Дата с максимальным кол-вом заказов: {date_max_count_order}, кол-во заказов: {date_order[date_max_count_order]}')
# количество звказов в этот день 33 *вроде, но и в другие дни тоже, я так и не понял как с этим быть((

#| Задание!| 4. Какой пользователь сделал самое большое количество заказов за июль?
count_order_users={}
for order_num, orders_data in orders_july_2023.items():
    user_id=orders_data['user_id']
    if user_id in count_order_users:
        count_order_users[user_id] +=1
    else:
        count_order_users[user_id]=1
count_max_order_users =max(count_order_users, key=count_order_users.get)
print()
print('#| Задание!| 4. Какой пользователь сделал самое большое количество заказов за июль?')
print(count_order_users)
print(f'Пользовотель с максимальным количеством заказов: {count_max_order_users}, кол-во заказов: {count_order_users[count_max_order_users]}')

#| Задание!| 5. У какого пользователя самая большая суммарная стоимость заказов за июль?
sum_price_user={}
for order_num, orders_data in orders_july_2023.items():
    user_id=orders_data['user_id']
    price=orders_data['price']
    if user_id in sum_price_user:
        sum_price_user[user_id] += price
    else:
        sum_price_user[user_id] = price

max_sum_price_user= max(sum_price_user, key=sum_price_user.get)
print()
print('#| Задание!| 5. У какого пользователя самая большая суммарная стоимость заказов за июль?')
print(sum_price_user)
print(f'Пользователь с максимальной суммой заказа: {max_sum_price_user}, сумма заказов: {sum_price_user[max_sum_price_user]}')

#| Задание!| 6. Какая средняя стоимость заказа была в июле?
list_price={}
for order_num, orders_data in orders_july_2023.items():
    user_id=orders_data['user_id']
    price=orders_data['price']
    list_price[user_id] = price
average_list_price=sum(list_price)/len(list_price)
print()
print('#| Задание!| 6. Какая средняя стоимость заказа была в июле?')
print(list_price)
print(f'Cредняя стоимость заказа в июле: {int(average_list_price)}')

#| Задание!| 7. Какая средняя стоимость товаров в июле?
list_average_sum_products_in_order=[]
for order_num, orders_data in orders_july_2023.items():
    price=orders_data['price']
    quantity=orders_data['quantity']
    average_sum_product_in_order =int(price/quantity)
    list_average_sum_products_in_order.append(average_sum_product_in_order)
print()
print('#| Задание!| 7. Какая средняя стоимость товаров в июле?')
print(list_average_sum_products_in_order)
average_sum_product_in_order_user=int(sum(list_average_sum_products_in_order)/len(list_average_sum_products_in_order))
print(f'Средняя стоимость товарра в июле: {average_sum_product_in_order_user}')