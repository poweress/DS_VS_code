"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1 # Объявим счетчик (будим считать кол-во попыток)
    min, max = 1, 101 # Определим минимум и максимум
    number_predict = int(max / 2) # Угадываемое число - максимальное значение делим по полам
    
    # Во вложенных циклах  будем сужать диапазон минимального и максимально значения
    while number != number_predict:        
        count += 1  # Увеличиваем счетчик попыток на 1                      
        if number > number_predict: #  Если истина, определим минимум
            min = number_predict # Запишим минимальное значение 
            number_predict = int((max + min) / 2) # Половиним угадываемое число на два
        elif number < number_predict: #  Если истина, определим максимум
            max  = number_predict # Запишем максимальное значение
            number_predict = int((max + min) / 2) #  И снова половиним угадываемое число
            #  Повторим цикл еще раз            
            while number != number_predict: 
                count += 1  # Увеличиваем счетчик попыток на 1   
                if number > number_predict:
                    min = number_predict
                    number_predict = int((max + min) / 2)                    
                elif number <number_predict:
                    max = number_predict
                    number_predict = int((max + min) / 2)                    
                    # И еще раз повторим
                    while number != number_predict:
                        count += 1  # Увеличиваем счетчик попыток на 1
                        if number > number_predict:
                            min = number_predict
                            number_predict = int((max + min) / 2)                            
                        elif number < number_predict:
                            max = number_predict
                            number_predict = int((max + min) / 2)                            
                            # И здесь повторим
                            while number != number_predict:
                                count += 1  # Увеличиваем счетчик попыток на 1
                                if number > number_predict:
                                    min = number_predict
                                    number_predict = int((max + min) / 2)                                                                        
                                elif number <number_predict:
                                    max = number_predict
                                    number_predict = int((max + min) / 2)                                    
                                    #  И здесь 
                                    while number != number_predict:
                                        count += 1  # Увеличиваем счетчик попыток на 1
                                        if number > number_predict:
                                            min = number_predict
                                            number_predict = int((max + min) / 2)                                                                                
                                        elif number <number_predict:
                                            max = number_predict
                                            number_predict = int((max + min) / 2)                                            
                                            #  аналогично как и выше 
                                            while number != number_predict:
                                                count += 1  # Увеличиваем счетчик попыток на 1
                                                if number > number_predict:
                                                    min = number_predict
                                                    number_predict = int((max + min) / 2)                                                                                        
                                                elif number < number_predict:
                                                    max = number_predict
                                                    number_predict = int((max + min) / 2)
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    #  При каждой итэрации будем добовлять загаданное число в список count_ls
    for number in random_array:
        count_ls.append(random_predict(number)) 

    score = int(np.mean(count_ls)) # Запишем среднее значение
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
