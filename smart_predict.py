"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def smart_predict(number: int = 1) -> int:
    """Угадываем число через сужение диапазона

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left, right = 1, 101 # диапазон загаданного числа
    predict_number = (left + right) // 2 # середина заданного диапазона

    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        
        elif number > predict_number:
            left = predict_number + 1 # левая граница становится предполагаемым числом
            predict_number = np.random.randint(predict_number + 1, right) # угадываем число в полученном диапазоне
            
        else:
            right = predict_number # правая граница становится предполагаемым числом
            predict_number = np.random.randint(left, predict_number) # угадываем число в полученном диапазоне    
                  
    return count


def score_game(smart_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        smart_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(smart_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score