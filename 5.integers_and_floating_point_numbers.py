def five_point_one():
    print('Integers writting')
    print(1000000)
    print(1_000_000)

    print('Float writting')
    print(1000000.0)
    print(1_000_000.0)
    print(1e6)
    print(2e308)

def five_point_two():
    print('Addition')
    print(1 + 2)  #Returns Integer
    print(1.0 + 2)  #Returns float

    print('Division')
    print(9/3)
    print(5.0/3)

    print('Integer Division')
    print(9//3)  #Returns Integer
    print(5.0//3)  #Returns float
    print(3//2)
    print(-3//2)  #Rounds down to an integer

    print('Exponents')
    print(2 ** 4)  #Returns integer
    print(3 ** 0.5)  #Returns float
    print(2 ** -2)  #Returns float

    print('The modulus operator')
    print(20 % 7)
    print(5 % -3)  #r = x - (y * (x // y))


#five_point_one()
five_point_two()