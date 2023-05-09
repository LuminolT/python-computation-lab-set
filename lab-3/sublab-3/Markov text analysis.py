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
    #剔除换行符和引号
    text=text.replace("\n"," ")
    text=text.replace("\"","")
    text=text.replace("--","")
    #保证每个标点符号都和前面的单词在一起
    #这样不会被剔除，保留在马尔科夫链中
    punctuation=[',','.',';',':']
    for symbol in punctuation:
        text=text.replace(symbol," "+symbol+" ")
    words=text.split(" ")
    #过滤空单词
    words=[ word for word in words if word !=""]
    
    wordDict={}
    for i in range(n,len(words)):
        word=' '.join(words[i-n:i])
        if word not in wordDict:
            #为单词新建一个字典
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
        #生成链长为100的马尔科夫链
        # print(wordDict)
        # fileOUt.write(str(wordDict))
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
