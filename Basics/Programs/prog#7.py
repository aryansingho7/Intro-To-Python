## Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.

start = 11
end = 25
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


