#!/usr/bin/env python
import os, sys, nltk

def setup():

    # Download the nltk corpus first
    # python -m nltk.downloader all

    from nltk.corpus import brown
    from nltk.corpus import gutenberg
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.update([",", ".", "\"", ",\"","'",";", ".\"", "-", "?", "--", ":",
    "!\"", "?\"", "!", "?--", ".--", "!--", "\'" ,"\'\'", "``", "`", "(", ")",
    '."--', ';--', "--\"", "--\"",".'--",'"`',":--","--`" , ";'", "/",'.--"',
    ".'\"", "'--", ".'",".,","!\"--","''",",)"])

    #for fileid in gutenberg.fileids():
    fileid = "milton-paradise.txt"
    with open("output/gutenberg.%s.tokens" %fileid, 'wb') as out:
        for w in gutenberg.words(fileid):
            if w not in stop_words:
                out.write(u''.join(w).encode('utf-8').strip().replace('\n', ''))
                out.write(' ')
            # fix srilm ngram sentence length issue
        out.write('\n')
'''
    for fileid in brown.fileids():
        with open("output/brown.%s.tokens" %fileid, 'wb') as out:
            for w in brown.words(fileid):
                if w not in stop_words:
                    out.write(u''.join(w).encode('utf-8').strip())
                    out.write(' ')
                # fix srilm ngram sentence length issue
            out.write('\n')
'''
if __name__ == '__main__':
    setup()
