import sys
import requests
import gzip
import os
import shutil
import getopt
import operator
import fasttext
import numpy as np
from german_normalize import normalize
from sklearn.metrics.pairwise import cosine_similarity
import argparse

fasttext.FastText.eprint = lambda x: None

parser = argparse.ArgumentParser(description='Run Fast-forward network.')
parser.add_argument('-l', '--language', help='language', required=True)
parser.add_argument('-f', '--inputFile', help='input-file', required=True)
parser.add_argument('-e', '--embeddingsFile', help='embeddings-file')
args = parser.parse_args()

lang = args.language
listFile = args.inputFile
embeddingsFile = args.embeddingsFile


if args.embeddingsFile is not None:
	sys.stderr.write("Loading model\n")
	model = fasttext.load_model(embeddingsFile)
else:	
	try:
		sys.stderr.write("Loading model\n")
		model = fasttext.load_model('cc.'+lang.lower()+'.300.bin')

	except:
		sys.stderr.write("Embeddings not found.\n")
		link = 'https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.'+lang.lower()+'.300.bin.gz'
		file_name = 'cc.'+lang.lower()+'.300.bin.gz'
		with open(file_name, "wb") as f:
		    sys.stderr.write("\nDownloading %s \n" % file_name)
		    response = requests.get(link, stream=True)
		    total_length = response.headers.get('content-length')

		    if total_length is None: 
		        f.write(response.content)
		    else:
		        dl = 0
		        total_length = int(total_length)
		        for data in response.iter_content(chunk_size=4096):
		            dl += len(data)
		            f.write(data)
		            done = int(50 * dl / total_length)
		            sys.stderr.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
		            sys.stderr.flush()

		sys.stderr.write("\nUnzip %s \n" % file_name)
		with gzip.open('cc.'+lang.lower()+'.300.bin.gz', 'rb') as f_in:
		    with open('cc.'+lang.lower()+'.300.bin', 'wb') as f_out:
		        shutil.copyfileobj(f_in, f_out)	
		        
		os.remove('cc.'+lang.lower()+'.300.bin.gz')
		sys.stderr.write("Loading model\n")
		model = fasttext.load_model('cc.'+lang.lower()+'.300.bin')

catDict1 = dict()
with open ("categories/categories1-"+lang+".tsv", 'r') as file:
	for line in file:
		line = line.strip()
		parts = line.split(",")
		catDict1[parts[0]] = parts[1:]


catDict2 = dict()
with open ("categories/categories2-"+lang+".tsv", 'r') as file:
	for line in file:
		line = line.strip()
		parts = line.split(",")
		catDict2[parts[0]] = parts[1:]

catEmbDict1 = dict()
for category in catDict1:
	myCategoryArray = []
	for item in catDict1[category]:
		item = item.strip()
		if " " in item:
			embedding = model.get_sentence_vector(item)
		else:
			embedding = model[item]
		myCategoryArray.append(embedding)

	catEmbDict1[category] = np.mean(myCategoryArray, axis=0)


catEmbDict2 = dict()
for category in catDict2:
	myCategoryArray = []
	for item in catDict2[category]:
		item = item.strip()
		if " " in item:
			embedding = model.get_sentence_vector(item)
		else:
			embedding = model[item]
			
		myCategoryArray.append(embedding)

	catEmbDict2[category] = np.mean(myCategoryArray, axis=0)

similarityDict1 = dict()
similarityDict2 = dict()

def computeSimilarity1 (word):
	wordEmb = model[word].reshape(1,-1)

	for category in catEmbDict1:
		catEmb = catEmbDict1[category].reshape(1,-1)
		cosine_value = cosine_similarity(catEmb, wordEmb)
		similarityDict1[category] = cosine_value

	classificationList1 = []
	for x in {k: v for k, v in sorted(similarityDict1.items(), key=lambda item: item[1], reverse=True)}:
		classificationList1.append([x,similarityDict1[x][0][0]])
	bestScore =  classificationList1[0][1]
	if float(bestScore < 0.40):
		return("")
		
	stringToPrint = word 
	for c in classificationList1[0:1]:
		stringToPrint = stringToPrint + "\t" + str(c[0]) + "\t" +  str(c[1])
		return(str(c[0]))

def computeSimilarity2 (word):
	wordEmb = model[word].reshape(1,-1)

	for category in catEmbDict2:
		catEmb = catEmbDict2[category].reshape(1,-1)
		cosine_value = cosine_similarity(catEmb, wordEmb)
		similarityDict2[category] = cosine_value

	classificationList2 = []
	for x in {k: v for k, v in sorted(similarityDict2.items(), key=lambda item: item[1], reverse=True)}:
		classificationList2.append([x,similarityDict2[x][0][0]])
	bestScore =  classificationList2[0][1]
	if float(bestScore < 0.5): 
		return("")
	stringToPrint = word 
	for c in classificationList2[0:1]:
		stringToPrint = stringToPrint + "\t" + str(c[0]) + "\t" +  str(c[1])
		return(str(c[0]))

sys.stderr.write("\n")
with open (listFile, 'r') as file:
	for line in file:
		if "_" in line:
			parts = line.split("_")

			if "noun" in line.lower():
				if "de" in lang:
					word = line
				else:
					word = line.strip().lower()
				word = word.split("_")[0]
				print(word,computeSimilarity1(word))

			if "adj"  in line.lower():
				if "de" in lang:
					word = line
				else:
					word = line.strip().lower()
				word = word.split("_")[0]
				print(word,computeSimilarity2(word))

file.close()		











