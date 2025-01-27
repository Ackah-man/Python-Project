'''Name: Oswin Heman-Ackah
index Number : 10022300148'''



print("********WELCOME********")
Attendant_name = 'Joe'
passs = 12345
trails = 3
tl = [] #tl -- transaction list


#--------------------------------------
#code begins from here

for t in range(trails):
    name = input("Enter Attendant Name \n")
    passs = int(input("Enter Password \n"))
    if Attendant_name == "Joe" and passs == 12345 : 
        print("Welcome Joe")
        break
    else:
        print("Your entered incorrect details(*_*)...Try again.")       
    retro = trails - t - 1
    if retro == 0:
         print('You have exhausted the number of trials available. The program is quitting')
         print('-------quitting-------')
         break
    else:
        continue
print("*****MENU*****")
item_inventory = {'Bread' :10, 'Water': 15, 'Pizza': 25, 'Salad':20}
print("L - List all items\nG - Generate Bill\nV - View all transactions\nP - Pay an attendant\nE - Exit Program")
choice = input("Please Select and option:")



if choice == "L":
    print("********List All Items********")
    print('Bread - 10\nWater - 15\nPizza - 25\nSalad - 20') 

#---------------------------------------------------------
elif choice == "G":
    print("********Generate Bills********")
    item_list_2 = {}
    while True:
        #item name is the key and item num is the value
        item_name = input('Enter item name:')
        item_num = int(input('Enter quantity of item:'))
        item_list_2[item_name] = item_num
        if item_name == "None" and item_num == 0:
            print(item_list_2)
        redo = input('Do you wish to perform thr task again? Y/N')
        if redo != "Y":
              break

#---------------------------------------------------------
    amount_payed=int(input("Enter Amount Paid:"))
    #code for the total
    total = 0
    shop_busket = {}
    for keys, values in item_inventory.items():
        if keys in item_list_2:
            res = values * item_list_2[keys]
            shop_busket[keys] = res
            total += res
            change = amount_payed - total
            #storing the total in a list
            tl.append(total)
            
    
    print('*****Bills*****')
    print(f'Amount Payed : {amount_payed}')
    print(f'Total : {total}')
    print(f'Change: {change}')
     
#---------------------------------------------------- 
elif choice == "V":
    tl_sum = 0
    print("********View All Transactions********")
    for i in tl:
        print(i)
        tl_sum = tl_sum + i
        print(tl_sum)


#-----------------------------------------------------
elif choice == "P":
    print("********Pay Attendant********")
    pay_per_hour = 100
    overtime_bonus = 50
    hours = int(input('Enter the number of hours worked:  '))
    if hours == 8 :
        pay_due = hours * pay_per_hour
        print(f'Pay Due: {pay_due}')
    elif hours > 8:
        add_hours = hours - 8
        print(f'You worked and additional {add_hours} hours')
        new_hours = add_hours * overtime_bonus
        overtime_pay_due = 800 + new_hours
        print(f'Pay Due: {overtime_pay_due}')

#----------------------------------------------------------
elif choice == "E":
    print('----Exitiing Program.Thank you----')

    




            
    
