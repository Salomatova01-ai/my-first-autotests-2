def get_day_name(day: int, string: str) -> str:

    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Неверный день недели "



def find_max_number():
    numbers = [100, 98, 20, 111]
    max_value = numbers[0]
    for number in numbers:
        if number < max_value:
             max_value = number
    return max_value

find_max_number()

array = [0, 1, 2, 3];
list(range(0,9))
print(list(range(0,10)))
for arrayItem in array:
    result = f"str{arrayItem}";
    print(result)
    

# words = [f"str{i}" for i in range(10)];
# print(array, words)

# [0, 1, 2 ]
# [1, 9 ,20]