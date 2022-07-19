# 일반 가격
def price(people):
    print('{0} 명 일반 가격{1} 원 입니다. '.format(people, people * 1000))

# 조조할인 가격
def price_morining(people):
    print('{0} 명 조조 할인 가격 {1} 원 입니다. '.format(people,people*6000))

# 군인 할인가격
def price_solder(people):
    print('{0} 명 군인 할인 가격 {1} 원 입니다. '.format(people,people*4000))