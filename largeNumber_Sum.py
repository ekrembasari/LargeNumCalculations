
#iki pozitif sayinin toplamini yapiyor sadece diger caseler eklenecek
#str_Sum(str,str) fonsiyonu ile iki float sayı stringini topluyoruz ve toplam str olarak dönüyor

#ondalık sayıların toplamı
def str_decSum(s1,s2):
    if len(s1)<len(s2):
        temp=s1
        s1=s2
        s2=temp
    #toplama işleminde kolaylık olması açısından basamak sayılarını eşitliyoruz
    for i in range(len(s1)-len(s2)):
        s2+='0'

    carry='0'
    sum=''
    #ilkokul matematiği toplama işlemi    
    for i in range(max(len(s1),len(s2))):
        temp_sum=int(s1[-i-1])+int(s2[-i-1])+int(carry[i])
        carry+=str(int(temp_sum / 10))
        sum+=str(temp_sum % 10)
        
    #son kalan eldeyi ekliyoruz
    if carry[-1]!='0':        
        sum+='.'+carry[-1]

    # let us remove all the unnecassary zeros in the end
    if sum[0]=='0':
        
        for i in range(len(sum)):
            if sum[i]=='0':
                continue
            elif sum[i]=='.':
                sum=sum[i-1:]
                break
            else:
                sum=sum[i:]
                break

    #diziyi tersine cevirip gönderiyoruz
    return sum[::-1]
        
#integer sayıların toplamı       
def str_intSum(s1,s2):
    if len(s1)<len(s2):
        temp=s1
        s1=s2
        s2=temp
    #toplama işleminde kolaylık olması açısından basamak sayılarını eşitliyoruz
    s2=s2[::-1]
    for i in range(len(s1)-len(s2)):
        s2+='0'

    s2=s2[::-1]

    carry='0'
    sum=''
    #ilkokul matematiği toplama işlemi    
    for i in range(max(len(s1),len(s2))):
        temp_sum=int(s1[-i-1])+int(s2[-i-1])+int(carry[i])
        carry+=str(int(temp_sum / 10))
        sum+=str(temp_sum % 10)
        
    #son kalan eldeyi ekliyoruz
    if carry[-1]!='0':        
        sum+=carry[-1]
    #diziyi tersine çevirip gönderiyoruz
    return sum[::-1]

def dot_check(sx):
    if sx.find('.')==-1:
        sx+='.0'

    return sx

#girilen float tipi integer stringini tam ve ondalık kısımlarına ayırıp yukarıda tanımladığımız ilgili foknsiyonlarla toplamayı yapıyoruz
def str_Sum(s1,s2):
    s1=dot_check(s1)
    s2=dot_check(s2)
    
    temp_D = str_decSum(s1[s1.find('.')+1:],s2[s2.find('.')+1:])
    temp_I = str_intSum(s1[:s1.find('.')],s2[:s2.find('.')])

    #ondalık kısımların toplamı 1 den büyük eşit olursa tam kısmı temp_I ya ekliyoruz
    if temp_D.find('.')!=-1:
        temp_I = str_intSum(temp_I,temp_D[:temp_D.find('.')])
        temp_D = temp_D[temp_D.find('.')+1:]
    
    return temp_I+'.'+temp_D
