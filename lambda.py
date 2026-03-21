#lambda function are anonymous fns. They execute within a single line. It auto returns. Takes in one argument
# square brackets show the type of data is a list
num = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, num))
print(even_nums)