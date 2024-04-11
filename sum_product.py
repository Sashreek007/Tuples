"""""Write a function that calculates the sum and product of all elements in a tuple of numbers."""

input_tuple = (1, 2, 3, 4)

def sum_product(input_tuple):
    sum_tuple=0
    product_tuple=1
    for i in input_tuple:
        sum_tuple += i
    for i in input_tuple:
        product_tuple *= i
    print(sum_tuple,product_tuple)

sum_product(input_tuple)
