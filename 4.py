#4 座標判斷 計算原點距離

x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
if(x>0 and y>0):
    print("該點在第一象限，離原點距離為根號",x**2+y**2)
elif(x<0 and y>0):
    print("該點在第二象限，離原點距離為根號",x**2+y**2)
elif(x<0 and y<0):
    print("該點在第三象限，離原點距離為根號",x**2+y**2)
elif(x>0 and y<0):
    print("該點在第四象限，離原點距離為根號",x**2+y**2)
elif(x>0 and y==0):
    print("該點位於右半平面X軸上，離原點距離為根號",x**2)
elif(x<0 and y==0):
    print("該點位於左半平面X軸上，離原點距離為根號",x**2)
elif(x==0 and y>0):
    print("該點位於上半平面Y軸上，離原點距離為根號",y**2)
elif(x==0 and y<0):
    print("該點位於下半平面Y軸上，離原點距離為根號",y**2)
elif(x==0 and y==0):
    print("該點位於原點")