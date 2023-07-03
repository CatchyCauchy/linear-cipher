a=int(input("Input a = "))
b=int(input("Input b = "))
output=''
with open('ciphertext.txt','r') as p:
      cipher=p.read()
for i in range(len(cipher)):
    if cipher[i].isalpha() and cipher[i].islower():
        #converting the letter in ciphertext to number
        num=int(ord(cipher[i])-97)
        #decrypting
        dec=((num-b)*a**11)%26
        #converting decrypted number to letter
        letter=chr(int(dec)+97)
        output=output+letter+''
    elif cipher[i]==' ':
        output=output+' '
    elif cipher[i].isalpha() and cipher[i].isupper():
        num=int(ord(cipher[i])-39)
        num2=((num-b)*a**11)%26
        letter=chr(int(num2)+97)
        output=output+letter+''
    else:
        output=output+cipher[i]+' '
print("Output : "+output)

