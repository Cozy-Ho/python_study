score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

for line in score_file.readlines():
    print(line)

score_file.close()