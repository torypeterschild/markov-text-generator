markov-text-generator
=====================

**Note**: markov-text-generator is a work in progress.

This is a Python implementation of a [Markov Text Generator](https://en.wikipedia.org/wiki/Markov_chain#Markov_text_generators) using [`TextBlob`](https://textblob.readthedocs.io/en/dev/index.html), a Python (2 and 3) library for processing textual data.

##How it works

Markov Text Generators generate original, superficially real-looking sentences based on a given source text. Each word is selected based on how often it follows the previous word, and the results are chained together to form a sentence.

The following was generated with this program using George Saunder's Pastoralia as source text:

> Around two there is no goat, just killed, sits in our shoes, you always
> said good, good fishing, son, and when you say it, I’m already deep into
> the cave was real and all, and you even come into my workplace and
> started swearing.” “Like you ever worked.” “Like jewelry making wasn’t
> work,” he says.

##License

markov-text-generator is licensed under the MIT License. See LICENSE for more information.