#1. 파일 열고, 읽어오기

# 리스트 내용 한꺼번에 출력하는 함수
from numpy import _2Tuple


def print_list(plist):
    for data in plist:
        print(data,end="\t")
    print()

with open('통합 문서1.csv','r')as sing_file:
    with open('new_singer1.csv','w',encoding='utf8')as sing_file2:
        header = sing_file.readline()
        header = header.strip()
        header_list = header.split(',')

        # 헤더리스트를 한꺼번에 문자열로 만들기
        header_str=','.join(map(str,header_list))

        # 헤더 문자열 파일에 쓰기
        sing_file2.write(header_str + '\n')

        # 헤더리스트 내용 출력 함수 호출
        print_list(header_list)

        for row in sing_file:
            row = row.strip()
            row_list = row.split(',')
            print_list(row_list)

            row_list[-1] = row_list[-1].replace('.','/')

            row_str = ','.join(map(str,row_list))

            sing_file2.write(row_str+'\n')

print("파일 복사 성공~~~~")

            
class Student:
    pass