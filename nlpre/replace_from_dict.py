import os
import itertools
import collections
import re
import csv


class replace_from_dictionary(object):

    '''
    DOCSTRING: TO WRITE.
    '''

    def __init__(self, f_dict, prefix=''):

        if not os.path.exists(f_dict):
            msg = "Can't find dictionary {}".format(f_dict)
            raise IOError(msg)

        self.rdict = {}
        with open(f_dict) as FIN:
            csvfile = csv.DictReader(FIN)
            for row in csvfile:
                term = row["term"].lower()
                self.rdict[term] = '{}{}'.format(prefix, row["replacement"])

    def __call__(self, org_doc):

        doc = org_doc
        ldoc = doc.lower()

        # Identify which phrases were used and possible replacements
        R = collections.defaultdict(list)
        for key, val in self.rdict.iteritems():
            if key in ldoc:
                R[val].append(key)

        # Remove replacements that are substrings of another
        # "5' exonuclease", vs "3' 5' exonuclease"
        all_replacements = [x for v in R.values() for x in v]
        ignore_tokens = set()
        for k1, k2 in itertools.combinations(all_replacements, r=2):
            if len(k1) < len(k2) and k1 in k2:
                ignore_tokens.add(k1)

        # For each term, make replacements based off size order
        for term, replacements in R.iteritems():
            replacements = sorted(replacements, key=lambda x: -len(x))
            for rval in replacements:
                if rval in ignore_tokens:
                    continue
                pattern = re.compile(re.escape(rval), re.IGNORECASE)
                doc = pattern.sub(' {} '.format(term), doc)

        doc = ' '.join([x for x in doc.split(' ') if x])
        return doc


# if __name__ == "__main__":
#    P = replace_from_dictionary('MeSH_two_word_lexicon.csv',
#                                'nlpre/dictionaries')
#    text = '((11-Dimethylethyl)-4-methoxyphenol).'
#    print(P(text))
