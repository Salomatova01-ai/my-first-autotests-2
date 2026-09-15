def get_day_name(day: int) -> str:

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
    numbers = list(range(1,10))
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
             max_value = number
    return max_value

find_max_number()


# array = [0, 1, 2, 3];
# list(range(0,9))
# print(list(range(0,10)))
# for arrayItem in array:
#     result = f"str{arrayItem}";
#     print(result)




def stop_at_five():
    numbers = list(range(1, 8))
    for number in numbers:
        print(number)

        if number == 5:
            break

def create_words():
    words = [f"str{i}" for i in range(10)]
    print(words)


import random
import time

LOAD_THRESHOLD = 85
ITERATIONS = 10
SLEEP_SECONDS = 0.2


def simulate_load_monitoring() -> None:
    iteration = 0

    while iteration < ITERATIONS:
        load = random.randint(0, 100)
        print(f"Итерация {iteration + 1}: нагрузка {load}%")

        if load > LOAD_THRESHOLD:
            print("⚠️ ВНИМАНИЕ: Высокая нагрузка!")

        time.sleep(SLEEP_SECONDS)
        iteration += 1