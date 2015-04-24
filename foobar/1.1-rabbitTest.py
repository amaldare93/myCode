'''
Rabbit test subjects
====================

The diabolical Professor Boolean has captured you and a group of your hapless rabbit kin as test sunjects for his terrible experiments! You're not sure what is real plans are, but currently it seems he's trying to make everyone faster and smarter? He's exposing rabbit test subjects to novel chemicals, genetic manipulations, and pathogens, then meaduring their completion time for various puzzles and excercises. Then again, there's a rumor he's developing a kind of zombie rabbit. You don't want to become a zombit!

Unfortunately, due to insubordination and laziness, Professor Boolean just "eliminated" the lab assistant tracking all data from this research. Now he's forcing you to sort through the notes and find something useful from the chaos. You have no chouce but to abide by your captors evil rules. For now.

Of the subjects that have survived, each has a distinct file, with anywhere from 1 to 100 measurements of completion time for the tests. The mesurements from the before and after cases are listed separately, but the ordering has been mixed up. You have to figure out the degree of improvement (0% to 99%, rounded to the nearest whole number) based on the two lists of results.

For example, if the first list of times is [22.2, 46, 100.8] and the second list is [23, 11.1, 50.4] you would return 50, because the times got 50% shorter: the 22.2 entry improved to 11.1, the 46 improved to 23, and the 100.8 improved to 50.4. Even though the data points are in different order, each improves by the same amount.

Write a function answer(x, y) which takes two lists of floating point performance scores and returns the improvement percentage, rounded to the nearest integer.

'''

def answer(y, x):
    # your code here
    return int(round((1 - sum(y) / sum(x)) * 100))

print answer([23, 11.1, 50.4], [22.2, 46, 100.8])

