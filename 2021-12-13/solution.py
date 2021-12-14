def findRestaurant(l1, l2):
	ans, least, tmp = [], len(l1)+len(l2), 0
	m1, m2 = dict(), dict()
	for i in range(len(l1)):
		m1[l1[i]] = i+1
	for i in range(len(l2)):
		m2[l2[i]] = i+1
	for s in l1:
		if s in m2:
			tmp = m1[s] + m2[s]
			if tmp<least:
				least = tmp
				ans = [s]
			elif tmp==least:
				ans.append(s)
	return ans

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))