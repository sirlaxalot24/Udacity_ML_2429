from scipy import stats
import math

pk1 = 2.0/2.0

prob1 = -pk1 * math.log(pk1, 2)

pk2 = 2.0/2.0

prob2 = -pk2 * math.log(pk2, 2)

ent = prob1 + prob2

print ent