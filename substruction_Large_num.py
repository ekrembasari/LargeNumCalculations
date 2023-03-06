import largeNumber_Sum 


swap=False
sign=[False,False]#isaret kontrolü eger false ise pozitif true ise negatif 
sign_count=0

#Checking if entered string has dot or not
def dot(sx):
    if sx.find('.')==-1:
        sx+='.0'
    
    return sx
# Adding zeros to make strings equal length.
def equal_len(s1,s2):
    i1=s1.find('.')
    i2=s2.find('.')
    d1=len(s1)-i1-1
    d2=len(s2)-i2-1
    #print(d1,d2)
#adding zeros to integer part from left
    if i1!=i2:
        if i1-i2>0:
            s2=s2[::-1]
            for i in range(i1-i2):
                s2+='0'

            s2=s2[::-1]

        else:
            s1=s1[::-1]
            for i in range (i2 - i1):
                s1+='0'

            s1=s1[::-1]
            
#adding zeros to decimal part from right
            
    if d1!=d2:
        if d1-d2>0:
            for i in range(d1-d2):
                s2+='0'
                

        else:
            for i in range(d2-d1):
                s1+='0'

    return s1,s2
        
def detect_greater(s1,s2):
    #print('s1=',s1,s2)
    for i in range(len(s1)):
        if s1[i]>s2[i]:
            return False
        
        if s2[i]>s1[i]:            
            return True
            

    return False

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

def usual_subs(s1,s2):
    temp_ex=''
    temp_rslt=''
    for i in range(len(s1)):
        if s1[i]=='.':
            temp_ex+='.'
            temp_rslt+='.'
            continue
        
        temp=int(s1[i])-int(s2[i])
        if temp<0:
            temp_ex+='1'        

        else:
            temp_ex+='0'
            
        temp_rslt+=str(temp % 10)
        
#yukarida soldan baslayarak mod 10 da cikarma islemi yapiyoruz. eger cikarma isleminin sonucu negatif olursa temp_ex te 1
#pozitif olursa 0 sifir yaziyoruz bu son olarak altta yaptigimiz bir basamak sola kayrdirma ile tam olarak normalde elde
#etmemiz gereken sonuctan ne kadar fazla buldugumuzu hesaplamis oluyoruz. Devaminda bunu da cikariyoruz
    if temp_ex[temp_ex.find('.')+1]=='0':
        temp_ex=temp_ex[1:temp_ex.find('.')]+'0.'+temp_ex[temp_ex.find('.')+2:]+'0'
    else:
        temp_ex=temp_ex[1:temp_ex.find('.')]+'1.'+temp_ex[temp_ex.find('.')+2:]+'0'
    #print('rslt=',temp_rslt)
    #print('ex=',temp_ex)

    if temp_ex.find('1')!=-1:
        temp_rslt=usual_subs(temp_rslt,temp_ex)

    return temp_rslt

def str_Sub(s1,s2):
    s1=sign_check(s1)
    s2=sign_check(s2)
    

    if len(s1)<len(s2):
        temp = s1
        s1=s2
        s2=temp

    s1=dot(s1)
    s2=dot(s2)

    s1,s2=equal_len(s1,s2)

    if detect_greater(s1,s2)== True:
        global swap
        swap=True
        temp=s1
        s1=s2
        s2=temp
    #print(ts1,ts2)

    if swap == True:
        if sign[0]== True and sign[1]== True:
            temp_sub = usual_subs(s1,s2)
            return temp_sub

        elif sign[0]==False and sign[1]==False:
            temp_sub ='-'+usual_subs(s1,s2)
            return temp_sub

        elif sign[0]==True and sign[1]==False:
            
            temp_sum=largeNumber_Sum.str_Sum(s1,s2)
            return '-'+temp_sum

        else:
            temp_sum=largeNumber_Sum.str_Sum(s1,s2)
            return temp_sum


    else:
        if sign[0]== True and sign[1]== True:
            temp_sub ='-'+usual_subs(s1,s2)
            return temp_sub

        elif sign[0]==False and sign[1]==False:
            temp_sub = usual_subs(s1,s2)
            return temp_sub

        elif sign[0]==True and sign[1]==False:
            temp_sum=largeNumber_Sum.str_Sum(s1,s2)
            return '-'+temp_sum

        else:
            temp_sum=largeNumber_Sum.str_Sum(s1,s2)
            return temp_sum





        
def Sub(s1,s2):
    try:        
        return str_Sub(s1,s2)   

    except:
        print('Make sure your number consist of integers and at most one "-" in the begining and one "." somewhere in the middle ')
        


    
        

    
