# Problem Set 4

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each
	  year (an integer between 0 and 100).
	- growthRate: the annual percent increase in your investment account (an
	  integer between 0 and 100).
	- years: the number of years to work.
	- return: a list whose values are the size of your retirement account at
	  the end of each year.
	"""
	fund = []
	for i in range(0, years):
		if i == 0:
			fund.append(salary * save * 0.01)
		else:
			fund.append(fund[i-1] * (1 + 0.01 * growthRate) + salary * save * 0.01)
	return fund
	
def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    salary     = 30000
    save       = 10
    growthRate = 9
    years      = 15
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    
    salary     = 55000
    save       = 15
    growthRate = 9
    years      = 15
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each
	  year (an integer between 0 and 100).
	- growthRate: a list of the annual percent increases in your investment
	  account (integers between 0 and 100).
	- return: a list of your retirement account value at the end of each year.
	"""
	fund = []
	for i in range(0, len(growthRates)):
		if i == 0:
			fund.append(salary * save * 0.01)
		else:
			fund.append(fund[i-1] * (1 + 0.01 * growthRates[i]) + salary * save * 0.01)
	return fund

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]
    # TODO: Add more test cases here.
    salary      = 36000
    save        = 15
    growthRates = [1, 2, 2, 3, 4]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)

    salary      = 100000
    save        = 15
    growthRates = [1, 2, 2, 3, 4]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
	"""
	- savings: the initial amount of money in your savings account.
	- growthRate: a list of the annual percent increases in your investment
	  account (an integer between 0 and 100).
	- expenses: the amount of money you plan to spend each year during
	  retirement.
	- return: a list of your retirement account value at the end of each year.
	"""
	fund = []
	for i in range(0, len(growthRates)):
		if i == 0:
			fund.append(savings+(savings*(growthRates[i]*0.01)-expenses))
		else:
			fund.append(fund[i-1]+(fund[i-1]*(growthRates[i]*0.01)-expenses))
	return fund

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    savings     = 78000
    growthRates = [3, 5, 0, 5, 1]
    expenses    = 20000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)

    savings     = 162000
    growthRates = [0, 9, 5, 12, 6]
    expenses    = 20000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each
	  year (an integer between 0 and 100).
	- preRetireGrowthRates: a list of annual growth percentages on investments
	  while you are still working.
	- postRetireGrowthRates: a list of annual growth percentages on investments
	  while you are retired.
	- epsilon: an upper bound on the absolute value of the amount remaining in
	  the investment fund at the end of retirement.
	"""
	fund = nestEggVariable(salary, save, preRetireGrowthRates)
	# print("nest egg", fund)
	savings = fund[len(fund)-1]
	print("")
	print("savings: ", savings)
	low = 0
	high = savings
	guess = (low+high)/2.0
	testexpenses = postRetirement(savings, postRetireGrowthRates, guess)
	# print("guess: ", guess, testexpenses)
	finalworth = testexpenses[len(testexpenses)-1]
	while finalworth < 0 or finalworth > epsilon: 
		if finalworth < 0:
			high = guess
		if finalworth > epsilon:
			low = guess 
		guess = (low+high)/2.0
		testexpenses = postRetirement(savings, postRetireGrowthRates, guess)
		# print("guess: ", guess, testexpenses[len(testexpenses)-1])
		finalworth = testexpenses[len(testexpenses)-1]
	return guess
			
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(f'Max expenses per year for {len(postRetireGrowthRates)} years: ', expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    salary                = 55000
    save                  = 15
    preRetireGrowthRates  = [3, 4, 5, 0, 3, 3, 4, 5, 0, 3, 3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1,10, 5, 0, 5, 1,10, 5, 0, 5, 1,10, 5, 0, 5, 1,10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(f'Max expenses for {len(postRetireGrowthRates)} years of savings', expenses)

    
###########################################################
#	                        Tests
###########################################################

print("")
print("######################")
print("Nest Egg Fixed")
testNestEggFixed()
print("######################")

print("")
print("######################")
print("Nest Egg Variable")
testNestEggVariable()
print("######################")

print("")
print("######################")
print("Post Retirement")
testPostRetirement()
print("######################")

print("")
print("######################")
print("Find Max Expenses")
testFindMaxExpenses()
print("######################")
