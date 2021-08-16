# fastfinder
The program is intended for extraction of sequence from a large FASTA (e.g. genome) file using sequence (chromosome, scaffold) name and start-end coordinates.

The FASTA file must be first indexed using samtools:
   samtools faidx genome-file.fasta

Example of use:
   fastfinder.py genome-file.fasta chr1 603062454 603074454 out.txt

In this example:
   genome-file.fasta - a large (genome) FASTA file
   chr1 - the name of the sequence in a file
   603062454 - start coordinate in the sequence 'chr1'
   603074454 - end coordinate in the sequence 'chr1' 
   out.txt - output file
