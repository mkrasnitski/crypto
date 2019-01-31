import sys
from sha import sha
class sha1(sha):
	word_length = 32

	# CONSTANTS

	K = [0x5a827999]*20 + [0x6ed9eba1]*20 + [0x8f1bbcdc]*20 + [0xca62c1d6]*20
	H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

	# FUNCS

	def f(self, t, x, y, z):
		if t < 20:
			return self.ch(x, y, z)
		elif t < 40:
			return self.parity(x, y, z)
		elif t < 60:
			return self.maj(x, y, z)
		elif t < 80:
			return self.parity(x, y, z)

	# DIGESTION

	def digest(self, p):
		m = self.parse(self.pad(p), 512)
		for b in m:
			W = self.parse(b, 32)
			for t in range(16, 80):
				W.append(self.rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1))

			a, b, c, d, e = self.H
			for t in range(80):
				T = (self.rotl(a, 5) + self.f(t, b, c, d) + e + self.K[t] + W[t]) & self.mask
				a, b, c, d, e = T, a, self.rotl(b, 30), c, d
				# print(a, b, c, d, e)

			n = [a, b, c, d, e]
			for t in range(len(self.H)):
				self.H[t] += n[t]
				self.H[t] &= self.mask

		d = sum(c << 32*(len(self.H)-i-1) for i, c in enumerate(self.H))
		return d

s = sha1()
x = sys.argv[1]
print(hex(s(x)))