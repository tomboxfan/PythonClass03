'''

Step 1) Copy 0032 to 0045

Step 2) You don't need to loop the welcome msg / price list

Step 3) You need to loop the buying process
        An extra option 'EXIT' is required to let customer to exit the 'buying product' while loop

Step 4) You don't need to loop the check member / payment process

The program is composed of
a) welcome msg
b) price list
c) buy product
d) check member
e) payment

The loop should happen only at c)

Notes:
1) another variable is required to accumulate the total price of all products


'''


welcome_msg = '''
**********************************
   Welcome to NTUC Supermarket
**********************************
'''

print(welcome_msg)


product_price = '''
-----------------------
beef - $20 / kg
pork - $16 / kg
tomato - $5 / kg
apple -  $5 for 5 apples; $1.6 each
orange - $5 for 3 oranges; $2 each
-----------------------
'''

print(product_price)



total_price_for_all_products = 0



while True:


    product_name = input("What product do you want to buy (beef / pork / tomato / apple / orange / exit): ")

    total_price = 0

    if product_name == 'beef' or product_name == 'pork' or product_name == 'tomato':

        total_weight = float(input("Total weight(kg): "))

        if product_name == 'beef':
            unit_price = 20 # $20 / kg
        elif product_name == 'pork':
            unit_price = 16
        else:
            unit_price = 5

        total_price = unit_price * total_weight
        print(f'{product_name} : ${unit_price} * {total_weight} = ${total_price}')


    elif product_name == 'apple' or product_name == 'orange':

        total_count = int(input("Total quantity: "))

        if product_name == 'apple':
            group_count = total_count // 5
            single_count = total_count % 5
            group_price = 5 # $5 for 5 apples
            single_price = 1.6 # $1.6 each

        else:
            group_count = total_count // 3
            single_count = total_count % 3
            group_price = 5
            single_price = 2

        group_price_total = group_price * group_count
        single_price_total = single_price * single_count
        total_price = group_price_total + single_price_total
        print(f"{product_name} : ${total_price}")

    elif product_name == 'exit':
        break

    else:
        print(f"Unrecognized product: {product_name}")

    total_price_for_all_products += total_price











# membership ------------------------------------
member_str = input("Are you a member? ")

'''
--Common mistake---WRONG!----------------------
if member_str == 'Y' or 'y' or 'Yes' or 'yes'
-----------------------------------------------
Because 'or' separate valid boolean expression.
'''

if member_str == 'Y' or member_str == 'y' or member_str == 'Yes' or member_str == 'yes':
    total_price_for_all_products *= 0.9
    print(f"After discount, total price: ${total_price_for_all_products}")

# payment ---------------------------------------------
payment = input("Will you pay using Visa / Mastercard / NETS / Cash? ")

if payment == 'Visa' or payment == 'Mastercard':
    signature = input("Plase sign your name: ")
    print(f"Signature {signature} is well received")
    print(f'${total_price_for_all_products} has been charged to your {payment} card')
elif payment == 'NETS':
    password = input("Please input your NETS card password: ")
    print(f"${total_price_for_all_products} has been charged to your NETS card.")
elif payment == 'Cash':

    total_paid = float(input("How much will you pay? "))
    if total_paid > total_price_for_all_products:
        print(f"Here comes your change: ${total_paid - total_price_for_all_products:.2f}")
    elif total_paid < total_price_for_all_products:
        print(f"you are still short of ${total_price_for_all_products - total_paid}. I am sorry, I cannot give you the product.")
    else:
        print("You've paid the exact amount")

else:
    print(f"Unsupported payment.")


bye_msg = '''
***********************
  See you again! 
***********************
'''

print(bye_msg)