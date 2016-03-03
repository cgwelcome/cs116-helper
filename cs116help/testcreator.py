import sys
from io import StringIO
from functools import wraps

# Print out the returned value of the function as "check.expect()"
def check_expect(function,index):		
	@wraps(function)
	def wrapper(*args):
		func_name = function.__name__
		func_contents = function(*args)
		arguments = ','.join([repr(x) for x in args])
		info = [index,func_name,arguments,func_contents]
		print("check.expect(\"t{0}\",{1}({2}),{3})".format(*info))
	return wrapper

# A decorator that captures the standard output stream, and print out
# the stdout in the check.set_screen_format
def check_set(function):
	@wraps(function)
	def wrapper(*args):
		back_stdout = sys.stdout
		screen_output = StringIO()
		sys.stdout = screen_output

		func_content = function(*args)
	
		sys.stdout = back_stdout
		screen_contents = screen_output.getvalue()
		screen_output.close()

		if screen_contents:
			sys.stdout.write('\n')	
			screen_contents = repr(screen_contents.strip('\n'))
			print("check.set_screen({0})".format(screen_contents))
		return func_content		

	return wrapper

			
# Setup the data to be tested 

def test(module,string_function,data_test_lst):
	mod = __import__(module)
	function = getattr(mod,string_function)
	set_function = check_set(function)
	print(repr(data_test_lst))
	for index,t_item in enumerate(data_test_lst,1):
		check_expect(set_function,index)(*t_item)
	
test("a05q1","tomorrow",[["Monday"],["tuesday"],["wEDNESDAY"],["THURSDAY"],["fRiDaY"],["SAturday"],["SUNDaY"],[""],["Random"],["3243"],["!@!@#"]])
#import string
#testlist1 = [x+str(y) for x in string.ascii_uppercase[:8] for y in [1,8]]
#testlist2 = [x+str(y) for x in string.ascii.uppercase[:8] for y in range(1,8)]
#test("a05q2","check_by_queen",[["A1","E2"],["B1","A1"]])

#test("a05q1","tomorrow",[["Monday"]])
