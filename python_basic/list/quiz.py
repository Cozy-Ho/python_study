from random import *

def event(num):
    temp_list = list(range(1,21))

    chicken = sample(temp_list, 1)
    temp_list.remove(chicken[0])
    coffee = sample(temp_list, 3)
    print(f"""
    --- 당첨자 발표 ---
    치킨 당첨자 : {chicken}
    커피 당첨자 : {coffee}
    --- 축하합니다 ---
    """)

def texi(num):
    count = 0
    for i in range(num):
        time = randint(5,50)
        if(time<15):
            match='O'
            count += 1
        else:
            match=' '
        print(f"[{match}] {i+1}번째 손님 ( 소요시간 : {time} 분)" )
    print(f"총  탑승 승객 : {count} 분")

def fat(height, gender):
    if(gender == "남자"):
        return height*height*22
    else:
        return height*height*22

# event(20)
# texi(50)

height = 175
gender = "남자"
std_weight = round(fat(height/100, gender), 2)


print(f"키 {height}cm {gender}의 표준 체중은 {std_weight}kg 입니다.")

fat(175, "남자")

fat(160, "여자")