import shell
import util
import wordsegUtil

############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return 0
        # END_YOUR_CODE

    def isGoal(self, state):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return state == len(self.query)
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (around 10 lines of code expected)
        results = []
        for i in range(state, len(self.query)): # for each char from state until end of string

            string = self.query[state:i+1]      # string = from state char to i
            newState = state + len(string)      # new state = state + 
            cost = self.unigramCost(string)

            results.append((string, newState, cost))

        return results

        # END_YOUR_CODE

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    return ' '.join(ucs.actions)
    # END_YOUR_CODE

############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return 0
        # END_YOUR_CODE

    def isGoal(self, state):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return state == len(self.queryWords)
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (around 10 lines of code expected)
        #print 'succAndCost(', state, ')'

        results = []

        if len(self.possibleFills(self.queryWords[state])) == 0:

            prev = wordsegUtil.SENTENCE_BEGIN
            string = self.queryWords[state]
            newState = state + 1
            cost = self.bigramCost(prev, string)
            results.append((string, newState, cost))

        else:

            for fill in self.possibleFills(self.queryWords[state]):

                if state == 0:

                    prev = wordsegUtil.SENTENCE_BEGIN
                    string = fill
                    newState = state + 1
                    cost = self.bigramCost(prev, string)
                    results.append((string, newState, cost))

                else:
                    for prev in self.possibleFills(self.queryWords[state-1]):
                        
                        string = fill
                        newState = state + 1
                        cost = self.bigramCost(prev, string)
                        results.append((string, newState, cost))

        return results

        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    if len(queryWords) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))

    return  ' '.join(ucs.actions)
    # END_YOUR_CODE

############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return 0
        # END_YOUR_CODE

    def isGoal(self, state):
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        return state == len(query)
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (around 15 lines of code expected)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################

if __name__ == '__main__':
    shell.main()
