#!/bin/bash
echo "############# Started Building Thesis ################"
pdflatex thesis.tex
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex
echo "Finished building  - output file thesis.pdf"
echo "Opening the pdf file" 
open thesis.pdf
echo "Ended Shell script, exiting........ "

