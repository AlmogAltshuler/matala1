def factorial(n):
    f=1
    if n==0:  
        return 1
    elif n>0:
        for k in range(1,n+1):
            f=f*k
        return f 

def exponent(x): 
    r=0
    for i in range(0,100):
        number=1
        p=0
        while p<i:
            number=number*x
            p=p+1
        r=r+(number)/factorial(i) 
    return r

def absolut(y_n,y_n_1):
    if(y_n-y_n_1)<0:
        a=-(y_n-y_n_1)
    else:
        a=(y_n-y_n_1)
    return a

def Ln(x):
    if x==0 or x<0:
        return 0.0
    else:
         y_n=x-1
         y_n_1=y_n+2*((x-exponent(y_n))/(x+exponent(y_n)))
         epsilon=0.001
         while absolut(y_n,y_n_1)>epsilon:
             y_n=y_n_1      
             y_n_1=y_n+2*((x-exponent(y_n))/(x+exponent(y_n)))
         return y_n_1  
 
def XtimesY(num,power): 
    if num<0:
        return 0.0
    else:
        return(exponent(power*Ln(num)))
        

def sqrt(number,sqrt_num):
    if sqrt_num<0:
        return 0.0
    elif sqrt_num==0:
        return 1.0
    else:
        return(exponent(1/number*Ln(sqrt_num)))
        
def calculate(num3):
    if num3==0 or num3<0:
        result=0.0
        return result
    else:
        result=exponent(num3)*xtimesy(7,num3)*sqrt(num3,num3)*XtimesY(num3,-1)
        result=float('%0.6f' % result)
        return result

 
  

  
