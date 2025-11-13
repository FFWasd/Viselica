import os, random, time
from human_image import viselica, window
from secrets_mod import photo

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
    
    window()
    # print("1. Животные \n2. Еда \n3. Спорт \n4. География")
    used_letters=[]
    kateg=int(input("Выберите категорию: "))
    attempt=1
    mistakes=0

    print("\nВыберите режим:")
    print("1 — Обычный")
    print("2 — На время")
    mode = input("Введите номер режима: ").strip()

    if mode == "2":
        timed_mode = True
        total_time = 60  # можно поменять на другое значение
        start_time = time.time()
    else:
        timed_mode = False

    match kateg:
        case 0: 
            
            mistakes=7
            word=''
            clear_terminal()

        case 1:
            word=random.choice(animals)
        case 2:
            word=random.choice(food)
        case 3:
            word=random.choice(sport)
        case 4:
            word=random.choice(geography)
        case 18:
            mistakes=18
            word=''
            
            

        case _:
            game()
            
            

    guess_word="_"*len(word)

    while(mistakes<6 and guess_word!=word):
        if timed_mode:
            elapsed = time.time() - start_time
            remaining = int(total_time - elapsed)
            if remaining <= 0:
                clear_terminal()
                print("⏰ Время вышло! Вы не успели угадать слово.")
                print(f"Слово было: {word}")
                play_again = input("Хотите сыграть снова? (да/нет): ").strip().lower()
                if play_again == "да":
                    game()
                else:
                    print("Будем ждать снова")
                return
        clear_terminal()
        # print(word) #загаданное слово
        print(create_viselica(mistakes))
        print(f"Попытка: {attempt}🙈")
        print(f"Ошибки: {mistakes}💩")
        if timed_mode:
            print(f"⏳ Осталось времени: {remaining} секунд")
        print(guess_word)
        letter=str(input("Введите букву: "))
        check_letter(letter)
        attempt+=1
        guess_word,mistakes=find_letter(word,letter,guess_word,mistakes)
    

    if mistakes==6:
        clear_terminal()
        print(create_viselica(mistakes))
        print("Вы проиграли🤮🤡👎")
        print(f"Количество попыток: {attempt}")
        print(f"Загадонное слово: {word}")
        play_again=input(str("Хотите сыграть снова? (да/нет): ")).strip().lower()
        if play_again=="да":
            game()
        else:
            print("Будем ждать снова")
    elif mistakes==7:
        clear_terminal()
        print("Будем ждать снова")
    elif mistakes==18:

        photo()
        
        
        
        
    else:
        clear_terminal()
        print(create_viselica(mistakes))
        print(f"Поздравляем, вы угадали слово❤️😍: ")
        print(f"Слово угадано с {attempt} попытки")
        print(f"Вы ошиблись {mistakes} раз👻")
        play_again=input(str("Хотите сыграть снова? (да/нет): ")).strip().lower()
        if play_again=="да":
            game()
        else:
            print("Будем ждать снова")


if __name__=="__main__":
    clear_terminal()
    game()