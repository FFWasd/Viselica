import os, random
from human_image import viselica

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def create_viselica(mistakes):
    return viselica.get(mistakes)



def find_letter(word,letter,guess_word,mistakes):
    word1=list(word)
    g_word=list(guess_word)
    flag=False
    for i in range(len(word)):
        if word1[i]==letter:
            g_word[i]=letter
            flag=True
    guess_word="".join(g_word)
    word="".join(word)
    if not flag:
        mistakes+=1
    return guess_word,mistakes


def check_letter(letter):
    letter=letter.lower()

    if letter not in "ёйцукенгшщзхъфывапролджэячсмитьбю":
        print("Поддреживается ввод только букв из русского алфавита")
        clear_terminal()
        print(create_viselica(mistakes))
        print(f"Попытка: {attempt}")
        print(f"Ошибки: {mistakes}")
        print(guess_word)
        print("Поддреживается ввод только букв из русского алфавита")
        letter=str(input("Введите новую букву: "))
        return check_letter(letter)

    elif not letter in used_letters :
        used_letters.append(letter)
        clear_terminal()
        print(create_viselica(mistakes))
        print(f"Попытка: {attempt}")
        print(f"Ошибки: {mistakes}")

    else:
        clear_terminal()
        print(create_viselica(mistakes))
        print(f"Попытка: {attempt}")
        print(f"Ошибки: {mistakes}")
        print(guess_word)
        print("Эта буква уже была!!!")
        letter=str(input("Введите новую букву: "))
        return check_letter(letter)
def game():
    global mistakes, attempt, used_letters, guess_word
    animals=["слон", "жираф", "бегемот", "аист", "кошка", "собака", "лев", "чайка", "карась", "хомяк"]
    food=["яблоко", "банан", "пюре", "котлета", "стейк", "ананас", "мороженое", "капуста", "картофель", "помидор"]
    sport=["мяч", "футбол", "лыжи", "баскетбол", "бита", "тачдаун", "пас", "кёрлинг", "волейбол", "клюшка"]
    geography=["россия", "пермь", "казань", "америка", "шотландия", "эдинбург", "владивосток", "германия", "франция", "москва"]

    print("1. Животные \n2. Еда \n3. Спорт \n4. География")
    used_letters=[]
    kateg=int(input("Выберите категорию: "))
    attempt=1
    mistakes=0

    match kateg:
        case 1:
            word=random.choice(animals)
        case 2:
            word=random.choice(food)
        case 3:
            word=random.choice(sport)
        case 4:
            word=random.choice(geography)

    guess_word="_"*len(word)

    while(mistakes<6 and guess_word!=word):
        clear_terminal()
        print(word)
        print(create_viselica(mistakes))
        print(f"Попытка: {attempt}")
        print(f"Ошибки: {mistakes}")
        print(guess_word)
        letter=str(input("Введите букву: "))
        check_letter(letter)
        attempt+=1
        guess_word,mistakes=find_letter(word,letter,guess_word,mistakes)
    

    if mistakes==6:
        clear_terminal()
        print(create_viselica(mistakes))
        print("Вы проиграли")
        print(f"Количество попыток: {attempt}")
        play_again=input(str("Хотите сыграть снова? (да/нет): ")).strip().lower()
        if play_again=="да":
            game()
        else:
            print("Будем ждать снова")
    else:
        clear_terminal()
        print(create_viselica(mistakes))
        print(f"Поздравляем, вы угадали слово: ")
        print(f"Слово угадано с {attempt} попытки")
        print(f"Вы ошиблись {mistakes} раз")


if __name__=="__main__":
    game()