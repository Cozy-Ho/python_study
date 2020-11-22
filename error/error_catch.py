try:
    print("나누기")
    num1 = int(input("first : "))
    num2 = int(input("second: "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("err!! 잘못된 값을 입력했습니다.")