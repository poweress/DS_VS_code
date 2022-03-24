import numpy as np

def random_predict(number:int=1)->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)# предлогаемое число
        if number == predict_number:
            break# выходим из цикла, если угадали
    return(count)  
def score_game(random_predict)->int:
    """ За какое количество попыток в среднем из 1000 подзодов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f' Ваш алгоритм угадывает число в среднм за : {score} попыток ')
    return (score)
if __name__ == '__main__':
    score_game(random_predict)