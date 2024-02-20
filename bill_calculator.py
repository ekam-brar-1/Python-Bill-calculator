order_list = []

no_of_cakes = int(input("Enter quantity of cakes: "))
price = 0

total_price=0
if no_of_cakes>=0:
    while no_of_cakes != 0:
        order_list.append(no_of_cakes)
        print("Choose flavor: \n1.Chocolate \n2.Vanilla \n3.Mango \n4.Hot Chocolate\n")
        flavor= int(input("Enter flavor :"))
        if flavor<5 and flavor>0:
            quantity = float(input("Enter wieght of cake in KG: "))
            match flavor:
                case 1: price = 30
                case 2: price = 50
                case 3: price = 35 
                case 4: price = 56
            total_price += price*no_of_cakes*quantity
            no_of_cakes = int(input("Enter quantity of cakes: "))
        else:
            print("Choose correct flavor")
else: 
    print("You have selected wrong quantity")
print(f'\nYou have order {len(order_list)} cakes \nTotal is ${total_price:.2f}')

