import os
import os.path
import warnings

NGRAM_SIZE = 3
CORPUS_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "corpus",
        "custom",
    )
)

import nltk

class Generator(object):
    _content_model = None

    def __init__(self, content_model=None):
        if content_model is None and self._content_model is None:
            self._create_content_model()
        elif content_model is not None:
            self._content_model = content_model

    def _create_content_model(self):
        reader = nltk.corpus.PlaintextCorpusReader(CORPUS_DIR, ".*.txt")
        sentences = reader.sents()
        self._content_model = nltk.NgramModel(2, sentences)

    def __call__(self, count=10):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            retval = " ".join(self._content_model.generate(count))\
                .replace(' .', '.')\
                .replace(". .", "..")\
                .replace(' ,', ',')\
                .replace('.,', '.')\
                .replace(',.', ',')
            if retval[-1] != '.':
                retval = "{0}.".format(retval)

        return retval

if __name__ == "__main__":
    x = Generator()
    print x()