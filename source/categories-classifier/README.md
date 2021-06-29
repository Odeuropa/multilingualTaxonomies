# categories-classifier

This script classifies a list of words in English, Italian, French, German, Dutch or Slovenian into one of the following categories.

Nouns can be calssified as:
* CATEGORY|emissions_traffic|fuel|dust
* CATEGORY|industry
* CATEGORY|food|beverage
* CATEGORY|tobacco|smoke
* CATEGORY|cleaning|medicinal
* CATEGORY|synthetic
* CATEGORY|waste_garbage|pee|vomit|excrement|rotten
* CATEGORY|animal|people
* CATEGORY|nature_flowers|plant|tree|soil

While adjectives can be:
* CATEGORY|Fragrant|fruity|floral
* CATEGORY|woody/earthy/mouldy
* CATEGORY|chemical|hydro-carbons|synthetic
* CATEGORY|fresh
* CATEGORY|sweet|spicy
* CATEGORY|smoky|toasted|burnt|fatty
* CATEGORY|decayed
* CATEGORY|pungent

The input is a file with a word per line followerd by its POS (underscore separated), e.g.

bergamot_noun
disgusting_adj
cigar_noun

An example of the input file is available in `sample_input.txt `


To run the code use:
```
pip3 install -r requirements.txt
```

```
python3 categories-classifier.py -l en -f sample_input.txt
```
The classifier relies on fastText embeddings, if the script doesn't find the models in the script folder it automatically download them. If you already have them in a different folder or if you want to move them it is possible to specify the path with '-e'.


Parameters:
* `-l`, `--language`, set the language of the input file. Supported languages are [en,it,de,fr,nl,sl]
* `-f`, `--inputFile`, path of the file with the words list, the sample_input.txt file is provide to check if the script works properly
* `-e`, `--embeddingsFile`, this paramether is optional, if you have fastText embedings in a different location you can set the path with this option

