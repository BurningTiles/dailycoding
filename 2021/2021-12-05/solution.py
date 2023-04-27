def constructRectangle(area):
	s = int(area**(.5))
	while s>1 and area%s!=0:
		s -= 1
	return [area//s, s]

print(constructRectangle(4))
print(constructRectangle(37))
print(constructRectangle(122122))