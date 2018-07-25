#!/bin/sh
# to combine .out files to make the summary of transcriptome alignment
for file in ~/my1stproj/bucket/quantitation/rsem_hg38/*.rsem.out
do
    awk 'NR==8 {print FILENAME f,$1}' "$file" >> alignmentSummary.txt
done
