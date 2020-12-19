import json
banned_verbs = ['is','Is','IS','Are','are','was','Was','were','Were']

f1 = open('literal.source','w')
f2 = open('metaphor.target','w')


for line in open('poem_0.9_3.json'):
	line = json.loads(line.strip())
	metaphorical = line["metaphorical"]
	position = line["position"]
	verb = line["verb"]
	meta_indices = metaphorical.split()
	symbols = line["symbol_lit"]
	lit_new = None
	for tup in line["literal"]:
		if tup[0] not in banned_verbs and (tup[1]>=4) and len(tup[0])>3 and (tup[0].lower() not in verb.lower()):
			lit_indices = metaphorical.split()
			lit_indices[position] = '<V> ' + tup[0]+ ' <V>'
			lit_new =  ' '.join(lit_indices)
			break
	if lit_new!=None:
		meta_indices[position] = '<V> ' + verb+ ' <V>'
		meta_new =  ' '.join(meta_indices)
		f1.write(lit_new+'\n')
		f2.write(meta_new+'\n')