#importing live btc price
import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
data = response.json()
btcp=data["bpi"]["USD"]["rate"]
print('Value of bitcoin= ',btcp)


#rounding it off and removing errors from price
li=btcp.split(',') 
st=li[0]+li[1]
st=st.split('.')   
print('Value of bitcoin(approx)= ',st[0])
btcp2=int(st[0])

#main code that will run the operation
n=int(input("Enter the number of exchanges "))
d=0
for i in range(n):
    a=int(input("Exchange balance "))
    d=a+d
total=int(d)+2500
print("total value in usd= " ,total)
totalbtc=int(d)/int(btcp2)
print("total value in btc= " ,totalbtc)

#saving the date in a file for future reference
from datetime import date 
date = date.today()
f=open("balancehistory.txt","a+")
f.write('Date='+' '+str(date)+'\n'+'Value in usd='+' '+str(total)+'\n'+'Value in btc ='+' '+str(totalbtc)+'\n'+'\n')
f.close()






