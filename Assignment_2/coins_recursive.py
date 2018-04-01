
def findMinCoins(S, n, N):
	# if total is 0, no coins are needed
	if (N == 0):
		return 0
	
	# return INFINITY if total become negative
	if (N < 0):
		return float('inf')
	
	# initalize minimum number of coins needed to infinity
	coins = float('inf')
	
	# do for each coin
	for i in range(0, n):
		# recuse to see if total can be reached by including
		# current coin S[i]
		res = findMinCoins(S, n, N - S[i])
	
		# update minimum number of coins needed if choosing current 
		# coin resulted in solution
		if (res != float('inf')):
			coins = min(coins, res + 1)
	
	# return minimum number of coins needed
	return coins

def main():
	# n coins of given denominations
	S = [ 1, 3, 5, 7 ];
	n = len(S);

	# Total Change required
	N = 18;

	print ("Minimum number of coins required to get desired change is " + str(findMinCoins(S, n, N)))

	return 0


if __name__ == "__main__":
	main()
