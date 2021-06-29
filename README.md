# multilingualTaxonomies


The folder taxonomies contains the first version of the multilingual taxonomy of olfactory terms. The taxonomy is available in English, French, German, Dutch, Italian and Slovenian, and has been created semi-automatically, starting from a core set of WordNet synsets and extending them with co-occurring terms using n-grams. 

For each language, we release two files in tab-separated format. 

The first file, ending with `_taxonomy` contains the following columns:

* `entry`: term listed in the taxonomy
* `source`: whether the term comes from the WordNet-based core taxonomy or has been obtained through n-gram co-occurrences.
* `synset`: if it comes from WordNet, which is the synset unique identifier
* `first appearance`: if it comes from co-occurrences, in which year it appeared first (if n-grams contain temporal information)
* `time periods`: for each time period between 1650 and 1925 (spans of 50 years), whether the term is mentioned or not
* `smell-source`: for nouns in English, Italian, German and French, to which category of smell sources it was assigned (see Section \ref{categorisation})
* `quality`: for adjectives in English, Italian, German and French, to which category of qualities it was assigned (see Section \ref{categorisation}) 


The second file, ending with `_co-occurences`, contains information about pairs of co-occurring terms (i.e. seed word + co-occurring term with high PMI) extracted from n-grams. Each file in tsv format contains the following columns:


* `seed word + part of speech`
* `co-occurring term`
* `time span`: when the two terms were found (if found in multiple time spans, the row is repeated with different values)
* `frequency`: number of times the two terms were co-occurring in the given time span
* `total tokens`: number of overall tokens present in the n-grams for the given time period, to be used as a reference or to normalise the frequency
