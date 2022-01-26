# multilingualTaxonomies


The folder `taxonomies-v2` contains the multilingual taxonomy of olfactory terms developed within the ODEUROPA project. The taxonomy is available in English, French, German and Italian (with ongoing work to add Dutch and Slovenian), and has been created semi-automatically, starting from a core set of WordNet synsets and extending them with co-occurring terms using n-grams. 

For each language, we release a files in tab-separated format, and an Excel file containing all the languages.

They contain the following columns:

* `entry`: term listed in the taxonomy
* `source`: whether the term comes from the WordNet-based core taxonomy or has been obtained through n-gram co-occurrences.
* `synset`: if it comes from WordNet, which is the synset unique identifier
* `first appearance`: if it comes from co-occurrences, in which year it appeared first (if n-grams contain temporal information)
* `time periods`: for each time period between 1650 and 1925 (spans of 50 years), whether the term is mentioned or not
* `smell-source`: for nouns in English, Italian, German and French, to which category of smell sources it was assigned (see Section \ref{categorisation})
* `quality`: for adjectives in English, Italian, German and French, to which category of qualities it was assigned (see Section \ref{categorisation}) 

