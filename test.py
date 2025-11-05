guess_word="_____"
word="кошка"
letter="к"
def find_letter(word,letter,guess_word):
    word1=list(word)
    g_word=list(guess_word)
    flag=False
    for i in range(len(word)):
        if word1[i]==letter:
            g_word[i]=letter
            flag=True
    guess_word="".join(g_word)
    word="".join(word)
    return guess_word

guess_word=find_letter(word,letter,guess_word)

print(guess_word)