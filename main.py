# Рекурсивное умножение цифр

def get_multiplied_digits(number, proiz ):
    str_number = str(number)
    first = int(str_number[0])
    proiz=first*proiz
    if (str_number[1:] !="" and str_number[1:]!="0"):
        get_multiplied_digits(int(str_number[1:]), proiz)
    else:
        print(proiz)

number = input("Введите целое число: ")
get_multiplied_digits(number,1)

