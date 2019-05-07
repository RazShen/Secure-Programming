

# Last modified: 2 May 2019

# you don't have to use the packages below, it is only a suggestion. 
# do not use any other python module unless it is explicitly permitted by the instructor.
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import Crypto.Cipher.AES as AES


class Cloud:
	"""
	the cloud stores your content encrypted.
	you can add variables and methods to this class as you want.
	"""
	def __init__(self, filename, key=get_random_bytes(32), nonce=get_random_bytes(8)):
		"""
		Encrypt the content of 'filename' and store its ciphertext at self.ciphertext
		The encryption to use here is AES-CTR with 32 byte key.
		The counter should begin with zero.
		"""
		self.__key = key
		self.__nonce = nonce
		self.__fn = filename
		
		with open(self.__fn, mode='rb') as file:
			self.__pt = file.read()
		self.aes_encrypt()
	
	def aes_encrypt(self):
		countf = Counter.new(64, self.__nonce)
		crypto = AES.new(self.__key, AES.MODE_CTR, counter=countf)
		self.__ct = crypto.encrypt(self.__pt)
	def Length(self):
		"""
		Returns the length of the plaintext/ciphertext (they are of the same length).
		This is necessary so one would not read/write with an invalid position.
		"""
		return len(self.__ct)

	def Read(self, position=0):
		"""
		Returns one byte at 'position' from current self.ciphertext. 
		position=0 returns the first byte of the ciphertext.
		"""
		return self.__ct[position]

	def Write(self, position=0, newbyte='\x33'):
		"""
		Replace the byte in 'position' from self.ciphertext with the encryption of 'newbyte'.
		Remember that you should encrypt 'newbyte' under the appropriate key (it depends on the position).
		Return the previous byte from self.ciphertext (before the re-write).
		"""

		if position >= len(self.__ct):
			return None
		pt_as_list = list(self.__pt)
		pt_as_list[position] = newbyte
		self.__pt = "".join(pt_as_list)
		old_byte = self.Read(position)
		self.aes_encrypt()
		return old_byte
		


