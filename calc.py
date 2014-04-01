"""Zadanie domowe - kalkulator"""
def add(args):
    """Suma elementow listy."""
    result = 0
    for arg in args:
        result += float(arg)
    return result
def multi(args):
    """Iloczyn argumentow listy."""
    result = 1
    for arg in args:
        result *= float(arg)
    return result
def subb(args):
    """Odejmowanie od pierwszego elementu listy."""
    result = float(args[0])
    for arg in args[1:]:
        result -= float(arg)
    return result
def div(args):
    """Wynik dzielenia pierwszego elementu listy przez kolejne."""
    result = float(args[0])
    for arg in args[1:]:
        result /= float(arg)
    return result
def power(args):
    """Potegowanie pierwszego elementu listy do kolejnych"""
    result = float(args[0])
    for arg in args[1:]:
        result **= float(arg)
    return result
def save(history, file_name):
    """Zapis historii do pliku"""
    with open(file_name, 'w') as his_file:
        his_file.write(history)
def main():
    """Glowna funkcja kalkulatora"""
    history = ""
    actions = {'+':add, '-':subb, '*':multi, '/':div, '**':power, '^':power,
        'save':save, 'quit':0}
    while 1:
        input_line = raw_input("?> ")
        input_list = input_line.split(' ')
        if input_list[0] in actions:
            if input_list[0] == 'quit':
                break
            elif len(input_list) >= 2:
                if input_list[0] == 'save':
                    save(history, input_list[1])
                else:
                    try:
                        result = actions[input_list[0]](input_list[1:])
                    except ValueError:
                        print "Niepoprawny argument!"
                    except ZeroDivisionError:
                        print "Dzielenie przez zero!"
                    else:
                        history += input_line
                        history += '\n'
                        history += str(result)
                        history += '\n'
                        print str(result)
            else:
                print "Za mala lista argumentow"
        else:
            print "Nie rozpoznane polecenie"
if __name__ == '__main__':
    main()

