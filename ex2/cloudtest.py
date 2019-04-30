

from cloud import *
from breakcloud import *

def testcloud():
	#testing your cloud functionality:
	cloud = new Cloud('what.txt')
	r1 = cloud.Read(10) # r1 = '\xb1'
	r2 = cloud.Read(20) # r2 = '\x41'
	v = '\x10'
	pos = 5
	r3 = cloud.Write(pos, v) # r3 = '\xc5'
	r4 = cloud.Read(5) # r4 = '\xbc'
	if r1 == '\xb1' and r2 == '\x41' and r3 == '\xc5' and r4 = '\xbc':
		print "success!"
	else:
		print "failed..."

def testbreaker():
	testfile = 'what.txt'
	cloud = new Cloud(testfile)
	breakcloud(cloud)

	with open(testfile, mode='rb') as file:
		originalcontent = file.read()
		file.close()
		with open('plain.txt', mode='rb') as breakerresult:
			breakercontent = breakerresult.read()
			breakerresult.close()

			if originalcontent == breakercontent:
				print "success!"
				exit()
	print "failed..."


def main():
	testcloud()
	testbreaker()


if __name__ == '__main__':
	main()



