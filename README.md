# ComboPermutation
Execute combinations or permuations (both where no replacement occurs)
## How-To
If you want some theory on how combinations and permutations work look here:
https://www.mathsisfun.com/combinatorics/combinations-permutations.html

This module allows for permutations or combinations which are not repetitive (replaced).
There are some example formulas in that link as well. This module uses the math library and takes in factorial as the formula for doing permutations and combinations require factorials. To use module, you can pass parameters based on which function you are using. If using combination, x will pass the amount of objects you are choosing and the y would pass from what amount of things you are choosing from. The permutation would function in a similar manner however, remember with permutations, order matters where with combos it does not. Therefore you need to understand they will both yield different results.
## Example Code
```
from ComPer.ComboPerm import cp

object = cp.combination(3,10)
print(object)
object = cp.permuation(3,10)
print(object)
*********************************
OUTPUT:
120.0
720.0

Process finished with exit code 0
```
