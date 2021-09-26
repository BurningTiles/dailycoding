def intersection(list1, list2, list3):
	i,j,k = 0,0,0
	ans = []
	while i<len(list1) and j<len(list2) and k<len(list3):
		if list1[i]==list2[j]==list3[k]:
			ans.append(list1[i])
			i += 1
			j += 1
			k += 1
		elif list1[i]<list2[j]:
			i += 1
		elif list2[j]<list3[k]:
			j += 1
		else:
			k += 1
	return ans
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))