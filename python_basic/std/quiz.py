def make_report(num):
    for i in range(num):
        with open(f"{i+1}주차.txt","w",encoding="utf8") as report:
            report.write(f"- {i+1} 주차 주간보고 - \n부서 : \n이름 : \n엄부 요약 : ")

make_report(5)