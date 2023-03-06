import largeNumber_Sum 

a='0.0000000000000001'
b='2222222.111111'


temp_mult='0.0'
sign=[False,False]
sign_count=0


#Checking if entered string has dot or not
def dot(sx):
    if sx.find('.')==-1:
        sx+='.0'
    
    return sx

def sign_check(s1):
    if s1[0]=='-':
        s1=s1[1:]
        global sign
        global sign_count
        sign[sign_count] = True
        #print(s1,sign[sign_count])

    else:
        sign[sign_count] = False
        
    

    sign_count+=1
    if sign_count >1:
        sign_count=0
    return s1

def dot_shift_r(s1):
    
    list1=list(s1)
    
    d=s1.find('.')
    list1[d]=list1[d+1]
    list1[d+1]='.'
    if list1[-1]=='.':
        s1=''.join(list1)+'0'
        return s1
    else:
        return ''.join(list1)

    
def dot_shift_l(s1):
    
    list1=list(s1)
    
    d=s1.find('.')
    list1[d]=list1[d-1]
    list1[d-1]='.'

    if list1[0]=='.':
        s1='0'+''.join(list1)
        return s1
    else:
        return ''.join(list1)

def handle_Zeros_l(s1):
    for i in range(s1.find('.')):
        if s1[0]=='0' and s1[1]=='0':
            s1=s1[1:]

    return s1

def str_Mult(s1,s2):
    

    s1=sign_check(s1)
    s2=sign_check(s2)

    s1=dot(s1)
    s2=dot(s2)
#separate integer and decimal parts
    temp_i = s2[:s2.find('.')]
    temp_d = s2[s2.find('.')+1:]

    temp_imult='0.0'
    temp_dmult='0.0'
    
    for basamak in range(len(temp_i)):
        syc=-1-basamak
        temp_Rshft=s1
        
        if int(temp_i[syc])==0:
            continue
        for shft in range(basamak):
            temp_Rshft=dot_shift_r(temp_Rshft)

        temp_isumm='0.0'

        for numOfsum in range(int(temp_i[syc])):
            temp_isumm=largeNumber_Sum.str_Sum(temp_isumm,temp_Rshft)

        temp_imult=largeNumber_Sum.str_Sum(temp_imult,temp_isumm)
        


    for d_basamak in range(len(temp_d)):
        temp_lshift=s1
        for shft in range(d_basamak+1):
            temp_lshift=dot_shift_l(temp_lshift)

        temp_dsumm='0.0'

        for i in range(int(temp_d[d_basamak])):
            temp_dsumm=largeNumber_Sum.str_Sum(temp_lshift,temp_dsumm)

        
        temp_dmult=largeNumber_Sum.str_Sum(temp_dmult,temp_dsumm)
        

    result=largeNumber_Sum.str_Sum(temp_dmult,temp_imult)
    result = handle_Zeros_l(result)
    if sign[0]^sign[1]:
        result= '-'+result

    return result

def Mul(s1,s2):
    try:        
        return str_Mult(s1,s2)
    

    except:
        print('Make sure your number consist of integers and at most one "-" in the begining and one "." somewhere in the middle ')
        

