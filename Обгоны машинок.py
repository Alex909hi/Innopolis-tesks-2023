'''
Задача С: Обгоны
В гонках участвуют n машин черного или белого цвета. Петя знает, в каком порядке стартовали
машины, а также он знает, что во время гонки произошло m обгонов (в результате каждого обгона
меняется порядок двух соседних машин). Пете стало интересно, какое максимальное число черных
машин могло финишировать подряд друг за другом? Помогите ему узнать это число.

Выведите одно число — максимальное число черных машин, которое могло финишировать подряд друг за другом
'''
list_chars = []
character = 'b'
result = 0

def find_indexes(order, char):
    return [i for i, letter in enumerate(order) if letter == char]

n = int(input("Введите число машин: \n"))
m = int(input("Введите число обгонов: \n"))

car = True
while car:
    order_cars = input("Напишите порядок машин и их цвет(белый - w или черный - b): \n")
    if len(order_cars) <= n:

        list_chars = find_indexes(order_cars, character)
        if len(list_chars) == 1:
            print(f"result: 1")
            break

        for i in range(len(list_chars)):
            count = 1
            
            if i == len(list_chars) - 1:
                continue
            else:
                for y in range(len(list_chars)):
                    if i == y:
                        continue
                    else:
                        diffirence = abs(list_chars[i] - list_chars[y]) - 1
                        if diffirence <= m:
                            count += 1
                            m = m - diffirence
                            if count > result:
                                result = count
                        else:
                            if count > result:
                                result = count
        print(f"result: {result}")
        car = False
    else:
        print("Слишком много машин!!! Попробуй ещё раз!!!")