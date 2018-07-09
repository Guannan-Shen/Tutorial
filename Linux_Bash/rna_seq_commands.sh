# this is a list of commands useful in RNAseq pipeline
# the following is shebang
#!/bin/sh
more [file_name]  # to view file
# using ctrl + z to quit the more 

gunzip [file_name] # unzip one file, it takes time for large .fastq.gz file

gzip [file_name]  # compress the file, compress the .fastq

## cp copy file from one dir to another dir

## set path to python 3.5

## for the test proj, trim
python trimBatch.py -c --cutadapt-q 20 --cutadapt-m 20 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -U -o /home/datasets/RNAseq/rawtest -i .fastq.gz /home/datasets/RNAseq/rawtest


