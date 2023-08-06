#!/usr/bin/env python3
import sys
import csv
import os


def psl_to_bed(infile):
    '''Convert psl format to bed'''

    # TODO: maybe use yield?
    if infile[-3:].lower() == 'bed':
        return infile
    elif infile[-3:].lower() == 'psl':
        bed = infile + '.bed'
        with open(bed, 'wt') as outfile:
            writer = csv.writer(outfile, delimiter='\t', lineterminator=os.linesep)
            for line in infile:
                line = line.rstrip().split('\t')
                if len(line) < 21:
                    sys.stderr.write('fewer than 21 columns in the psl file, exiting\n')
                    sys.exit(1)
                chrom, name, start, end = line[13], line[9], line[15], line[16]
                strand, blocksizes = line[8], line[18]
                starts = line[20].split(',')[:-1]
                relstarts = ','.join([str(int(n) - int(start)) for n in starts]) + ','
                writer.writerow([chrom, start, end, name, '1000', strand, start, end, '0,0,0',
                    str(len(starts)), blocksizes, relstarts])
        return bed
    else:
        sys.stderr.write(f'do not understand format of {infile}, should be psl or bed')
        sys.exit()
