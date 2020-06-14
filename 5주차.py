import operator

def menu() :
    print('1. 데이터 추가''\n'
        '2. 데이터 검색''\n'
        '3. 데이터 삭제''\n'
        '4. 데이터 정렬''\n'
        '5. 데이터 출력''\n'
        '0. 종료''\n')
    key = int(input("메뉴를 선택하세요 : "))
    return key

def addinfo() :
    global info
    global std
    part = input(("학과를 입력하세요 : "))
    info.append(part)
    num = input(("학번을 입력하세요 : "))
    info.append(num)
    name = input(("이름을 입력하세요 : "))
    info.append(name)
    korea = int(input("국어 성적을 입력하세요 : "))
    info.append(korea)
    eng = int(input("영어 성적을 입력하세요 : "))
    info.append(eng)
    math = int(input("수학 성적을 입력하세요 : "))
    info.append(math)
    sum = info[3] + info[4] + info[5]
    info.append(sum)
    avg = float(info[6] / 3)
    avg = round(avg, 1)
    info.append(avg)
    if avg >= 95:
        grade = 'A+'
    elif (avg >= 90) and (avg < 95):
        grade = 'A0'
    elif (avg >= 85) and (avg < 90):
        grade = 'B+'
    elif (avg >= 80) and (avg < 85):
        grade = 'B0'
    elif (avg >= 75) and (avg < 80):
        grade = 'C+'
    elif (avg >= 70) and (avg < 75):
        grade = 'C0'
    elif (avg >= 65) and (avg < 70):
        grade = 'D+'
    elif (avg >= 60) and (avg < 65):
        grade = 'D0'
    else:
        grade = 'F'
    info.append(grade)
    std.append(info)
    info = []

def searchstd() :
    global std
    global keys
    stack = 0
    search = input("검색할 학생의 이름 또는 학번을 입력하세요 : ")
    for i in range(len(std)):
        if (search == std[i][1]) or (search == std[i][2]):
            dic = dict(zip(keys, std[i]))
            print(dic)
            break
        stack += 1
    if (stack == len(std)):
        print("찾을 수 없습니다.")

def delstd() :
    global std
    delete = input("삭제할 학생의 이름 또는 학번을 입력하세요 : ")
    for i in range(len(std)):
        if (delete == std[i][1]) or (delete == std[i][2]):
            del (std[i])
            break
def sortstd() :
    global std
    sortkey = input("학과로 정렬하려면 1, 학번으로 정렬하려면 2를 입력하세요 : ")
    if (sortkey == 1):
        std.sort(key=lambda x: x[0])
    elif (sortkey == 2):
        std.sort(key=lambda x: x[1])

def printstd() :
    global std
    global keys
    for i in range(len(std)):
        dic = dict(zip(keys, std[i]))
        print(dic)

global keys
keys=['학과','학번','이름','국어','영어','수학','총점','평균','학점']
global info
info = []
global std
std = []

while True:
    menukey=menu()
    if menukey == 1:
        addinfo()

    elif menukey == 2:
        searchstd()

    elif menukey == 3:
        delstd()

    elif menukey == 4:
        sortstd()

    elif menukey == 0:
        print("종료합니다.")
        break

    elif menukey == 5:
        printstd()

    else:
        continue