# import movie_price

# movie_price.price(3) #3명의 일반 영화 가격
# movie_price.price_morining(4) #4명의 조조할인 가격
# movie_price.price_solder(5) #5명의 군인할인 가격

# 1
# from movie_price import * #모든 함수를 사용할 수 있다
# price(3)
# price_morining(4)
# price_solder(5)

# 2
# import movie_price as mp
# mp.price(3)
# mp.price_morining(4)
# mp.price_solder(5)

# 3
# from movie_price import price, price_morining
# price(3)
# price_morining(4)

# from movie_price import price_solder as price
# price(5)



# import travel_package.Tiland as tiland
# import travel_package.Vietnam as vietnam
# from travel_package import *
# Tiland.tiland_package()
# Vietnam.vietnam_package()
# import travel_package.Tiland


# print('메인의 name을 출력합니다.')
# print(__name__)
# print()

# 외부 모듈 사용

# import matplotlib.pyplot as plt
# data = [100,250,330,500.700]
# plt.plot(data)
# plt.show()

# import matplotlib.pyplot as plt
# x_data= [10,20,30,40,50]
# y_data = [10000,15000,33000,34000,60000]
# plt.plot(x_data, y_data, color='red',linestyle=':',marker='$★$')
# #plt.plot(x_data, y_data, 'r:$★$')
# plt.show()

# import matplotlib.pyplot as plt
# x_data = ['1st','2st','3rd','4th','5th']
# y1_data = [90,28,75,58,78]
# y2_data = [80,80,50,40,90]
# y3_data = [40,50,90,90,60]
# plt.plot(x_data,y1_data,'r-o',x_data,y2_data,'g:x',x_data,y3_data,'b--p')
# plt.show()

import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

font_name = font_manager.FontProperties(fname='C:/Wondows/Fonts/')