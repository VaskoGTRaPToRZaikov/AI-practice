restaurant_menu = {}

while True:
    info = input()

    if info == "close kitchen":
        output_category = input()
        break
    menu_info = info.split("-")
    menu_category, dish, price = menu_info[0], menu_info[1], float(menu_info[2])

    if menu_category not in restaurant_menu:
        restaurant_menu[menu_category] = {}

    restaurant_menu[menu_category][dish] = price

if output_category in restaurant_menu:
    dishes = restaurant_menu[output_category]
    sorted_dishes = sorted(dishes.items(), key=lambda x: x[1])
    for some_dish, some_price in sorted_dishes:
        print(f"{some_dish}-${some_price:.2f}")
else:
    print("Category not found!")
