# open text file.
# r for reading, w for writing, a for appending.

file_path = "/Users/hantaehee/Downloads/file.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

file_path = "/Users/hantaehee/Downloads/file.txt"
with open(file_path, "r", encoding="utf-8") as file:
    file_stuff = file.read()
    print(file_stuff)

# reading the content line by line
file_path = "/Users/hantaehee/Downloads/file.txt"

with open(file_path, "r", encoding="utf-8") as file:
    line1 = file.readline().strip()  # 개행 문자 제거
    line2 = file.readline().strip()

print(line1)

if 'important' in line2.lower():  # 대소문자 구분 없이 비교
    print('This line is important!')

# 더 효율적인 파일 읽기 방식
for line in file:
    print(line.strip())  # 개행 문자 제거