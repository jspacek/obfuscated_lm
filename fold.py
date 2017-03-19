#!/usr/bin/env python
import os, sys, fileinput

def fold():
    from sklearn.model_selection import KFold

    fvalidation = []
    for file in os.listdir('output'):
        if file.endswith('tokens'):
            fvalidation.append(file)

    print fvalidation

    # Create a 10 fold cross validation with randomized order
    kf = KFold(n_splits=10, shuffle=True)
    foldcount = 0
    for train, test in kf.split(fvalidation):
        print("%s %s" % (train, test))
        trainlist = train.tolist()
        testlist = test.tolist()
        # Put all of the training file tokens into the current fold training
        with open("train/fold%d.train" % foldcount, 'wb') as outtrain:
            for trainindex in trainlist:
                ftrain = 'output/%s' % fvalidation[trainindex]
                fin = fileinput.input(ftrain)
                for line in fin:
                    outtrain.write(line)
                fin.close()

        # Generate a language model for this fold's concatenated training file
        os.system('./bin/ngram-count -text train/fold%d.train -addsmooth 1 -lm train/fold%d.train.kn.lm.gz -order 3 -interpolate'
        % (foldcount, foldcount))

        with open("train/fold%d.test" % foldcount, 'wb') as outtest:
            for testindex in testlist:
                ftest = fvalidation[testindex]
                print("TEST %d %s" % (testindex, ftest))
                # Record the tested files in this fold
                outtest.write(ftest + '\n')
                # test the file on trigrams with debug set to word level and record perplexity
                os.system('./bin/ngram -lm train/fold%d.train.kn.lm.gz -order 3 -ppl output/%s -write-lm train/fold%d.%s.3grams -debug 2 > train/fold%d.%s.3grams.count'
                % (foldcount, ftest, foldcount, ftest, foldcount, ftest))

        foldcount += 1

if __name__ == '__main__':
    fold()
