fh=open("output6.txt",'w')
n = int(input("enter the value"))
i =1
sum=i
while(i<=n):
 sum=sum*i
 i+=1
fh.write('The factorial is:'+str(sum)) 