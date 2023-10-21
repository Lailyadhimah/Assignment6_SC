from Math_function import add
from Math_function import multiply
from Math_function import divide

def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = multiply(data_1, data_2)
    elif operator == "/":
        if data_2 == 0:
            print("Pembagian dengan nol tidak diizinkan.")
        else:
            result = divide(data_1, data_2)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()