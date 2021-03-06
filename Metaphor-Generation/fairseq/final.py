import torch
from fairseq.models.bart import BARTModel
import os
import time
import numpy as np
os.environ['CUDA_VISIBLE_DEVICES']="2"


datadir = 'metaphor'
cpdir = 'checkpoint-'+datadir+'/'
bart = BARTModel.from_pretrained(cpdir,checkpoint_file='checkpoint_best.pt',data_name_or_path=datadir)

bart.cuda()
bart.eval()
np.random.seed(4)
torch.manual_seed(4)


count = 1
bsz = 1 #128
maxb = 30
minb = 7
print("done")
t = 0.7
elem = []
for val in [5]:
    with open('metaphor.source') as source, open('metaphor.hypo', 'w') as fout:
        sline = source.readline().strip()
        slines = [sline]
        for sline in source:
            if count % bsz == 0:
                with torch.no_grad():
                    hypotheses_batch = bart.sample(slines, sampling=True, sampling_topk=val, temperature=t, lenpen=2.0, max_len_b=maxb, min_len=minb, no_repeat_ngram_size=3)
                for hypothesis in hypotheses_batch:
                    fout.write(hypothesis.replace('\n','') + '\n')
                    fout.flush()
                slines = []

            slines.append(sline.strip())
            count += 1
        if slines != []:
            hypotheses_batch = bart.sample(slines, sampling=True, sampling_topk=val, temperature=t, lenpen=2.0, max_len_b=maxb, min_len=minb, no_repeat_ngram_size=3)
            for hypothesis in hypotheses_batch:
                fout.write(hypothesis.replace('\n','') + '\n')
                fout.flush()
