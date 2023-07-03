a=int(input("Input a = "))
b=int(input("Input b = "))
output=''
with open('plaintext.txt','r') as p:
      plain=p.read()
for i in range(len(plain)):
    if plain[i].isalpha() and plain[i].islower():
        num=str(((a*(ord(plain[i])-97))+b)%26)
        letter=chr(int(num)+97)
        output=output+letter+''
    elif plain[i]==' ':
        output=output+'\t'
    elif plain[i].isalpha() and plain[i].isupper():
        num=str(((a*ord(plain[i])-39)+b)%26)
        letter=chr(int(num)+39)
        output=output+letter+''
    else:
        output=output+plain[i]+''
print("Output : "+output)

