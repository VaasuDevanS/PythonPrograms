#C:\Python27\python (2.7.12) 64-bit

'''  Program 1  '''
print "\nProgram 1---> Welcome to RCC Program"
print "Welcome to RCC"
print "########################################"


'''  Program 2  '''
print "Program 2---> Addition of Two Numbers"
print input("Enter the first number..")+input("Enter the Second number.."),"is the sum of given numbers."
print "########################################"


'''  Program 3  '''
print "Program 3---> Add,Sub,Mul,Div"
num1,num2=input("Enter the first number.."),input("Enter the Second number..")
print "Sum is..",num1+num2,"Difference is..",num1-num2,"Product is..",num1*num2,"Quotient is..",num1/num2,"Remainder is..",num1%num2
print "########################################"


'''  Program 4  '''
print "Program 4---> Convert celsius to Farenheit.."
print input("Enter the celsius..")*(9.0/5)+32,"is the corresponding Farenheit for the given celsius."
print "########################################"


'''  Program 5  '''
print "Program 5---> Area of circle for given radius"
from math import pi
print input("Enter the radius")**2*pi,"is the area of the circle."
print "########################################"


'''  Program 6  '''
print "Program 6--> Swapping two numbers using temp variable"
a,b=input("Enter the first number.."),input("Enter the second number..")
temp=a;a=b;b=temp;
print "After Swapping..",a,b
print "########################################"


'''  Program 7  '''
print "Program 7--> Swapping two numbers without using temp variable"
a,b=input("Enter the first number.."),input("Enter the second number..")
a,b=b,a
print "After Swapping..",a,b
print "########################################"


'''  Program 8  '''
print "Program 8--> Simple Interest"
print input("Enter the Principal amount..")*input("Enter the Rate of interest..")*input("Enter the no. of years.."),"is the SI.."
print "########################################"


'''  Program 9  '''
print "Program 9--> Compound Interest"
n=input("Number of times the amount is compunded every year..")
print input("Enter the Principal Amount..")*pow((1+(input("Enter the rate of interest")/float(n))),input("No. of times the amount is deposited or borowed for..")*n)
print "########################################"


'''  Program 10  '''
print "Program 10--> Power of the given number"
print input("Enter the number..")**input("Enter the power to be raised.."),"is the Result.."
print "########################################"


'''  Program 12  '''
print "Program 12--> Leap Year or not"
from calendar import isleap
print "Leap Year" if isleap(input("Enter the year..")) else "Not Leap Year"
print "########################################"


'''  Program 13  '''
print "Program 13--> Odd or even"
print "Even" if input("Enter the number..")%2==0 else "Odd"
print "########################################"


'''  Program 14  '''
print "Program 14--> positive or negative"
print "Positive" if input("Enter the number..")>0 else "Negative"
print "########################################"


'''  Program 15  '''
print "Program 15--> Ascending order of three nos"
print sorted([input("Enter num1"),input("Enter num2"),input("Enter num3")]),"is the Ascending order of three numbers"
print "########################################"


'''  Program 16  '''
print "Program 16--> Triangle is valid or not"
print "Valid" if sum([input("Enter first angle.."),input("Enter second angle.."),input("Enter third angle..")])<=180 else "Not Valid"
print "########################################"


'''  Program 17  '''
print "Program 17--> Cost per unit"
print input("No of units..")*input("Cost per unit.."),"is the required Cost"
print "########################################"


'''  Program 18  '''
print "Program 18--> Grades of students based on average"
avg=int(sum([input("Maths mark.."),input("Tamil mark.."),input("English mark.."),input("Science mark.."),input("Social-Sci mark..")])/5)
R=xrange
grade={"S":R(90,100),"A":R(80,90),"B":R(70,80),"C":R(60,70),"D":R(55,60),"E":R(50,55),"U":R(0,50)}
print [i for i,j in grade.items() if avg in grade[i]][0],"Grade"
print "########################################"


'''  Program 19  '''
print "Program 19--> Max and min of given nos"
nos=input("Enter the numbers in list([,,,])")
print "Max is",max(nos),"& Min is",min(nos)
print "########################################"


'''  Program 20  '''
print "Program 20 --> Print String"
print '"Printed.."'
print "########################################"


'''  Program 21  '''
print "Program 21--> Length of the given string"
print len(raw_input("Enter the String..")),"is the length of the given String"
print "########################################"


'''  Program 22  '''
print "Program 22--> Copying the string"
str1=str2=raw_input("Enter the String..")
print "Printing from the Copied Variable..",str2
print "########################################"


'''  Program 23 '''
print "Program 23--> Comparision of two strings"
print "Both are same" if raw_input("Enter the First one..")==raw_input("Enter the Second one..") else "Both are not same"
print "########################################"


