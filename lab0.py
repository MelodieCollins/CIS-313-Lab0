import math
class mathOps:
	
	def __init__(self, u, v):
		self.u = u
		self.v = v
	
	def __repr__(self):
		return "LeastCommonMultiple({}, {})".format(self.u, self.v)
	
	def __str__(self):
		return "GreatestCommonDivisor({}, {}).".format(self.u, self.v)
	
	def valid(self):
		return isinstance(self.u, int) and isinstance(self.v, int)
	
	def gcd(self):
		# Find the greatest common divisor of a and b
		tempU = self.u
		tempV = self.v

		try:
			# Check for infinity
			if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
				raise OverflowError
			# Check for strings
			if type(tempU) == str or type(tempV) == str:
				raise TypeError
			
			# Set ceiling value and absolute value of numbers 
			tempU = math.ceil(abs(tempU))
			tempV = math.ceil(abs(tempV))

			# GCD of 0 and any number is the number
			# GCD of 0 and 0 is 0
			if tempU == 0:
				return tempV
			if tempV == 0:
				return tempU
			# GCD of any two same numbers is the number
			if tempU == tempV:
				return tempU

			# Find GCD
			else:
				while(tempU != tempV):
					if tempU > tempV:
						tempU = tempU - tempV
						gcd = tempU
					else:
						tempV = tempV - tempU
						gcd = tempV
				return gcd

		except OverflowError:
			print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
			raise OverflowError

		except TypeError:
			print("one or both of", tempU, " and ", tempV, "have type string")
			raise TypeError

	def lcm(self):
		# Find the least common multiple of a and b
		try:
			# Set ceiling value and absolute value of numbers
			tempU = math.ceil(abs(self.u))
			tempV = math.ceil(abs(self.v))
			# Check for infinity
			if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
				raise OverflowError
			# Check for 0s
			if tempU == 0 or tempV == 0:
				raise ValueError
			# Check for strings
			if type(tempU) == str or type(tempV) == str:
				raise TypeError

			# Find LCM
			else:
				return (tempU*tempV)/mathOps.gcd(self)

		except OverflowError:
			print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
			raise OverflowError
		except ValueError:
			print("one or both the values are 0. Lcm of 0 and any number is undefined")
			raise ValueError
		except TypeError:
			print("one or both of", tempU, " and ", tempV, "have type string")
			raise TypeError
