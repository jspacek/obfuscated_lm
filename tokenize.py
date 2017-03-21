#!/usr/bin/env python
import os, sys

def tokenize(indir, outdir):

    for root, dirs, filenames in os.walk(indir):
        for fname in filenames:
            if fname.endswith('.c'):
                print "Preprocessing " + fname
                # Remove anything not in the C grammar using remccoms3.sed
                # Place the sanitized file in the output folder
                sanitizedfile = '%s/%s.sanitized' % (outdir, fname)
                os.system("cat input/%s | ./bin/remccoms3.sed | sed '/^\s*$/d' > %s"
                % (fname, sanitizedfile))
                os.system("cat input/%s | ./bin/remccoms3.sed | sed -e '/#include/d;/#define/d' > %s"
                % (fname, sanitizedfile))
                # Tokenize the sanitized file using the C lexer
                os.system('java -jar bin/LexC-1.0.jar %s' % sanitizedfile)
            elif fname.endswith('.java'):
                print "Preprocessing " + fname
                # Tokenize the sanitized file using the Java lexer
                os.system('java -jar bin/LexJava-1.0.jar %s/%s' % (indir, fname))
            else:
                print "Invalid file " + fname

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: ./tokenize.py outdir traindir'
        sys.exit(1)

    indir = sys.argv[1]
    outdir = sys.argv[2]
    tokenize(indir, outdir)
