#함수정의
def open_account():#계좌새성하는 역할
    print('계좌가 생성되었습니다.')

#전달값(입력값)과 반환값
#입금 함수 정의
def deposit(balance, money):
    print('입금이 완료되었습니다. 잔액은 {}원 입니다.'.format(balance+money))#옛날방식
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.")#요즘방식
    return balance+money


#출금 함수 정의
def withdraw(balance, money):
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {} 원 입니다.'.format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance(balance)))
        return balance


#저녁 출금시 수수료 포함
def withdraw_night(balance, money):
    commission=100
    return(commission,balance-money-commission)#반환값이 2개임


#함수 사용(호출)
balance=0
balance = deposit(10000,1000)
#print(f"현재 잔액은 {result} 입니다.")

balance=withdraw(balance,5000)
(commission,balance)=withdraw_night(balance,5000)
print("수수료 {} 원이며, 잔액은 {} 원입니다.".format(commission,balance))