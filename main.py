tshirt  = {101:{"brand":"Allen","size":20,"price":200,"qty":3}, 
   102:{"brand":"Jack","size":22,"price":500,"qty":2},
   103:{"brand":"Levis","size":28,"price":450,"qty":4},
   104:{"brand":"Allen","size":30,"price":700,"qty":1}}

gymWear = {201:{"brand":"Puma","size":40,"price":400,"qty":4}, 
   202:{"brand":"Nike","size":25,"price":350,"qty":1},
   203:{"brand":"Reebok","size":22,"price":350,"qty":8},
   204:{"brand":"Nike","size":32,"price":800,"qty":3}}

sports_wear = {301:{"brand":"Armour","size":20,"price":600,"qty":3}, 
  302:{"brand":"Athleta","size":25,"price":800,"qty":2},
   303:{"brand":"Armour","size":15,"price":900,"qty":5},
   304:{"brand":"Athleta","size":18,"price":1000,"qty":5}}
cart = []
cry=True
def changeCat(i):
  if(i==1):
    print("You Chose the T-shirt's Category")
    return tshirt
  elif(i==2):
    print("You Chose the Gym Wear's Category")
    return gymWear
  elif(i==3):
    print("You Chose the Sports Wear's Category")
    return sports_wear
  else:
    print("Invalid Choice")
    return 0
def BuyUpQty(i):
  pr_amt=int(input("How many would you like to buy"))
  if pr_amt <= type[i]['qty']:
    print(f"The price will be {type[i]['price']*pr_amt}")
    type[i]['qty']=type[i]['qty']-pr_amt
    print(f"There are {type[i]['qty']} items remaining")
    for j in range(pr_amt):
      cart.append(f"Brand:{type[i]['brand']} Size:{type[i]['size']} Price:{type[i]['price']}")
  elif pr_amt > type[i]['qty']:
    print(f"Sorry there are only {type[i]['qty']} of this item remaining")
while cry==True:
  print("1 - T-Shirt")
  print("2 - Gym Wear")
  print("3 - Sports Wear")
  pr_type = int(input("Enter the product type you wish to purchase or enter 4 to see your cart: "))

  if not(pr_type == 4):
    type=changeCat(pr_type)
    print("Here are the products that you can purchase: ")
    for i in type:
      print(f"Product ID: {i} Brand: {type[i]['brand']} Size: {type[i]['size']} Price: {type[i][ 'price']} Quantity: {type[i]['qty']}")
    
    cont=(input("Do you wish to enter your size (y/n): "))
    if cont=="n":
      pr_id=int(input("Enter the product ID: "))
      if pr_id in type:
        print(f"You are trying to purchase a {type[pr_id]['brand']} brand product.The price is {type[pr_id]['price']} ")
        BuyUpQty(pr_id)
      else:
        print("This item doesnt exist")
    else:
      pr_size = int(input("Please enter your size"))
      check = True
      for i in type:
        if pr_size == type[i]['size']:
          check = False
          print(f"The {type[i]['brand']} Is available for {type[i]['price']}")
          if check==False:
            askPurc=input("Would you like to purchase it?")
            if askPurc=="y":
             BuyUpQty(i)
      if check==True:
        print("Sorry there are no items available for your size")
      
    c2=input("You would like to keep buying y/n: ")
    if c2=="y":
      cry=True
    else:
      cry=False
  else:
    print("Your Cart:")
    print(cart)