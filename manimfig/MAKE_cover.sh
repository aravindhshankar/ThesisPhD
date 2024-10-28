#!/bin/bash

QFLAG="-pqk -s" #options pql/pqh/pqk for low/high/k quality

echo "######### MAKE Hyperbolae shell script ##########"
manim $QFLAG cover_try.py Hyperbolae
#
echo "######### MAKE BackPage shell script ##########"
manim $QFLAG cover_try.py BackPage
#
echo "######## MAKE MIddleStrip #################"
manim $QFLAG middle_strip.py MiddleStrip
#
echo "Finished making covers. Exiting ........"
