import random
word = ["java", "html"]


def hang():
    ran_word = random.choice(word)
    print(ran_word)
    li_word = list(ran_word)
    res = []
    res = ["-" for i in range(len(li_word))]
    print(res)
    inp = input("Enter the word :  ")
    for i in range(len(li_word)):
        if li_word[i] == inp:
            res[i] = li_word[i]
    print(res)

    # print("Do you want to play again (y/n)  : ")
    # key = input()
    # if key == 'y':
    #     hang()
    # else:
    #     print("Thankyou!")


hang()
