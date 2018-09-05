import sys
import json

sentimentScores = {}
    
def afinn_build_sentiment():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score  = line.split("\t")
        sentimentScores[term] = int(score)
        
def tweet_scorer():
    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweet = json.loads(line)
        tweet_sentiment_score = 0;
        if 'text' in tweet:
	    words = tweet["text"].encode('UTF-8').split() 
            for word in words:
                if word in sentimentScores:
                    tweet_sentiment_score += sentimentScores[word]
        print tweet_sentiment_score;

def main():
    afinn_build_sentiment()
    tweet_scorer()

if __name__ == '__main__':
    main()

