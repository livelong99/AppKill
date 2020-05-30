num = input("Enter the Number : ")


count = len(num)
numb = ""
if(count%2==0):
    n = count
else:
    n = count+1

while(numb=="" or len(numb)!=1):
    numb=""
    if(count%2==0):
        n = count
    else:
        n = count+1
    for i in range(0,int(n/2)):
        if(num[i]>num[count-i-1]):
            numb = numb+num[i]
        elif(num[i]<num[count-1-i]):
            numb = numb+num[count-i-1]
        elif(i==count-i-1):
            numb = numb+num[count-i-1]
    count = len(numb)
    num = numb
    print(numb)

print("Strongest Digit:")
print(numb)
                    
        
    
