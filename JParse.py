##This program will take a specified text file, calculate the frequency of tokens (specified by delimiters, words by default), and print a text file with the sorted tokens.

import re ##regular expressions
import os.path


def fileToList(fpath, delim):
    pathdir = os.path.dirname(fpath)
    pathdir = os.path.abspath(pathdir)
    file = open(fpath)
    content = file.read()
    file.close()
    if len(delim) == 0:
        #replace newlines and punctuation with a space
        content = re.sub('(\n)+', ' ', content)
        content = re.sub("[,-.!:?_;]", ' ', content)

        ##remove  ,'"
        content = re.sub("[')(]", '', content)
        content = re.sub('"', '', content)

        ##convert remaining characters to lowercase
        content = content.lower()
        ##split string into words (at this point they should be seperated by spaces)
        words = content.split()
    else:
        #Remove new lines and " (Excel csv files encapsulate each line in ")
        removelines = re.sub('\n', delimiter, content)
        removelines = re.sub('"', '', removelines)
        tokens = removelines.split(delimiter)
        words = []
        for token in tokens:
            new = token.strip()
            if len(new) != 0:
                words.append(new)
    return words
        
def listToSortedFreq(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word]=freq[word]+1
        else:
            freq[word]=1
    freqpairs = freq.items()
    sortedpairs = sorted(freqpairs, key=lambda pair: pair[1], reverse=True)
    return sortedpairs
    
def listOfTuplesToFile(tokenlist, inpath):
    inpath = os.path.dirname(inpath)
    inpath = os.path.abspath(inpath)
    newfile = open(inpath + "\\output.csv", 'w')
    for pair in tokenlist:
        newfile.write(str(pair[0]) + "," + str(pair[1])+"\n")
    newfile.close()
    print 'Output written to ', inpath, '\\output.csv'
    
if __name__ == '__main__':
    filefound = False
    while filefound == False:
        path = raw_input('Please enter the absolute path of the text file to be parsed.\ne.g. C:\\dump\\1.txt\n')
        if os.path.isfile(path):
            filefound = True
        else:
            print 'File does not exist.'
    delimiter = raw_input('Please enter the delimiter.  Leave black to use default (Space).\n')

    words = fileToList(path, delimiter)
    sortedpairs = listToSortedFreq(words)
    listOfTuplesToFile(sortedpairs, path)