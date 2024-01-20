"""guess the number. Computer makes and guesses numbers itself"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Guess  number randomly

    Args:
        number (int, optional): Number made in wish. Defaults to 1.

    Returns:
        int: count of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        if number == predict_number:
            break # exit from cycle if you guessed
    return(count)

# print(f'Count of attempts: {random_predict()}')


def score_game(random_predict) -> int:
    """How many attempts of 1000 will it take to guess using our algorithm?

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average count of attempts
    """
    count_ls = [] # list for keeping attempts
    np.random.seed(1) # fix seed for reproduce
    random_array = np.random.randint(1, 101, size=(1000)) # estimated list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # find average of count of attempts
    
    print(f'Your algorithm guesses number in average for: {score} attempts')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)