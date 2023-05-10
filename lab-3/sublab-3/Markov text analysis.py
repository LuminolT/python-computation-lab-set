from random import randint
from random import choice

def wordListSum(wordList):
    sum=0
    for word,value in wordList.items():
        sum+=value
    return sum
 
def retrieveRandomWord(wordList):
    randIndex=randint(1,wordListSum(wordList))
    for word,value in wordList.items():
        randIndex-=value
        if randIndex<=0:
            return word
        
def buildWordDict(text,n):
    text=text.replace("\n"," ")
    text=text.replace("\"","")
    text=text.replace("--"," ")
    text=text.replace("_","")
    text=text.replace("`","")
    text=text.replace("\'","")

    punctuation=[',','.',';',':','!','?']
    for symbol in punctuation:
        text=text.replace(symbol," "+symbol+" ")
    words=text.split(" ")

    words=[ word for word in words if word !=""]
    
    wordDict={}
    for i in range(n,len(words)):
        word=' '.join(words[i-n:i])
        if word not in wordDict:
            wordDict[word]={}
        if words[i] not in wordDict[word]:
            wordDict[word][words[i]] = 0
        wordDict[word][words[i]]+=1
    return wordDict

def Markov_chain(n,m):
    with open(r'emma.txt','r',encoding='utf-8') as fileIn,open(r'testemma.txt','w',encoding='utf-8') as fileOUt:
        text=fileIn.read()
        wordDict=buildWordDict(text,n)
        OutsetList=[]
        for key in wordDict.keys():
            if key[0].isupper():
                OutsetList.append(key)
        s=0
        chain = []
        prefix = choice(OutsetList)
        chain += (prefix.split(' '))
        while s < m:
            if chain[-1]=='.':
                s+=1
                print(' '.join(chain))
                chain = []
                prefix=choice(OutsetList)
                chain+=prefix.split(' ')
                continue
            selectedWord=retrieveRandomWord(wordDict[prefix])
            chain += [selectedWord]
            prefix = ' '.join(chain[-2:])

if __name__=='__main__':
    n=2
    m=2
    Markov_chain(n,m)
