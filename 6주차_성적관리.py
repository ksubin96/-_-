import operator

class student:
    def __init__(self, part, num, name, korea, eng, math, sum, avg, grade):
        self.part = part
        self.num = num
        self.name = name
        self.korea = korea
        self.eng = eng
        self.math = math
        self.sum = sum
        self.avg = avg
        self.grade = grade

    def getpart(self):
        return self.part
    def getnum(self):
        return self.num
    def getname(self):
        return self.name
    def getkorea(self):
        return self.korea
    def geteng(self):
        return self.eng
    def getmath(self):
        return self.math
    def getsum(self):
        return self.sum
    def getavg(self):
        return self.avg
    def getgrade(self):
        return self.grade

def searchstd(std):
        search = input("검색할 학생의 이름 또는 학번을 입력하세요 : ")
        for i in range(len(std)):
            if (search == std[i].getname()) or (search == std[i].getnum()):
                printstd(std, i)
                return None
        print("찾을 수 없습니다.")

def delstd(std):
        delete = input("삭제할 학생의 이름 또는 학번을 입력하세요 : ")
        for i in range(len(std)):
            if (delete == std[i].getname()) or (delete == std[i].getnum()):
                del(std[i])
                break

def sortstd(std):
        sortkey = int(input("학과로 정렬하려면 1, 학번으로 정렬하려면 2를 입력하세요 : "))
        if (sortkey == 1):
            std.sort(key=lambda x:x.part)

        elif (sortkey == 2):
            std.sort(key=lambda x:x.num)

def printstd(std, stdnum = None):
        if stdnum == None:
            for i in range(len(std)):
                print("학과 :",std[i].part," 학번 :",std[i].num, " 이름 :", std[i].name, " 국어 :", std[i].korea,
                      " 영어 :", std[i].eng, " 수학 :", std[i].math, " 총점 :", std[i].sum, " 평균 :", std[i].avg, " 학점 :", std[i].grade)
        else:
            print("학과 :", std[stdnum].part, " 학번 :", std[stdnum].num, " 이름 :", std[stdnum].name, " 국어 :",std[stdnum].korea,
                  " 영어 :", std[stdnum].eng, " 수학 :", std[stdnum].math, " 총점 :", std[stdnum].sum, " 평균 :",std[stdnum].avg, " 학점 :", std[stdnum].grade)
            print("\n")

def addinfo(std):
        part = input(("학과를 입력하세요 : "))
        num = input(("학번을 입력하세요 : "))
        name = input(("이름을 입력하세요 : "))
        korea = int(input("국어 성적을 입력하세요 : "))
        eng = int(input("영어 성적을 입력하세요 : "))
        math = int(input("수학 성적을 입력하세요 : "))
        sum = korea + eng + math
        avg = round(float(sum / 3), 1)
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
        std.append(student(part, num, name, korea, eng, math, sum, avg, grade))

def menu():
    print('1. 데이터 추가''\n'
          '2. 데이터 검색''\n'
          '3. 데이터 삭제''\n'
          '4. 데이터 정렬''\n'
          '5. 데이터 출력''\n'
          '0. 종료''\n')
    key = int(input("메뉴를 선택하세요 : "))
    return key

# main 부분
std = list()
while True:
    menukey = menu()
    if menukey == 1:
        addinfo(std)

    elif menukey == 2:
        searchstd(std)

    elif menukey == 3:
        delstd(std)

    elif menukey == 4:
        sortstd(std)

    elif menukey == 0:
        print("종료합니다.")
        break

    elif menukey == 5:
        printstd(std)

    else:
        continue