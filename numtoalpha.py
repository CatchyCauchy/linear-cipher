with open ('cipher.txt', 'r') as f:
    data=f.read()
output=''
for i in range(len(data)):
    if data[i].isnumeric():
        letter=chr(int(data[i])+97)
        output=output+letter+''
    elif data[i]==' ':
        output=output+' '
    else:
        output=output+data[i]+' '
print("Output : "+output)
        
