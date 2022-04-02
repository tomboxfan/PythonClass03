'''
Requirement:

A juice factory produces apple juice and orange juice in 2 containers - cube size and ball size
cube container has a edge length 10cm
ball container has a radius 6 cm

The factory use 2 materials - plastic / metal
So in total, the factory produces 8 kinds of beverage:
1) apple juice - cube container - plastic material
2) apple juice - cube container - metal material
3) apple juice - ball container - plastic material
4) apple juice - ball container - metal material
5) orange juice - cube container - plastic material
6) orange juice - cube container - metal material
7) orange juice - ball container - plastic material
8) orange juice - ball container - metal material

orange juice cost: 0.14 cent / cm^3
apple juice cost: 0.11 cent / cm^3
plastic material cost: 0.08 cent / cm^2
metal material cost: 0.18 cent / cm^2



These 8 kinds of juice are sold in NTUC supermarket and Cold Storage supermarket.
NTUC charges 10% of your juice price, meaning if your juice is sold at $2, you need to pay NTUC 20 cent.
Cold Storage changes 15% of your juice price, meaning if your juice is sold at $2, you need to pay Code Storage 30 cent.

There are in total 16 situations.

Remember: the factory also needs to make profit 30%

The factory manager asks you to help them to calculate the price for the above 16 situations, how much they should sell for each case.
'''

import math


'''
--------------------------------
Step 1) Prepare all the data including:
--------------------------------
1) container
2) juice
3) material
4) supermarket 
'''

container_1 = ['cube', 10]   # cube has a edge length of 10 cm
container_2 = ['sphere', 6]  # sphere has a radius of 6 cm
containers = [container_1, container_2]

juice_1 = ['orange', 0.14] # juice cost: 0.14 cent / cm^3
juice_2 = ['apple', 0.11] # juice cost: 0.11 cent / cm^3
juice = [juice_1, juice_2]

material_1 = ['plasitc', 0.08] # container material cost: 0.08 cent / cm^2
material_2 = ['metal', 0.18] # container material cost: 0.18 cent / cm^2
material = [material_1, material_2]

ntuc = ['NTUC', 0.1] # NTUC charges 10%
cold_storage = ['Cold Storage', 0.15] # Cold Storage changes 15%
supermarkets = [ntuc, cold_storage]

# IMPORTANCE!!! ----------------------------------------------------
# list can help group related information together.
# So that you can use 1 list variable only to access many related information.
# ------------------------------------------------------------------


'''
When data is ready, we can start our actual python code 

--------------------------------
Step 2) Core logic:
--------------------------------

total situation = 2 juice * 2 container * 2 material * 2 supermarkets
                = 16 situations
                
I use nested loop to cover all 16 situations.

for container in containers:
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                # here we have 4 variable: container / current_juice / current_material / supermarket
                # loop body is here



Inside the loop body, what shall we do? 

Step 1) calculate the container's surface & volume
        So we define a function:
        
        def surface_and_volume(container):
            pass

Step 2) Use container's surface and volume / juice / material to calculate the cost of the juice to the factory
        So we define a function:
        
        def calculate_cost(container_data, juice, material):
            pass
            
Step 3) Because the factory needs to make 30% profit, so based on the cost to the factory, we can calcuate the price sold to supermarket.
        So we define a function:

        def sold_price_to_supermarket(cost):
            pass
            
Step 4) Because NTUC and Cold Storage need to make different profit, so same import price from factory has a different selling price to customer.
        So we define a function:

        def sold_price_to_customer(cost, supermarket):
            pass

'''


def surface_and_volume(container):
    '''
    Calculate the surface area and the volume of the container

    :param container: is a list <br>
                      container[0] can be either 'cube' or 'sphere'  <br>
                      container[1] means 'radius' when container[0] is a sphere.  <br>
                      container[1] means 'edge length' when container[0] is a cube.  <br>

    :return: a list which contains 2 values - the surface ared and the volume of the container
    '''
    # The above part is called docstring. -> document string



    result = []

    if container[0] == 'cube':
        result.append(container[1] ** 2 * 6) # calculate surface area of the cube
        result.append(container[1] ** 3) # cube volume
    elif container[0] == 'sphere':
        result.append(4 * math.pi * container[1] ** 2) # sphere surface
        result.append(4/3 * math.pi * container[1] ** 3) # sphere volume
    else:
        print(f"Unknown container type: {container[0]}")

    return result




def calculate_cost(container_data, juice, material):
    '''
    calculate the real cost of the juice to the factory

    :param container_data: is a list <br>
           container_data[0] is the surface area of the container <br>
           container_data[1] is the volume of the container <br>

    :param juice: is a list <br>
           juice[0] is the juice type, it can be either 'apple' or 'orange' <br>
           juice[1] is the juice price <br>

    :param material: is a list <br>
           material[0] is the material type, it can be either 'plastic' or 'metal' <br>
           material[1] is the material price <br>

    :return: the total cost of the juice. Including juice cost + container cost
    '''

    container_cost = container_data[0] * material[1]
    juice_cost = container_data[1] * juice[1]
    total_cost = container_cost + juice_cost
    return total_cost


def sold_price_to_supermarket(cost):
    return cost * 1.3


def sold_price_to_customer(cost, supermarket):
    '''
    calculate how much the supermarket should sell the juice to the customer

    :param cost: price at which supermarket buys.
    :param supermarket: is a list <br>
           supermarkte[0] is the supermarket name.
           supermarkte[1] is the proft rate of the supermarket

    :return: the selling price to the customer
    '''
    return cost * (1 + supermarket[1])



for container in containers:
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                # here we have 4 variable: container / current_juice / current_material / supermarket

                print(f'For juice type: container: {container}, juice: {current_juice}, material: {current_material}, supermarket: {supermarket}')
                container_info = surface_and_volume(container)
                print(f"Surface area: {container_info[0]:.2f} cm^2")
                print(f"Volume: {container_info[1]:.2f} cm^3")

                original_cost = calculate_cost(container_info,current_juice, current_material)
                print(f"Cost for the factory to produce the juice: ${original_cost/100:.2f}")

                selling_price_to_supermarket = sold_price_to_supermarket(original_cost)
                print(f"selling price to supermarket: ${selling_price_to_supermarket/100:.2f}")

                selling_price_to_customer = sold_price_to_customer(selling_price_to_supermarket, supermarket)
                print(f"selling price to customer: ${selling_price_to_customer/100:.2f}")

                print("-" * 100)






