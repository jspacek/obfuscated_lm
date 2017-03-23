#!/usr/bin/env python
import os, sys

def processresults(indir, outfile):
    # 10 folds have each 9 grams tested, 90 results
    foldresults = [0,0,0,0,0,0,0,0,0]
    foldcounts = [0,0,0,0,0,0,0,0,0]
    oldfoldnumber = 0
    foldnumber = 0

    for root, dirs, filenames in os.walk(indir):
        for fname in filenames:
            if fname.endswith('.count'):
                print "Processing results of " + fname
                a,b,c,d,e,f = fname.split(".")
                foldnumber = (int)(a.split("fold",1)[1])

                if oldfoldnumber != foldnumber:
                    printresults(outfile, foldresults, foldcounts, foldnumber, oldfoldnumber)
                    # Reset array
                    foldresults = [0,0,0,0,0,0,0,0,0]
                    foldcounts = [0,0,0,0,0,0,0,0,0]
                    oldfoldnumber = foldnumber

                ngram = (int)(e.split("gram")[0])
                print "Fold number %s" % foldnumber
                print "ngram %s" % ngram
                fp = open("%s/%s" % (indir, fname))
                for i, line in enumerate(fp):
                    if i == 1: #2nd line with perplexity measure
                        # 0 zeroprobs, logprob= -60.26888 ppl= 35.10395 ppl1= 87.93414
                        a,b,c,d,e,f,g,h = line.split(" ")
                        ppl = (float) (f)
                        print "f %s" % f
                        print "PPL %f" % ppl
                # Add in the perplexity and another test count for this ngram
                foldresults[ngram-1] = foldresults[ngram-1] + ppl
                foldcounts[ngram-1] = foldcounts[ngram-1] + 1

        printresults(outfile, foldresults, foldcounts, foldnumber, oldfoldnumber)

def printresults(outfile, foldresults, foldcounts, foldnumber, oldfoldnumber):
    print "**********\nPrinting fold %d \n************\n" % oldfoldnumber
    # Output the fold results to a file
    fresults = '%s.%d.results' % (outfile, oldfoldnumber)
    with open(fresults, 'wb') as out:
        out.write("Fold %d \n" % oldfoldnumber)
        out.write("\n".join(str(elem) for elem in foldresults))
        out.write("\nFold counts \n")
        out.write("\n".join(str(elem) for elem in foldcounts))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: ./tokenize.py indir outfile'
        sys.exit(1)

    indir = sys.argv[1]
    outfile = sys.argv[2]
    processresults(indir, outfile)
