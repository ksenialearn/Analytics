sentimentscore = {}
with open("AFINN-111.txt", "r") as sentimentfile:
    for line in sentimentfile:
        parts = line.split()
        score = int(parts[-1])
        text = ' '.join(parts[0:-1])
        sentimentscore[text] = score        

tweets = []
with open("output.txt","r") as tweetfile:
    for line in tweetfile:
        tweets.append(line)


score= 0

keys= sentimentscore.keys()

for tweet in tweets:
    sc= 0
    for key in keys:
        if key in tweet:
            sc+= sentimentscore[key]
    if sc>0:
        print tweet
    score+=sc
                            
            
print score
