# Question: Almost equivalent strings

class Solution:

	def AlmostEquivalent(self, s,t ):
		n = len(s)
		res = []
		for i in range(n):
			string1, string2 = s[i], t[i]
			if self.is_equivalent (string1, string2):
				res.append(‘Yes’)
			else:
				res.append(‘No’)
		return res

	def is_equivalent(self, s1, s2):
		if s1 == s2:
			return True
		if len(s1) != len(s2):
			return False
		n = len(s1)
		count1, count2 = self.count(s1), self.count(s2)
		for s in count1.keys():
			if s in count2:
				if abs(count2[s] – count1[s])>3:
					return False
				else:
					del count2[s]
					continue
			else:
				if count1[s] > 3:
					return False
				else:
					continue
		for s in count2.keys():
			if count2[s] > 3:
				return False

		return True

	def count(self, s):
		count = {}
		for i in s:
			count[i] = count.get(i, 0) + 1
		return count
