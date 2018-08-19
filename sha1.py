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
x = """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""
print(hex(s(x)))