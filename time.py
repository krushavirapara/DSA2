import time

#to get epoch

print(time.gmtime(0))

#to get currnt time in floating number
print(time.time())

#to get cuurent time in string
print(time.ctime(time.time()))

#to get  current loacttime
print(time.localtime()) #RETURN struct_time_object

#to get uct time
print(time.gmtime()) #RETURN struct_time_object

#to get string from struct_time
print(time.asctime(time.localtime()))

#to format the string as per our needs
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%A,%d-%B-%Y", named_tuple)
print(time_string)

#to get struct_time from string
print(time.strptime(time_string,"%A,%d-%B-%Y"))

#to sleep
time.sleep(3)

#to measure performance
def fun(n):
	for i in range(100):
		print(i)

start = time.perf_counter()
fun(4)
end=time.perf_counter()
print(end-start)