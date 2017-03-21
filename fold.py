#!/usr/bin/env python
import os, sys, fileinput

def fold(ngramorder, outdir, traindir):
    from sklearn.model_selection import KFold

    fvalidation = []
    for file in os.listdir(outdir):
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
        with open("%s/fold%d.train" % (traindir, foldcount), 'wb') as outtrain:
            for trainindex in trainlist:
                ftrain = '%s/%s' % (outdir, fvalidation[trainindex])
                fin = fileinput.input(ftrain)
                for line in fin:
                    outtrain.write(line)
                fin.close()

        # Generate a language model for this fold's concatenated training file
        # -addsmooth 0
        os.system('./bin/ngram-count -text %s/fold%d.train -interpolate -unk -addsmooth 0 -lm %s/fold%d.train.kn.lm.gz -order %d'

        #os.system('./bin/ngram-count -text %s/fold%d.train -addsmooth 1 -lm %s/fold%d.train.kn.lm.gz -order %d -interpolate'
        % (traindir, foldcount, traindir, foldcount, ngramorder))

        with open("%s/fold%d.test" % (traindir, foldcount), 'wb') as outtest:
            for testindex in testlist:
                ftest = fvalidation[testindex]
                print("TEST %d %s" % (testindex, ftest))
                # Record the tested files in this fold
                outtest.write(ftest + '\n')
                # test the file on trigrams with debug set to word level and record perplexity
                os.system('./bin/ngram -lm %s/fold%d.train.kn.lm.gz -order %d -ppl %s/%s -write-lm %s/fold%d.%s.%dgrams > %s/fold%d.%s.%dgrams.count'

                #os.system('./bin/ngram -lm train/fold%d.train.kn.lm.gz -order %d -ppl %s/%s -write-lm train/fold%d.%s.%dgrams -debug 2 > train/fold%d.%s.%dgrams.count'
                % (traindir, foldcount, ngramorder, outdir, ftest, traindir, foldcount, ftest, ngramorder, traindir, foldcount, ftest, ngramorder))

        foldcount += 1

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: ./fold.py ngramorder outdir traindir'
        sys.exit(1)

    ngramorder = int(sys.argv[1])
    outdir = sys.argv[2]
    traindir = sys.argv[3]
    fold(ngramorder, outdir, traindir)
