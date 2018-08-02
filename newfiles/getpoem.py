import pandas as pd


def getpoem(x):
	df = pd.read_csv("data/corpus/poemcorpus.csv",usecols= [1,2,3])
	if x==0:
		df=(df.loc[df['emotion'] == 0])
	else:
		df=(df.loc[df['emotion'] == 1])		
	poems = df['poem'].tolist()
	urls = df['url'].tolist()
	req=[]
	stri=""
	for i in range(len(poems)):
		stri=poems[i]+"("+urls[i]+")"
		req.append(stri)
	import random
	random.shuffle(req)
	return(req[0:5])
