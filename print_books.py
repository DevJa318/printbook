import sys


ilosc_stron = int(sys.argv[1])
if ilosc_stron%4 == 0:
	pod4 = ilosc_stron
else:
	mod4 = 4-ilosc_stron%4
	pod4 = ilosc_stron+mod4

x = [i+1 for i in range(pod4)]

stronytyl = len(x)-1
stronyprzod = 0

dountil = int(len(x)/4)

print("Część pierwsza: ", end='')
for i in range(dountil):
	print(x[stronytyl], end=', ')
	print(x[stronyprzod], end=', ')
	stronytyl = stronytyl - 2
	stronyprzod = stronyprzod + 2

stronyprzod = int(len(x)/2-1)
stronytyl = int(len(x)/2)
print("\nCzęść druga: ", end='')
for i in range(dountil):
	print(x[stronyprzod], end=', ')
	print(x[stronytyl], end=', ')
	stronyprzod = stronyprzod - 2
	stronytyl = stronytyl + 2 
print()