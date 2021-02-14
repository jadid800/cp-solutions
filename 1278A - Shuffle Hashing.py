def str_2_list(a_str):
    a_list=[]
    for i in range(len(a_str)):
        a_list.append(a_str[i])
    return a_list
    
def is_valid(password, hash_code):
    has_pass=False
    sorted_hash=''
    sorted_pass=sorted(password)
    try:
        for i in range(len(hash_code)):
            sorted_hash=sorted(hash_code[i:i+len(password)])
            sorted_pass=''.join(str(x) for x in sorted_pass)
            sorted_hash=''.join(str(x) for x in sorted_hash)
            
            
            if(sorted_pass in sorted_hash):
                return True
    except IndexError:
        pass
    return False            
            
repeat=int(input())
for rep in range(repeat):
    password=input()
    password= str_2_list(password)

    hash_code=input()
    hash_code= str_2_list(hash_code)

    if(is_valid(password, hash_code)):
        print("YES")
    else:
        print("NO")
