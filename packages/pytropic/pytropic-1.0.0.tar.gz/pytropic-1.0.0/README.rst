========
Pytropic
========

[![Python package](https://github.com/willf/pytropic/actions/workflows/test.yml/badge.svg)](https://github.com/willf/pytropic/actions/workflows/test.yml)


<img alt="An python with a lot of entropy" src="https://user-images.githubusercontent.com/37049/192400489-7a2fdc49-b29a-4299-a1c6-97c8b97b2eaf.png" width=150>



Train and predict string entropy based on character n-grams

## Features

-   Train a model on a corpus of text
-   multiple n-gram sizes
-   Can name models

## Example

Train a model on a corpus of text


..ipython::
        In [1]: from pytropic import pytropic

        In [2]: en = pytropic.Model(name='English 3-gram', size=3)

        In [3]: fr = pytropic.Model(name='French 3-gram', size=3)

        In [4]: with open('./corpora/bible-english.txt') as f:
        ...: en.train(f)
        ...:

        In [5]: with open('./corpora/bible-french.txt') as f:
        ...: fr.train(f)
        ...:

        In [6]: t = {'en': en, 'fr': fr}

        In [7]: min(t, key=lambda x: t[x].entropy("this is a test"))
        Out[7]: 'en'

        In [8]: min(t, key=lambda x: t[x].entropy("c'est un test"))
        Out[8]: 'fr'
