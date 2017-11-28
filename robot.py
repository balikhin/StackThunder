############################################################
#This robot performs simple stack classification without ML#
############################################################

SUSPICIOUS = 1
CLEAN = 0
UNCERTAIN = -1

# Library import
import pandas as pd

def NaPosition(stack):
	na_string = 'n/a'
	na_positions = []
	stack_size = stack.size
	for i in range (stack_size - 1):
		if (stack[i] == na_string):
			na_positions.append(i)
	return na_positions

def AnalyseStack(stack, na_positions, whitelist):
	stack_size = stack.size
	whitelist_size = len(whitelist)
	na_count = len(na_positions)
	decision = UNCERTAIN
	for i in range(na_count):
		for j in range(whitelist_size):
			if ((i > 0) and (stack[i - 1] == whitelist[j])):
					print('I am here')
					break
					#j = whitelist_size
			if ((i < stack_size - 1) and (stack[i + 1] == whitelist[j])):
					print('I am here(frame after)')
					break
					#j = whitelist_size

		# IsInWhitelist(frame_before)
		# IsInWhitelist(frame_after)
	return 1

# Data load
stacks = pd.read_csv("Stacks.csv")
print(stacks.head(5))
whitelist = ['opera_browser.dll', 'atcuf64.dll']

# Positioning n_a frames in the first stack
na_positions = NaPosition(stacks.iloc[0])

# Processing those n_a frames
decision = AnalyseStack(stacks.iloc[0], na_positions, whitelist)

# Print the decision
print(decision)