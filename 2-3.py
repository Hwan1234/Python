#더하기 함수 정의
def add(a,b):
        c = a + b
        return c
#빼기 함수 정의
def minus(a,b):
        c = a - b
        return c
#곱하기 함수 정의
def multi(a,b):
        c = a*b
        return c
#나누기 함수 정의
def divide(a,b):
        c = a/b
        return c
while True :
    a=input("1st input?")

    if a=="0000":
        break
    b = int(input("2nd input?"))
    a = int(a);
    
    
    #더하기 함수 호출
    result =add (a,b)
    print(a,"+",b,"=",result)
    #빼기 함수 호출
    result=minus(a,b)
    print(a, "-", b, "=", result)
    #곱하기 함수 호출 
    result= a * b
    print(a, "*", b, "=", result)
    result= a / b
    print(a, "/", b, "=", result)
    print("\n")

print("exit")
