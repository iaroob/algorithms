def solve(s:"IList"):
	c=[]

	c.append((s[0],s[0]+1))
	valor=s[0]+1
	for i in range(1,len(s)):
		if s[i]> valor:

			c.append((s[i],s[i]+1))
			valor=s[i]+1
	return c

S=[1,1.3,1.4,2.2,3,7,7.2]
print(solve(S))