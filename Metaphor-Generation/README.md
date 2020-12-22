conda create --name metaphor python=3.6

conda activate metaphor

#point your LD_LIBRARY_PATH to your miniconda or anaconda library

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nas/home/tuhinc/miniconda3/lib/      (Use your own)





#INSTALL COMET
Code used from https://github.com/atcbosselut/comet-commonsense with modifications



  - install nltk
      
    - cd comet-commonsense
    
       To run the setup scripts to acquire the pretrained model files from OpenAI, as well as the ATOMIC and ConceptNet datasets

      ```
      bash scripts/setup/get_atomic_data.sh
      bash scripts/setup/get_conceptnet_data.sh
      bash scripts/setup/get_model_files.sh
      ```

      Then install dependencies (assuming you already have Python 3.6 ):

      ```
      pip install torch==1.3.1
      pip install tensorflow
      pip install ftfy==5.1
      conda install -c conda-forge spacy
      python -m spacy download en
      pip install tensorboardX
      pip install tqdm
      pip install requests
      pip install regex
      pip install pandas
      pip install ipython
      pip install inflect
      pip install pattern
      pip install pyyaml==5.1
      
      ```
      <h1> Making the Data Loaders </h1>

      Run the following scripts to pre-initialize a data loader for ATOMIC or ConceptNet:

      ```
      python scripts/data/make_atomic_data_loader.py
      python scripts/data/make_conceptnet_data_loader.py
      ```
      
      <h1> Download pretrained COMET </h1>
      
      First, download the pretrained models from the following link:

      ```
      https://drive.google.com/open?id=1FccEsYPUHnjzmX-Y5vjCBeyRt1pLo8FB
      ```

      Then untar the file:

      ```
      tar -xvzf pretrained_models.tar.gz
      
    
 Make sure your directory resembles this 
 https://github.com/tuhinjubcse/SarcasmGeneration-ACL2020/blob/master/comet-commonsense/directory.md
 

Clone "https://github.com/aparrish/gutenberg-poetry-corpus"
Please put the poetry corpus file `gutenberg-poetry-v001.ndjson` into path `data/poem`

In the code `preprocess.py`, `stanfordcorenlp` is needed. Please download http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip and unzip to `data/corenlp`.

We would require a BERT Fine-tuned model for metaphor detection first to identify naturally occuring metaphors
To finetune 
      
              cd vua_detection_ml
              cd bert
              sh run.bash
Alternatively download the model https://drive.google.com/file/d/1RmITw1LghnfjSXWPJ6NWGJXwGzgtdMR8/view?usp=sharing in this directory
              
To create parallel data using Commonsense Symbolism

```bash
cd data/poem
python preprocess.py
cd ../..
python poem.py
```

This creates poem_0.95_3.json
You can download it from here https://drive.google.com/file/d/10p3gh5JmDd_Vi2S3w1za_pmhtD4jjBjM/view?usp=sharing
createpaireddata.py takes this file can create literal metaphorical pairs


To train the metaphor generation model you can finetune BART. The steps are as follows


                                            
                                            cd fairseq
                                            sh script2.sh
                                            

                            
It creates a checkpoint-metaphor folder. Alternatively you can download from the drive link and place inside fairseq

https://drive.google.com/drive/folders/1P-OxMqCX1oD6jdVULQDMrpEeQjpOK-w2?usp=sharing


To train the discriminator you can finetune roberta-large. The steps are as follows


                                            
                                            cd fairseq
                                            sh roberta_train.sh
                                        
It creates a metaphor-roberta folder. 
To run on literal input , to generate metaphors
                                            
                                            
                                            python inference.py
                                            






Email me at tc2896@columbia.edu for any problems/doubts. Further you can raise issues on github, or suggest improvements.