'''  Program 24 '''
print "Program 24--> Lower and upper functions"
str1=raw_input("Enter the String..")
print "In lower..",str1.lower(),"In Upper..",str1.upper()
print "########################################"


'''  Program 25  '''
print "Program 25--> Sorting Strings"
print sorted(input("Enter the Strings..['','','']"))," is the sorted form"
print "########################################"


'''  Program 26  '''
print "Program 26--> Reversing String"
print raw_input("Enter the String..")[::-1],"is the revresed form"
print "########################################"


'''  Program 27  '''
print "Program 27--> Vowels,Consonants,digits"
from re import sub
str1=sub("\s","",raw_input("Enter the string..").lower())
print "Vowels:",len(sub("[^aeiou]","",str1)),"Consonants:",len(sub("[aeiou]","",str1)),"Digits:",len(sub("\D","",str1))
print "########################################"


'''  Program 28  '''
print "Program 28--> Frequency of characters"
from collections import Counter
print Counter(raw_input("Enter the String..")).items(),"is the Frequency of characters"
print "########################################"


'''  Program 29  '''
print "Program 29--> Palindrome or not"
str1=raw_input("Enter the String..")
print "Palindrome" if str1==str1[::-1] else "Not Palindrome"
print "########################################"


'''  Program 30  '''
print "Program 30--> Deleting Vowels in a String"
from re import sub
print sub("[aeiou]","",raw_input("Enter the string..")),"..- After Deletion"
print "########################################"


'''  Program 31  '''
print "Program 31--> Sorting characters in a string"
print "".join(sorted(list(raw_input("Enter the String..")))),"is the sorted order"
print "########################################"


'''  Program 32  '''
print "Program 32--> Number of words,Lines and Characters"
str1=raw_input("Enter the String(lines with .)..")
print "Words:",len(str1.split()),"Lines:",len(str1.split('.')),"Characters:",len(str1)
print "########################################"


'''  Program 33  '''
print "Program 33--> Concatenate Two Strings"
print raw_input("Enter the first one..")+raw_input("Enter the second one.."),"..-Concatenated"
print "########################################"


'''  Program 34  '''
print "Program 34--> Factorial of a number(Function)"
from math import factorial
print factorial(input("Enter the number")),"is the factorial of given number"
print "########################################"


'''  Program 35  '''
print "Program 35-->Finding Area of triangle(Function)"
Area=lambda b,h:0.5*b*h
print Area(input("Enter the Breadth.."),input("Enter the Height.."))
print "########################################"


'''  Program 36  '''
print "Program 36--> Sum the Fibonacci Series(Function)"
fib=[0,1]
for i in xrange(2,input("Enter the range..")):fib.append(fib[-1]+fib[-2])
print "Sum of fibonacci series is",sum(fib)
print "########################################"


'''  Program 37 '''
print "Program 37--> Sum of n nos(Function)"
print sum(input("Enter the nos..[,,]..")),"is the sum of given numbers"
print "########################################"


'''  Program 38  '''
print "Program 38--> Sum of digits(Function)"
print sum(map(int,raw_input("Enter the number.."))),"is the sum of digits of the given number"
print "########################################"


'''  Program 39  '''
print "Program 39--> 7 is present or not(Function)"
print '7' in raw_input("Enter the number..")
print "########################################"


'''  Program 40  '''
print "Program 40--> Odd or Even(Function)"
odd_even=lambda n:"Even" if n%2==0 else "Odd"
print odd_even(input("Enter the number.."))
print "########################################"


'''  Program 41  '''
print "Program 41--> Days of the Week"
from calendar import day_name
print day_name[input("Enter the day of week(1-7)..")-1],"is the day of the week"
print "########################################"


'''  Program 42  '''
print "Program 42--> Printing the array"
print [1,2,3,"vaasu","devan"],"..- Array Printed"
print "########################################"


'''  Program 43  '''
print "Program 43--> Sum of Squares of array elements"
print [i*i for i in input("Enter the nos ([,,,])..")]
print "########################################"


'''  Program 44  '''
print "Program 44--> Reversing the given array"
print list(reversed(input("Enter the array([,,,]).."))),"is the reversed order"
print "########################################"


'''  Program 45  '''
print "Program 45--> Middle value of array"
array=input("Enter the nos.([,,,])..")
print "The middle value of given array is",array[len(array)/2]
print "########################################"


'''  Program 46  '''
print "Program 46--> Position of biggest element in an array"
array=input("Enter the nos.([,,,])..")
print "The position of biggest element in the given array is..",array.index(max(array))
print "########################################"


'''  Program 47  '''
print "Program --> Insert an element in an array"
array=input("Enter the nos.([,,,])..");array.insert(input("Enter the Position.."),input("Enter the element.."))
print "After Insertion..",array
print "########################################"


