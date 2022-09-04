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

    print('Division')  #Always returns float
    print(9/3)
    print(5.0/3)

    print('Integer Division')  #Rounds down to an integer
    print(f'9//3 = {9//3}')  #Returns Integer
    print(f'5.0//3 = {5.0//3}')  #Returns float
    print(f'3//2 = {3//2}')
    print(f'-3//2 = {-3//2}')  #Rounds down to an integer

    print('Exponents')
    print(2 ** 4)  #Returns integer
    print(3 ** 0.5)  #Returns float
    print(2 ** -2)  #Returns float

    print('The modulus operator')
    print(20 % 7)
    print(5 % -3)  #r = x - (y * (x // y))


def five_point_five():
    print('The round() function')  #to the nearest integer
    print(f'round(2.7) = {round(2.7)}')
    print(f'round(2.5) = {round(2.5)}')
    print(f'round(3.5) = {round(3.5)}')  #Rounding ties to even
    print(f'round(3.14159, 3) = {round(3.14159, 3)}')
    # Expected value: 2.68 
    print(f'round(2.675, 2) = {round(2.675, 2)}')  # Floating point error

    print('The pow() Function')
    print(f'pow(2, 3) = {pow(2, 3)}')
    #  print(f'{}')

#five_point_one()
#five_point_two()
five_point_five()