from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화 된 sheet를 가져옴

ws.title = "cozy-ho" # sheet의 이름을 변경

wb.save("sample.xlsx")
wb.close()