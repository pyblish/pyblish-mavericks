import sys

while True:
	sys.stdout.write("> ")

	msg = raw_input()
	if msg == "quit":
		print "Good Bye"
		sys.exit()
	print "Hello %s!" % msg