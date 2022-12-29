#Ghofrane kamoun
#Imagine you place a knight chess piece on a phone dial pad.
# This chess piece moves in an uppercase “L” shape: two steps horizontally followed by one vertically, or one step horizontally then two vertically.
#Suppose you dial keys on the keypad using only hops a knight can make. Every time the knight lands on a key, we dial that key and make another hop.
# The starting position counts as being dialed.
#How many distinct numbers can you dial in N hops from a particular starting position?

hops = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}


def count(n, p):
    if n == 0:
        return 1

    result = 0

    for position in hops[p]:
        result = result + count(n - 1, position)

    return result


n = int(input('please enter number of Hops:\n n= '))
p = int(input("what is your start position ?\n p= "))
if n < 0:
    print('inputs are incorrect ')
    print('please enter positive integer n ')
elif p > 9 or p < 0:
    print("please enter positive integer p between 0 and 9 ")
elif n == 0:
    print("You can dial only 1 number from a starting position of " + str(p))
else:
    print('You can dial {0} number from a starting position of {1}.'.format(count(n - 1, p), p))
