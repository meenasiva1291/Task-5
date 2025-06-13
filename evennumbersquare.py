list_ = [15,20,198,177,23,24,1009,1998]
even_square = list(map(lambda a:a ** 2, filter(lambda a:a % 2 == 0, list_)))
print(even_square)

