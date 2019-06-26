import math
import os
import random
import collections
import numpy
import hashlib

#TODO fix this shitty code
def buildDataSet(file, persist=False):
	dataSet = node()
	f = open(file, 'r')
	for line in f:
		spline = line.strip().split(" ")
		iterNode = dataSet

		for i in spline:
			iterNode = iterNode.addChainedWord(i)
			print(iterNode.getVal())

	f.close()
	return dataSet
		



class node:

	#value is the string value the node contains, pairWords is a dict of nodes with the number of occurances
	def __init__(self, value=None, pairWords={}):
		self.value = value
		self.pairWords = pairWords

	def selectRandomNext(self):
		#Generate a probability distribution called probs
		probs = []
		#And a list of Node values called vals
		vals = []
		for i in self.pairWords:
			probs.append(self.getProb(i))
			vals.append(i)

		if vals == [] or probs == []:
			return None, None

		selectedString = None
		selectedNode = None
		#use numpy function for weighted choice
		try:
			selectedNode = numpy.random.choice(a=vals, size=None, replace=True, p=probs)
			selectedString = selectedNode.getVal()
		except ValueError:
			pass

		return selectedString, selectedNode

	def getProb(self, word):
		if word in self.pairWords:
			total = 0
			for n in self.pairWords:
				total += self.pairWords[n]
			return (float(self.pairWords[word] / total))
		else:
			return 0.0

	def getVal(self):
		return self.value

	def generateChain(self):
		generatedStringChain = ""
		generatedString, generatedNode = self.selectRandomNext()
		while True:
			generatedStringChain += generatedString + " "
			generatedString, generatedNode = generatedNode.selectRandomNext()
			if generatedString is None or generatedNode is None:
				break
			print(generatedString)

		return generatedStringChain

	#Pretty sure this is the issue here, keep fixing this
	def addChainedWord(self, word):
		for n in self.pairWords:
			if n.getVal() == word:	
				self.pairWords[n] += 1
				else:
					self.pairWords.update({tempNode : 1})
				
				for n in self.pairWords:
					if n == tempNode:
						return n
		return None

print(buildDataSet("training.txt").generateChain())
