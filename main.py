n = 100
while n > 0:
    n -= 1
    user_word = input("Enter a word that you want to revers: ")
    rev_word = ''.join(reversed(user_word))
    print(rev_word)
