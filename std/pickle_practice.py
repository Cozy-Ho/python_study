with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("Studying python...!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())