import inspect
class sha:
	def __init__(self):
		self.mask = 2**self.word_length - 1

	def __call__(self, s):
		return self.digest(s)

	def rotl(self, x, n):
		return ((x << n) | (x >> (self.word_length - n))) & self.mask

	def rotr(self, x, n):
		return ((x >> n) | (x << (self.word_length - n))) & self.mask

	def shr(self, x, n):
		return (x >> n) & self.mask

	def ch(self, x, y, z):
		return (x & y) ^ ((~x) & z)

	def maj(self, x, y, z):
		return (x & y) ^ (x & z) ^ (y & z)

	def parity(self, x, y, z):
		return x ^ y ^ z

	def pad(self, m):
		n = sum(c << 8*(len(m)-i-1) for i, c in enumerate(map(ord, m)))
		n <<= 1
		n += 1
		k = 0
		while (len(m)*8 + 1 + k) % (self.word_length*16):
			k += 1
		n <<= k
		n += len(m)*8
		return n
		return pad

	def parse(self, m, n):
		s = []
		while m:
			s.insert(0, m & ((1 << n) - 1))
			m >>= n
		return s