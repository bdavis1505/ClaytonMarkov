import math
import os
import random
import collections
import numpy
import hashlib

#TODO fix this shitty code
def buildDataSet(file, persist=False):
	dataSet = node("")

	f = open(file, 'r')
	line = fp.readline()
	spline = line.strip().split(" ")
	for i in range(0,len(spline)):
		if node(i) in dataSet:
			for j in range (i+1, len(spline)):
				tempNode = node(i).addChainedWord(spline[j]) 
				if tempNode is not None:
					j += 1
					tempNode.addChainedWord(spline[j])
				else:
					pass

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

	def __eq__(self, other):
		if self.getVal() == other.getVal():
			return True
		else:
			return False

	def __hash__(self):
		#returns the sum of all ascii characters in the string... could possibly be an issue later on with words that
		#are anagrams of eachother (such as listen and silent) but this appears to be an easy fix for now
		x = [ord(i) for i in self.getVal()]
		total = 0
		for i in x:
			total += i

		return(total)

	def generateChain(self):
		generatedStringChain = ""
		generatedString, generatedNode = self.selectRandomNext()
		while(generatedString is not None):
			generatedStringChain += generatedString + " "
			generatedString, generatedNode = generatedNode.selectRandomNext()

		return generatedStringChain

	def addChainedWord(self, word):
		tempNode = node(word)
		if tempNode in self.pairWords:
			self.pairWords[tempNode] += 1
			return tempNode
		else:
			self.pairWords.update({tempNode : 1})
			return None

x = node(pairWords={
		node(value="Node", pairWords={node("Bodes"):3,node("Coeds"):6,node("Boats"):7}):32,
		node(value="Code"): 18,
		node(value="Chode"):5
	})

print(x.generateChain())
