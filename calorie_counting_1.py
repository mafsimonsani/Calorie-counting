# CCC '06 J1 - Canadian Calorie Counting

burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

# Calculate and display the Calorie total
# Burger calorie
if burger_choice == 1:
    calorie_burger = 461
elif burger_choice == 2:
    calorie_burger = 431
elif burger_choice == 3:
    calorie_burger = 420
else:
    calorie_burger = 0
    
# Side calorie
if side_choice == 1:
    side_calorie = 100
elif side_choice == 2:
    side_calorie = 57
elif side_choice == 3:
    side_calorie = 70
else:
    side_calorie = 0
    
# Drink calorie
if drink_choice == 1:
    drink_calorie = 130
elif drink_choice == 2:
    drink_calorie = 160
elif drink_choice == 3:
    drink_calorie = 118
else:
    drink_calorie = 0
    
# Dessert calorie
if dessert_choice == 1:
    dessert_calorie = 167
elif dessert_choice == 2:
    dessert_calorie = 266
elif dessert_choice == 3:
    dessert_calorie = 75
else:
    dessert_calorie = 0

print(f'Your total Calorie count is \
{calorie_burger + side_calorie + drink_calorie + dessert_calorie}')
    