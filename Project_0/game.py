import numpy as np 
number = np.random.randint(1, 101) # Make a wish number
count = 0

while True:
    count += 1
    predict_number = int(input("Make a wish number from 1 to 100: "))
    
    if predict_number > number:
        print("Number must be less")
        
    elif predict_number < number:
        print("Number must be more")
    
    else:
        print(f"You win! The number is {number} for {count} attempts")
        break # Game over, exit from cycle