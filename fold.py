#!/usr/bin/env python
import os, sys

def fold():
    from sklearn.model_selection import KFold

    fvalidation = []
    for file in os.listdir('output'):
        if file.endswith('tokens'):
            fvalidation.append(file)

    print fvalidation
    # Create the ngram counts and ngram files for trigram of all the token files
    for file in fvalidation:
        #./ngram-count -text burton/prog.c -order 2 -addsmooth 1 -write burton.count -lm burton.lm
        os.system('./bin/ngram-count -text output/%s -addsmooth 1 -lm train/%s.lm -order 3 -interpolate' % (file, file))
        #os.system('./bin/ngram-count -text output/%s -lm train/%s.lm -order 3 -unk -kndiscount -wbdiscount3 -interpolate' % (file, file))
        os.system('./bin/ngram -lm train/%s.lm -order 3 -ppl -write train/%s.3grams.count' % (file, file))
        # ./ngram -lm corpus.lm -ppl test_corpus2.txt -debug 2

    kf = KFold(n_splits=10)
    foldcount = 0
    for train, test in kf.split(fvalidation):
        print("%s %s" % (train, test))
        trainlist = train.tolist()
        testlist = test.tolist()
        with open("train/fold%d.test" % foldcount, 'wb') as outtest:
            for testindex in testlist:
                testfile = fvalidation[testindex]
                #print("TEST %d %s" % (testindex, testfile))
                outtest.write(testfile + '\n')

        with open("train/fold%d.train" % foldcount, 'wb') as outtrain:
            for trainindex in trainlist:
                trainfile = fvalidation[trainindex]
                #print("TRAIN %d %s" % (trainindex, trainfile))
                outtrain.write(trainfile + '\n')

        foldcount += 1

        # TODO believe we can get rid of the lm files at this point and just leave the 3grams count files

if __name__ == '__main__':
    fold()
