import pandas as pd


def getfilm(x):

	df = pd.read_csv("data/filmcorpus.csv",usecols= [0,1,2])
	if x==0:
		df=(df.loc[df['emotion'] == 0])
	else:
		df=(df.loc[df['emotion'] == 1])		
	films = df['film'].tolist()
	urls = df['url'].tolist()
	req=[]
	stri=""
	for i in range(len(films)):
		stri=films[i]+"("+urls[i]+")"
		req.append(stri)
	import random
	random.shuffle(req)
	return(req[0:5])
