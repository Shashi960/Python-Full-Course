def Cart(orders):
    cart=[]
    cart.append(orders)
    print("Your Order is ready")
    print(f'Your Total Items:{len(cart[0])}\n')
    for item in cart:
        print(item,end=' ')