'''  Program 48  '''
print "Program 48--> Delete an element in an array"
array=input("Enter the nos.([,,,])..");array.remove(input("Enter the element to delete.."))
print "After Deletion..",array
print "########################################"


'''  Program 49  '''
print "Program 49--> Merge two arrays"
print input("Enter the first one.([,,,])..")+input("Enter the second one.([,,,]).."),"..-After merging process"
print "########################################"


'''  Program 50  '''
print "Program 50--> Array in Ascending order"
print sorted(input("Enter the array.([,,,])..")),"is the sorted order"
print "########################################"


'''  Program 51  '''
print "Program 51--> Finding the position of given element"
print input("Enter the array.([,,,])..").index(input("Enter the number to find..")),"is the position"
print "########################################"


'''  Program 52  '''
print "Program 52--> Similar elements and counting them"
from collections import Counter
print list(Counter(input("Enter the array.([,,,])..")).items()),"...[(number, count)]"
print "########################################"


'''  Program 53  '''
print "Program 53--> Sum of Sine Series"
from math import sin
print sin(input("Enter the value..")),"is the sine value"
print "########################################"


'''  Program 54  '''
print "Program 54--> Two table"
for i in xrange(1,11):print '2X'+str(i)+"="+str(2*i)
print "########################################"


'''  Program 55  '''
print "Program --> Armstrong or not"
num=input("Enter the number..")
print "Armstrong Number" if num==sum(map(lambda n:n**3,map(int,str(num)))) else "Not an Armstrong Number"
print "########################################"


'''  Program 56  '''
print "Program 56--> Generation of Armstrong numbers"
A=lambda num:num==sum(map(lambda n:n**3,map(int,str(num))))
print [i for i in xrange(input("Start.."),input("End..")) if A(i)],"is(are) the Armstrong numbers within the given range"
print "########################################"


'''  Program 57  '''
print "Program --> Square of the given number"
print input("Enter the number..")**2,"is the Squared value of the given number"
print "########################################"


'''  Program 58  '''
print "Program 58--> Power of the given number"
print pow(input("Enter the number.."),input("Enter the value to be raised..")),"is the powered value"
print "########################################"


'''  Program 59  '''
print "Program 59--> Krishnamoorthy number"
from math import factorial as F
num=input("Enter the number..")
print "Krishnamoorthy Number" if num==sum(map(lambda n:F(n),map(int,str(num)))) else "Not a Krishnamoorthy Number"
print "########################################"


'''  Program 60  '''
print "Program 60--> Generation of Krishnamoorthy numbers"
from math import factorial as F
A=lambda num:num==sum(map(lambda n:F(n),map(int,str(num))))
print [i for i in xrange(input("Start.."),input("End..")) if A(i)],"is(are) the Krishnamoorthy numbers within the given range"
print "########################################"


'''  Program 61  '''
print "Program 61--> Patterns"
x=xrange
n=input("Enter the size (common for all patterns)..")

print "Right Angled Triangle-Left Side"
for i in x(n):
    for j in x(i+1):print '*',
    print
    
print "Right Angled Triangle-Right Side"
for i in x(n):
    for k in x(n,i+1,-1):print " ",
    for j in x(i+1):print '*',
    print 
    
print "Floyd's triangle"
k=1
for i in x(1,n+1):
    for j in x(i):
        print k,
        k+=1
    print
    
print "Right Angled Triangle-Decrementing Order"
for i in x(n,0,-1):print '*'*i
print "########################################"


'''  Program 62  '''
print "Program 62--> Hollow Box"
n=input("Enter the size of box..")
from time import sleep
x=xrange
for i in x(n):
    for j in x(n):
        if i==0 or i==n-1 or j==0 or j==n-1:print '*',
        else:print " ",
    print
    sleep(0.08)
print "########################################"


'''  Program 63  '''
print "Program 63--> Matrix Operations (+,-)"
x,r=xrange,range
row,col=input("Enter the no. of rows.."),input("Enter the no. of columns..")
matrix1=[r(col) for i in x(row)]
matrix2=[r(col) for i in x(row)]
add=[r(col) for i in x(row)]
sub=[r(col) for i in x(row)]
print "Enter the",row*col,"elements for Matrix A"
for i in x(row):
    for j in x(col):
        matrix1[i][j]=input("Enter the element for["+str(i)+"]["+str(j)+"] ")
print "Enter the",row*col,"elements for Matrix B"
for i in x(row):
    for j in x(col):
        matrix2[i][j]=input("Enter the element for["+str(i)+"]["+str(j)+"] ")
for i in x(row):
    for j in x(col):
        add[i][j]=matrix1[i][j]+matrix2[i][j]
        sub[i][j]=matrix1[i][j]-matrix2[i][j]
