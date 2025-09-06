import random

computerGuess = random.randint(1, 10)
health = 3

while health > 0:
    print("Nyawa mu: ", health)
    jawabanUser = int(input("Tebak Angka 1-10: "))
    
    if jawabanUser == computerGuess:
        print("Yey Anda Benar. Jawabannya adalah: ", computerGuess)
        break
    elif jawabanUser < computerGuess:
        health -= 1
        print("Kekecilan bang")
    elif jawabanUser > computerGuess:
        health -= 1
        print("Kegedan bang")
        
if health == 0:
    print("Anda Gagal Jawabannya adalah ", computerGuess)