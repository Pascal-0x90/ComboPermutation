from math import factorial

class cp(object):

    #    To use module, you can pass parameters based on which
    #    function you are using. If using combination, x will pass
    #    the amount of objects you are choosing and the y would pass
    #    from what amount of things you are choosing from.
    #
    #    The permutation would function in a similar manner however,
    #    remember with permutations, order matters where with combos
    #    it does not. Therefore you need to understand they will both
    #    yield different results.

    def combination(x, y, z='n'):  # Combination without Repetition
        robject = int(x)  # Choosing r objects
        nsets = int(y)  # From n sets
        combos = (factorial(nsets)) / (factorial(robject) * factorial(nsets - robject))
        return combos

    def permuation(x, y, z='n'):  # Permutation without repetition
        robject = int(x)  # We choose r of them
        nsets = int(y)  # Number of things to choose from
        permutations = (factorial(nsets)) / factorial(nsets - robject)
        return permutations