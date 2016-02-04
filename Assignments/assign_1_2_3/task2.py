import networkx as nx
from sets import Set
f = open('out_task2.txt', 'r')
if(f!=None):
    str1=f.read().splitlines()
    arr=""
    for line in str1:
        arr+=line
    ar=arr.replace('','')
else:
    print "error opening the file"

text_input=[]
text_input_2=[]
itr=0
while(ar.find("(. .)))")!=-1):
    itr+=1
    if(itr!=1):
        tmp=num1
    num1=ar.find("(ROOT  (")
    if(itr!=1):
        text_input_2.append(ar[(ar[:num1].find(". .)))")+6):num1])
    num2=ar.find("(. .)))")
    temp1=ar[num1:num2]
    text_input.append(temp1)
    ar=ar[num2+1:len(ar)]
text_input_2.append(ar[(ar[:num1].find(". .)))")+6):])
edges=[{},{}]
def graph(string,senNo):
    global edges
    G=nx.Graph()
    curr=0
    mylst=['MYROOT']			
    spt=string.split('(')
    glbl=1
    # print spt
    for line in spt:
    	if(line!=''):
            l=line.split(')')
            for s in l:
                if(s==''):
                    # print "no"
                    mylst.pop()
                    curr-=1
                elif(s.isspace()):
                    # print "yes"
                    mylst.pop()
                    curr-=1
                else:
                    s=s.strip()
                    if(len(s.split())==1):
                        if(s not in G.nodes()):
                            # print "adding edge",mylst[curr],",",s	       #add edge
                            if mylst[curr]+"$"+s not in edges[senNo]:
                                edges[senNo][mylst[curr]+"$"+s]=1
                            else:
                                edges[senNo][mylst[curr]+"$"+s]+=1
                            mylst.append(s)
                            curr+=1
                        else:
                            # print "adding edge",mylst[curr],",",s+str(glbl)
                            if mylst[curr]+"$"+s+str(glbl) not in edges[senNo]:
                                edges[senNo][mylst[curr]+"$"+s+str(glbl)]=1
                            else:
                                edges[senNo][mylst[curr]+"$"+s+str(glbl)]+=1
                            mylst.append(s+str(glbl))
                            curr+=1
                            glbl+=1
                    else:
                        if(s.split()[1] not in G.nodes()):
                            # print "adding edge",mylst[curr],",",s.split()[0],"\there",s.split()[1]
                            if mylst[curr]+"$"+s.split()[0] not in edges[senNo]:
                                edges[senNo][mylst[curr]+"$"+s.split()[0]]=1
                            else:
                                edges[senNo][mylst[curr]+"$"+s.split()[0]]+=1
                            mylst.append(s.split()[0])
                            curr+=1
                        else:
                            # print "adding edge",mylst[curr],",",s.split()[0]+str(glbl),"\tpppppp",s.split()[1]
                            if mylst[curr]+"$"+s.split()[0] not in edges[senNo]:
                                edges[senNo][mylst[curr]+"$"+s.split()[0]]=1
                            else:
                                edges[senNo][mylst[curr]+"$"+s.split()[0]]+=1
                            mylst.append(s.split()[0]+str(glbl))
                            curr+=1
                            glbl+=1
         
    # print len(nx.shortest_path(G,'Dibaba','Ethiopian'))

graph(text_input[0],0)
# for f in  edges[0].keys():
#     print f,edges[0][f]
graph(text_input[1],1)

# for f in edges[1].keys():
#     print f,edges[1][f]
commonEdge=0
# print Set(edges[0].keys()).intersection(Set(edges[1].keys()))
for common in Set(edges[0].keys()).intersection(Set(edges[1].keys())):
    if('MYROOT' in common):
        continue
    # print common,edges[0][common],edges[1][common]
    if(edges[0][common]>=edges[1][common]):
        commonEdge+=edges[1][common]
    else:
        commonEdge+=edges[0][common]
        
print commonEdge    
    
list1=[{},{}]    
def depgraph(string,senNo):
    for i  in string.split(')'):
        if(i!=''):
            relation=i.split('(')[0]
            if relation in list1[senNo]:
                list1[senNo][relation]+=1
            else:
                list1[senNo][relation]=1   
            first=i.split('(')[1].split(',')[0]
            second=i.split('(')[1].split(',')[1]
            # print relation,first,second   


depgraph(text_input_2[0],0)
# print 
depgraph(text_input_2[1],1)   
# for i in list1:
#     print 
#     for k in i :
#         print k,i[k]
commonEdge=0
for common in Set(list1[0].keys()).intersection(Set(list1[1].keys())):
    # print common,list1[0][common],list1[1][common]
    if(list1[0][common]>=list1[1][common]):
        commonEdge+=list1[1][common]
    else:
        commonEdge+=list1[0][common]

print commonEdge        
            