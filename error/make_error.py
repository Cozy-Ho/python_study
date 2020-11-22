class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    num1 = int(input("first num : "))
    num2 = int(input("second num : "))

    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1/num2)}")

except ValueError:
    print("wrong value. please input single number")
except BigNumberError as err:
    print("Error!! ")
    print(err)
finally:
    print("program end successful")