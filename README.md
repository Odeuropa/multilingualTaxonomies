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


If you use this resource, please cite:

Stefano Menini, Teresa Paccosi, Serra Sinem Tekiroğlu, and Sara Tonelli (2022) *Building a Multilingual Taxonomy of Olfactory Terms with Timestamps*. In Proceedings of the Thirteenth Language Resources and Evaluation Conference, pages 4030–4039, Marseille, France. European Language Resources Association. [[Link]](https://aclanthology.org/2022.lrec-1.429/)

## Funding acknowledgement

<img src="https://github.com/Odeuropa/.github/raw/main/profile/eu-logo.png" width="80" height="54" align="left" alt="EU logo" />

This work has been realised in the context of [Odeuropa](https://odeuropa.eu/), a research project that has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No. 101004469.
