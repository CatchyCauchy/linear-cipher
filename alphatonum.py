with open ('cipher.txt', 'r') as f:
    data=f.read()
output=''
for i in range(len(data)):
    if data[i].isalpha() and data[i].islower():
        num=str(ord(data[i])-97)
        output=output+num+''
    elif data[i]==' ':
        output=output+'\t'
    elif data[i].isalpha() and data[i].isupper():
        num=str(ord(data[i])-39)
        output=output+num+''
    else:
        output=output+data[i]+' '
print("Output : "+output)
        
