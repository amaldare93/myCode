#!/usr/bin/python

import random
import collections
import math
import numpy
import copy
import sys
from collections import Counter
from util import *

############################################################
# Problem 2: binary classification
############################################################

############################################################
# Problem 2a: feature extraction
def extractWordFeatures(x):
    """
    Extract word features for a string x.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    fv = {}
    for w in x.split():
        if(w in fv):
            fv[w] = fv[w] + 1
        else:
            fv[w] = 1
    return fv
    # END_YOUR_CODE

############################################################
# Problem 2b: stochastic gradient descent
def learnPredictor(trainExamples, testExamples, featureExtractor):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, return the weight vector (sparse feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    weights = {}  # feature => weight
    # BEGIN_YOUR_CODE (around 15 lines of code expected)
    numIters = 19
    etc = .01
    def gradient_Loss(x, y):
        if(dotProduct(weights, x) * y <= 1):
            return {f: v * -y for (f, v) in x.items()}
        else:
            return {f: 0 for (f, v) in x.items()}

    for i in range(numIters):
        for j in trainExamples:
            increment( weights, -etc, gradient_Loss(featureExtractor(j[0]), j[1]) )

    # END_YOUR_CODE
    return weights
############################################################
# Problem 2c: generate test case

weights = {"hello":1, "world":-1}
def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) can be anything (randomize!) with a nonzero score under the given weight vector
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        # BEGIN_YOUR_CODE (around 5 lines of code expected)
        #phi = random.choice([f for (f, v) in weights.items()])
        phi = {}
        for w in weights:
            phi[w] = random.randint(0, 20)

        y = math.copysign(1, dotProduct(weights, phi))
        # END_YOUR_CODE
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]
#generateDataset(100, weights)
############################################################
# Problem 2f: n-gram features
def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all 1,2,3,...,n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'I': 1, 'like': 1, 'tacos': 1, 'I like': 1, 'like tacos': 1, 'I like tacos' : 1}
    EXAMPLE: (n = 3) "not good. This movie not good" ->
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (around 10 lines of code expected)
        fv = {}
        words = x.replace(' ','')
        for j in range(len(words)-n+1):
            if ''.join(words[j:j+n]) in fv:
                fv[''.join(words[j:j+n])] += 1
            else:
                fv[''.join(words[j:j+n])] = 1 
        return fv
        # END_YOUR_CODE
    return extract
    
def extractNgramFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all 1,2,3,...,n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'I': 1, 'like': 1, 'tacos': 1, 'I like': 1, 'like tacos': 1, 'I like tacos' : 1}
    EXAMPLE: (n = 3) "not good. This movie not good" ->
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (around 10 lines of code expected)
        fv = {}
        words = x.split()
        for j in range(len(words)-n+1):
            if ' '.join(words[j:j+n]) in fv:
                fv[' '.join(words[j:j+n])] += 1
            else:
                fv[' '.join(words[j:j+n])] = 1 
        return fv
        # END_YOUR_CODE
    return extract
#ngram = extractNgramFeatures(3)
#print ngram(string)
############################################################
# Problem 2h: extra credit features

def extractExtraCreditFeatures(x):
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 3: k-means
############################################################

x1 = {0:1, 1:0}
x2 = {0:2, 1:1}
x3 = {0:0, 1:0}
x4 = {0:0, 1:2}

examples = [x1, x2, x3, x4]
def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (around 35 lines of code expected)

    # calculates Euclidean Distance**2
    def distance(v1, v2):
        return sum([((v1[i] - v2[i])**2) for i in v1])

    mews = {}
    assignments = {}
    loss = 0

    # choose random mews
    temp = random.sample(examples, K)
    samples = copy.deepcopy(temp)
    for i in range(K):
        mews[i] = samples[i]
    #print 'initial random mew: ', mews

    #start loop
    for _ in range(maxIters):
        old_loss = loss

        # assign x based on mew
        for j in range(len(examples)): 
            dist = {}
            for i in mews:
                dist[i] = distance(examples[j], mews[i])
            assignments[j] = min(dist, key=dist.get)
        #print 'assignments: ', assignments

        # set mew based on assignments
        for i in mews:  # each mew
            for x in mews:   # each dimension in mew
                mews[i][x] = numpy.mean([examples[j][x] for j in range(len(examples)) if assignments[j] == i])
                #print [j for j in range(len(examples))]
        #print 'new mew: ', mews

        # calculate reconstruction loss
        loss = sum([distance(examples[i], mews[assignments[i]]) for i in range(len(examples))])

        # test for convergence
        if old_loss == loss:
            break

    return (mews, assignments, loss)
                            
    # END_YOUR_CODE







