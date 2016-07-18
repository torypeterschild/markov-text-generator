markov-text-generator
=====================

**Note**: markov-text-generator is a work in progress.

This is a Python implementation of a [Markov Text Generator](https://en.wikipedia.org/wiki/Markov_chain#Markov_text_generators) using [`TextBlob`](https://textblob.readthedocs.io/en/dev/index.html), a Python (2 and 3) library for processing textual data.

##How it works

Markov Text Generators generate original, superficially real-looking sentences based on a given source text. Each word is selected based on how often it follows the previous word, and the results are chained together to form a sentence.

Using a Markov Text Generator with The Wonderful Wizard of Oz as the source text might result in the following:

> Dorothy lived in the doorway and looked upon her right foot and said: "Oz has sent for
> you." So the Wizard in the basket. "Good-bye!" "Good-bye!" shouted everyone, and all eyes
> were turned upward to where the Great Oz." "Oh, indeed!" exclaimed the man. "He has more
> brains than he needs." "And I am something terrible." "But, I don't care who kills her. But
> until she is melted," explained the Scarecrow. He had been cut. "There," said he; "now you
> have earned the brains you will oil the joints of my legs, I shall know everything."

##License

markov-text-generator is licensed under the MIT License. See LICENSE for more information.