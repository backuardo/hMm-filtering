from MarkovFilter import *
# test.py
# Eisner Nov 2017
#
# This file runs a few different tests with varying numbers of walls and
# varying lengths of sequence. The maze and sequence are randomly generated
# each time the code is ran, so the test cases will produce different results
# each time.

print('---------------------TEST 1-----------------------')
print('Walls: 1, Sequence Length: 5\n')
rm1 = RoboMaze(1, 5)
mf1 = MarkovFilter(rm1)
f1 = mf1.filter()
rm1.display_maze()
print('\nSequence: ', mf1.sequence)
print('\nDistributions: ')
for distribution in f1:
    print(distribution)

print('\n\n---------------------TEST 2-----------------------')
print('Walls: 3, Sequence Length: 10\n')
rm2 = RoboMaze(3, 10)
mf2 = MarkovFilter(rm2)
f2 = mf2.filter()
rm2.display_maze()
print('\nSequence: ', mf2.sequence)
print('\nDistributions: ')
for distribution in f2:
    print(distribution)

print('\n\n---------------------TEST 3-----------------------')
print('Walls: 6, Sequence Length: 20\n')
rm3 = RoboMaze(6, 20)
mf3 = MarkovFilter(rm3)
f3 = mf3.filter()
rm3.display_maze()
print('\nSequence: ', mf3.sequence)
print('\nDistributions: ')
for distribution in f3:
    print(distribution)

print('\n\n---------------------TEST 4-----------------------')
print('Walls: 10, Sequence Length: 30\n')
rm4 = RoboMaze(10, 30)
mf4 = MarkovFilter(rm4)
f4 = mf4.filter()
rm4.display_maze()
print('\nSequence: ', mf4.sequence)
print('\nDistributions: ')
for distribution in f4:
    print(distribution)