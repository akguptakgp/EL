from sets import Set
PosTags=[]
with open("sample-output.txt","r") as f:
	for line in f:
		for i in line.split():
			PosTags.append(i.split('_')[1])
position={}
UniquePosTags=list(Set(PosTags))
for i in range(len(UniquePosTags)):
	position[UniquePosTags[i]]=i
# print PosTags
# print position	

count1D=[0 for i in range(len(UniquePosTags))]
count2D=[[0 for j in range(len(UniquePosTags))] for i in range(len(UniquePosTags))]
count1D[position[PosTags[0]]]+=1
count1D[position[PosTags[-1]]]-=1
for i in range(1,len(PosTags)):
	count1D[position[PosTags[i]]]+=1
	count2D[position[PosTags[i-1]]][position[PosTags[i]]]+=1
print "Biagram Non-zero Probabilities are"
for i in UniquePosTags:
	for j in UniquePosTags:
		if(count1D[position[i]]!=0):
			prob=count2D[position[i]][position[j]]*1.0/count1D[position[i]]
			if(prob!=0):
				print i,'\t',j,'\t->\t',prob


