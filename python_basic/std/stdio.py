import sys

print("Python", "Java", file=sys.stderr)

scores = {"Math":0, "Eng":50, "CS":100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무값이나 입력하세요 : " )
print(f"입력값 : {answer: >10}")

print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >10}".format(+500))


print("{0:_<10}".format(500))

# 3자리 마다 , 찍기.
print("{0:,}".format(500000000000000))


print("{0: >10}".format(500))
print("{0: >10}".format(500))
print("{0: >10}".format(500))
