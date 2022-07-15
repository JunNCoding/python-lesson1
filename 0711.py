#함수정의
def open_account():#계좌새성하는 역할
    print('계좌가 생성되었습니다.')

#전달값(입력값)과 반환값
#입금 함수 정의
def deposit(money,balance=10000):
    print('입금이 완료되었습니다. 잔액은 {}원 입니다.'.format(balance+money))#옛날방식
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.")#요즘방식
    return balance+money


#출금 함수 정의
def withdraw(money,balance=10000):
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {} 원 입니다.'.format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance(balance)))
        return balance


#저녁 출금시 수수료 포함
def withdraw_night(money,balance=10000):
    commission=100
    return(commission,balance-money-commission)#반환값이 2개임


#함수 사용(호출)

balance = deposit(10000,1000)
#print(f"현재 잔액은 {result} 입니다.")

balance=withdraw(balance,5000)
(commission,balance)=withdraw_night(balance,5000)
print("수수료 {} 원이며, 잔액은 {} 원입니다.".format(commission,balance))


def print_n_times(n,*values):   #가변 매개변수(매개변수를 원하는 만큼 받을 수 있는 함수)
    #n번 반복합니다.
    for i in range(n):
        #valuse는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

#함수를 호출합니다.
print_n_times(3, "안녕하세요","즐거운","파이썬 프로그래밍")