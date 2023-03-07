def proc1():
    words = []
    while (new_word :=str(input())) != "stop":
        words.append(new_word)

    print(" ".join(words))
proc1()

def proc2():
    words = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Это не редкое слово!")
proc2()

def proc3():
    print("Ноль в качестве знака операции""\n завершит работу операции")
    while True:
        s = input("Знак (+,-,*,/): ")
        if s== '0':
            break
        if s in ('+','-','*','/'):
            x = float(input("x="))
            y = float(input("y="))
            if s =='+':
                print("%.2f" % (x+y))
            elif s == '-':
                print("%.2f" % (x-y))
            elif s == '*':
                print("%.2f" % (x*y))
            elif s == '/':
                if y != 0:
                    print("%.2f" % (x/y))
                else:
                    print("Делить на ноль нельзя")
        else:
            print("Неверный знак операции")
proc3()



