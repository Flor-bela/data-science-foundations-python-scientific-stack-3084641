# %%
from sklearn.datasets import fetch_20newsgroups

corpus = fetch_20newsgroups(
    categories=['sci.space'],
    remove=['headers', 'footers'],
)
text = corpus['data'][4]
print(text)

# %%
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
doc
# It looks very much like the original text
# %%
# But if you look at the type of the document we are going to see that this is something else. 
type(doc)
# This document contains a lot of information about the text
# %%
# For example, we can list the document sentences
# And get the first sentence
# We can iterate over the sentences and look at the tokens.
sent = list(doc.sents)[1]
print(sent)

# %%
for tok in sent:
    print(f'{tok.text!r} -> {tok.tag_}')
# These tags: VB for verb, etc... is something that we need to learn about.
# %%
# The convention in Spacy is that attributes whithout underscore at the end are numeric 
# And one that ends with an underscore like the tag here are textual (tok.tag_)

# Document itselft also has entities or ents which are the names entities it can find
# So for every entity in the doc you print the text and the label of it.
for ent in doc.ents:
    print(f'{ent.text} ({ent.label_})')

# %%
