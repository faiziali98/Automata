

edgeArr =  {
	(0,'a') : 4,
	(0,'b') : 2,
	(2,'a') : 1,
	(2,'b') : 3,
	(1,'a') : 1,
	(1,'b') : 3,
	(3,'a') : 3,
	(3,'b') : 5,
	(5,'b') : 4,
	(5,'a') : 4,
	(4,'a') : 4,
	(4,'b') : 4
}

accepting = [3,5]
states=[]
Edges=[]
toRet={}

def deleteDead(edges):
	for i in edges:
		if i[0] not in states:
			states.append(i[0])
		if edges[i] not in states: # if state has no in edge
			states.append(edges[i])
		if i[1] not in Edges:
			Edges.append(i[1])

	Dead=[]
	count = 0
	instance = 0

	for i in states:
		for j in Edges:
			if edges[(i,j)]:
				instance +=1
			if edges[(i,j)]==i:
				count += 1
		if (count == len(Edges)):	
			Dead.append(i)
		count = 0

	for i in edges:
		if edges[i] not in Dead:
			toRet[i] = edges[i]
	return toRet

def selfLoops(edgesMap):
	states = []
	for action in edgesMap:
		if action[0] == edgesMap[action]:
			states.append(action[0])
	return states


print "States excpet dead states are: \n\nEdgesMap:{\n",
for x in deleteDead(edgeArr):
	print x
print "}\n"

print "Self Loops are: \n\n",selfLoops(toRet)
