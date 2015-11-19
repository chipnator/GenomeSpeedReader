# Code for reading and issolating common 5, 8 and 15 basepair sequences within
# the given Genome.

def readcode():
    fileClean=open("VCgenomeClean.txt", "r")
    fileFinal=open("Output-Final_bp_Sequence.txt", "w")
    genome=fileClean.read()
    listofbp9=[] #empty list
    maximum=0
    theSeq={}
    outStr=""
    lengths=[5,8,15]
    for length in lengths:
        for i in range(len(genome)-(length-1)): #Iterate accross genome
            if i%20000==0 and i!=0: 
                keys = [x for x,y in theSeq.items() if y > 1] #gets keys 
                for key in keys:
                    #creates a list of keys and values
                    listofbp9.append(key)
                    listofbp9.append(theSeq[key])
                theSeq={} #reset dictionary
                for t in range(0,len(listofbp9),2):
                    theSeq[listofbp9[t]]=listofbp9[t+1]
                    #add back in the dict items that have more than one
            bp9=genome[i:i+int(length)]
            bp9J="".join(bp9)
            if bp9J in theSeq:
                theSeq[bp9J]=theSeq[bp9J]+1
            else:
                theSeq[bp9J]=1
        maxxx = max(theSeq.values())
        for h in range(maxxx,1,-1):
            keyss = [x for x,y in theSeq.items() if y==h]
            if keyss!=[]:
                outStr+="Sequences "+str(keyss)+" occurred "+str(h)+" times. \n \n"
    print("Data written to Output-Final_bp_Sequence.txt")
    fileFinal.write(outStr)

    
readcode()
