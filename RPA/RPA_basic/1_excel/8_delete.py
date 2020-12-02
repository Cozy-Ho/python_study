from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8)  # 8 번째 줄에있는 7번 학생 데이터 삭제.
# ws.delete_rows(8, 3)  # 8 번째 줄 부터 총 3줄 삭제.

ws.delete_cols(2)  # 2 번째 열(B) 삭제
ws.delete_cols(2, 2)  # 2 번째 열(B) 부터 2열 삭제


# wb.save("sample_delete_rows.xlsx")
wb.save("sample_delete_cols.xlsx")