print "The sum of two matrices is.."
for i in add:print i
print "The Difference between two matrices is.."
for i in sub:print i
print "########################################"


'''  Program 64  '''
print "Program --> Matrix Multiplication"
x,r=xrange,range
row1,col1=input("Enter the no. of rows for matA.."),input("Enter the no. of columns for matA..")
row2,col2=input("Enter the no. of rows for matB.."),input("Enter the no. of columns for matB..")
if col1!=row2:print "Multiplication is not Possible."
else:
    a=[r(col1) for i in x(row1)]
    b=[r(col2) for i in x(row2)]    
    c=[r(col2) for i in x(row1)]
    print "Enter the",col1*row1,"elements for Matrix A"
    for i in x(row1):
        for j in x(col1):
            a[i][j]=input("Enter the element for["+str(i)+"]["+str(j)+"] ")
    print "Enter the",row2*col2,"elements for Matrix B"
    for i in x(row2):
        for j in x(col2):
            b[i][j]=input("Enter the element for["+str(i)+"]["+str(j)+"] ")  
    for i in x(row1):
        for j in x(col2):
            c[i][j]=0
            for k in x(col1):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    print "The Product is.."
    for i in c:print i        
print "########################################"


'''  Program 65  '''
print "Program 65--> Printing Statement 10 times"
for i in xrange(10):print "I love Python Programming"
print "########################################"


'''  Program 66  '''
print "Program 66--> Printing Statement n times"
for i in xrange(input("Enter the no. of times..")):print "I love Python Programming"
print "########################################"


'''  Program 67  '''
print "Program 67--> Stars in a row"
print '*'*input("Enter the no.of times..")
print "########################################"


'''  Program 68  '''
print "Program 68--> Prime Series upto n"
x=xrange
P=lambda n:all(n%i for i in x(2,n))
print [i for i in x(2,input("Enter the limit..")+1) if P(i)]
print "########################################"


'''  Program 69  '''
print "Program 69--> n Prime numbers"
x,i,j,Prime=xrange,2,0,[]
P=lambda n:all(n%i for i in x(2,n))
n=input("Enter how many numbers..")
while j!=n:
    if P(i):Prime.append(i);j+=1
    i+=1
print Prime
print "########################################"


'''  Program 70  '''
print "Program 70--> Numbers divisible by 7"
print filter(lambda i:i%7==0,xrange(1,input("Enter the limit..")))
print "########################################"


'''  Program 71  '''
print "Program 71--> Odd/Even Series upto n"
n=input("Enter the limit..")
x=xrange
print "Odd Series..",filter(lambda i:i%2!=0,x(1,n)),"Even Series..",filter(lambda i:i%2==0,x(1,n))
print "########################################"


'''  Program 72  '''
print "Program 72--> Sum of Odd/Even Series upto n (Input from Program 71)"
print "Sum of Odd Series:",sum(filter(lambda i:i%2!=0,x(1,n))),"Sum of Even Series:",sum(filter(lambda i:i%2==0,x(1,n)))
print "########################################"


'''  Program 73  '''
print "Program 73--> Sum of Series 1/3 + 2/5 + 3/7 +.... + n terms"
x,ans,j=xrange,0,3
for i in xrange(1,input("Enter the limit..")+1):ans+=float(i)/j;j+=2
print "The sum of the series is..",ans
print "########################################"


'''  Program 74  '''
print "Program 74--> Sum of Series x+ x**2+ x**3 +... n terms"
x,n=input("Enter the number.."),input("Enter the number of terms..")
print sum([x**i for i in xrange(1,n+1)]),"is the sum of the series"
print "########################################"


'''  Program 75  '''
print "Program 75-->Sum of Series 1/1 + 1/2 + 1/3 +.... + 1/n"
print sum([1.0/i for i in xrange(1,input("Enter the limit..")+1)]),"is the sum of the series"
print "########################################"


'''  Program 76  '''
print "Program 76--> Palindrome Series.."
print [i for i in xrange(input("Start..: "),input("End..: ")+1) if str(i)==str(i)[::-1]],"is the Palindrome Series"
print "########################################"


''' Program 77  '''
print "Program 77--> Pascal's Triangle (Through nck... n!/(k!*(n-k)!)"
x=xrange
from math import factorial as F
n=input("Enter the number..")
for i in x(n):
    for j in x(n-i-1):print " ",
    for k in x(i+1):print str(F(i)/(F(k)*F(i-k)))+"  ",
    print 
print "########################################"


'''  Program 78  '''
print "Program 78--> Two Way Multiplication Table.."
R=range
n=input("Enter the size..")
for i in R(1,n+1):print [i*j for j in R(1,n+1)]
print "########################################"
