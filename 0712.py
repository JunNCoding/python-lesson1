# #숫자 패턴 맞추기 게임
# pattern1 = [2,4,6,8]
# correctAns = 0
# wrongAns = 0

# def pattern_match(pattern,correctAns,wrongAns):
#     for i in range(len(pattern)-1):
#         print(pattern[i],end=" ")

#     guess_num = int(input('다음 수는 무엇일까요? '))
#     if guess_num == pattern[len(pattern)-1]:
#         correctAns += 1
#         print('잘했어요..')
#     else:
#         wrongAns += 1
#         print("틀렸네요..")
    
#     return (correctAns, wrongAns)

# correctAns = 0 
# wrongAns = 0

# pattern1 = [2,4,6,8]
# pattern2 = [13,16,19,22]
# pattern3 = [2,3,5,7,11]
# pattern4 = [1,1,2,3,5,8]
# pattern5 = [31,28,31,30]

# correctAns, wrongAns = pattern_match(pattern1, correctAns, wrongAns)
# correctAns, wrongAns = pattern_match(pattern2, correctAns, wrongAns)
# correctAns, wrongAns = pattern_match(pattern3, correctAns, wrongAns)
# correctAns, wrongAns = pattern_match(pattern4, correctAns, wrongAns)
# correctAns, wrongAns = pattern_match(pattern5, correctAns, wrongAns)

# print("%d개 패턴중 %d개 맞았어요" %(correctAns + wrongAns, correctAns))



# #1. 파일 열기
# #file = open("basic.txt","w",encoding = 'utf8')
# file = open("basic.txt",'r',encoding = 'utf8')
# #2. 파일 내용 쓰기
# file.write("Hello Python Programming...!")
# #3. 파일 읽기
# print(file.read())

# #4. 파일 닫기 
# file.close()


# with open('score.txt','w',encoding='utf8')as score_file:
   
#     score_file.write('60');
#     score_file.write('\n100');
#     score_file.write('\n70');


for i in range(1,51):
    with open(str(i)+'주차.txt','w',encoding='utf8') as report:
        report.write('- {0} 주차 주간보고 -'.format(i))
        report.write('부서: ')
        report.write('\n이름: ')
        report.write('\n업무 요약: ') 