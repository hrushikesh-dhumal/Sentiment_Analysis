import nltk;
import re;
import os;

# Set the working directory to current location
wrk_dir = os.getcwd();
os.chdir(wrk_dir);

# Read the positive and negative lexicons/bags of words
def getLexicon(path_to_my_read_file):
    """
    arguments:
    input: @path_to_my_read_file: path to a file.
    returns: a tuple containing lexicon of words with space and \n removed
    """
    
    lexica = []; # list to append all the lexicons
    my_file=open(path_to_my_read_file, "r").readlines();
    # Read words from each line
    for line in my_file:
        lexica.append(re.sub("_", " ", line[:-1])); # Remove the \n(last character) from each line and replace _ with space
    # Return tuple for less memory size and make the lexicon unchangeable
    return tuple(lexica);
    
posLexicon = getLexicon("data\postest");
negLexicon = getLexicon("data\\negtest"); #the double \\ to avoid python reading it as \n

# Read the data file
my_file=open("data\\test.tsv", "r").readlines();
res = [];
for tweet in my_file: # Read tweet in line
    pos = neg = 0; # Counts for negative and positive words in a tweet
    for lexicon in posLexicon:
        if tweet.find(lexicon):
            pos+=1;
    for lexicon in negLexicon:
        if tweet.find(lexicon): #re.findall(posLexica, tweet)
            neg+=1;
    # Result is positive/negative depending on which word count is more else neutral.
    if pos > neg: 
        res.append("POSITIVE");
    elif pos < neg:
        res.append("NEGATIVE");
    elif pos == neg:
        res.append("NEUTRAL");
        
out_file=open("data/output", "w"); # Opens for writing
print>>out_file, res # Save output to disk
out_file.close();
