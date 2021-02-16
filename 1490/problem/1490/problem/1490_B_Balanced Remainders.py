def find_divisors(a_list):
    c0,c1,c2=0,0,0
    for i in a_list:
        if(i%3==0):
            c0+=1
        elif(i%3==1):
            c1+=1
        else:
            c2+=1
    return c0,c1,c2
repeat=int(input())
for rep in range(repeat):
    length=int(input())       
    div_arr=list(map(int, input().split()))
    c0,c1,c2=find_divisors(div_arr)
    operations=0
    standard=length//3
    subtract=0
    while(True):
        if(c0>standard):
            subtract=c0-standard
            c0-=subtract
            c1+=subtract
            operations+=subtract
        
        if(c1>standard):
            subtract=c1-standard
            c1-=subtract
            c2+=subtract
            operations+=subtract
        
        if(c2>standard):
            subtract=c2-standard
            c2-=subtract
            c0+=subtract
            operations+=subtract
        if(c1==standard and c0==standard and c2==standard  ):
            break
    print(operations)
