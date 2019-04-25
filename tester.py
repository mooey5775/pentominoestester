import subprocess
from tqdm import tqdm
import time
import argparse
import pickle
import sys
from collections import deque

ap = argparse.ArgumentParser()
ap.add_argument('program', help='path to pentominoes solver')
ap.add_argument('-t', '--testcases', default='testcases.pickle', help='custom path to testcases pickle file')
args = vars(ap.parse_args())

good = True

def prompt():
	(input('Continue or exit [C/e]? ') == 'e') and sys.exit()

def rotate(a):
	w = len(a)
	h = len(a[0])
	b = [[0]*w for i in range(h)]
	for y in range(h):
		for x in range(w):
			b[y][w-x-1] = a[x][y]
	return b

def flip(a):
	w = len(a)
	h = len(a[0])
	b = [[0]*h for i in range(w)]
	for y in range(h):
		for x in range(w):
			b[w-x-1][y] = a[x][y]
	return b

def convertTo2D(a, h, w):
	b = [[0]*h for i in range(w)]
	for i, j in enumerate(a):
		b[i%w][i//w] = j
	return b

def c1(a):
	return tuple([i for s in zip(*a) for i in s])

print('[INFO] loading testcases...')
tc = pickle.load(open(args['testcases'], 'rb'))

print('[INFO] will test', len(tc), 'test cases')
totalTime = 0
for x, n, y in tqdm(tc):
	h, w = (int(i) for i in x.split('\n')[-1].split())
	p = subprocess.Popen([args['program']], stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf8')
	start = time.time()
	output = deque(i for i in p.communicate(x)[0].split('\n') if len(i)>0)
	totalTime += time.time()-start

	if p.returncode != 0:
		print('[ERROR] Crashed with return code', p.returncode, 'on test case')
		print(x)
		prompt()
		good = False
		continue

	num = int(output.popleft())
	if num != n:
		print('[ERROR] Wrong number of solutions')
		print('Your answer:', num)
		print('Correct answer:', n)
		print('Test case:')
		print(x)
		prompt()
		good = False
		continue

	if len(output) != n:
		print('[ERROR] Inconsistent number of solutions')
		print('Your P was correct (the number is correct), but you did not output the solutions themselves')
		print('Your program claimed:', n, 'solutions')
		print('Your program outputted:', len(output), 'solutions')
		print("If you're sure this is not the case, it might be an issue with the tester - make sure your program isn't outputting any extra whitespace")
		print('Test case:')
		print(x)
		prompt()
		good = False
		continue

	s = set()
	g = False
	for i in range(n):
		sol = tuple(output.popleft().split())
		if sol in s:
			print('[ERROR] Duplicate solution')
			print('Your program printed the same solution more than once')
			print('Solution:', ' '.join(sol))
			print('Test case:')
			print(x)
			prompt()
			good = False
			g = True
			break
		if sol not in y:
			mat = convertTo2D(sol, h, w)
			rot = rotate(rotate(mat))
			flipped = flip(mat)
			frot = rotate(rotate(flipped))
			if (c1(rot) not in y) and (c1(flipped) not in y) and (c1(frot) not in y):
				print('[ERROR] Wrong solution')
				print('Your program printed a solution that is wrong')
				print('Solution:', ' '.join(sol))
				print('This might be an issue with my program - if you are confident your answer is right let me know')
				print('Common issues may include - printing column by column instead of row by row')
				print('Test case:')
				print(x)
				prompt()
				good = False
				g = True
				break
		s.add(sol)
	if g:
		continue

if good:
	print('Congrats, all cases passed!')
	print('Took', totalTime, 'seconds')
	print("One more case!! - I'm too lazy to code it into the tester")
	print("Make sure you check that h*w is the same as the number of blocks covered by the pieces BEFORE any brute forcing")
	print("This will make sure that Nevard won't hang your program with something like:")
	print("1\nS\n600 600")
else:
	print('Oops, you failed at least one case')