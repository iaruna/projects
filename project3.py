# python code to train pokemon
''' Input : 
The single line describing powers of N Pokémon caught. 

Output : 
N lines stating minimum power so far and maximum power so far separated by single space '''
powers = [3, 5, 9, 12]

mini, maxi = 0, 0

for power in powers:
	if mini == 0 and maxi == 0:
		mini, maxi = powers[0], powers[0]
		print(mini, maxi)
	else:
		mini = min(mini, power)
		maxi = max(maxi, power)
		print(mini, maxi)
		
# Time Complexity is O(N) with Space Complexity O(1)
