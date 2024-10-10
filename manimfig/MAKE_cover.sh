#!/bin/bash

QFLAG="-pqh -s" #options pql/pqh for low/high quality

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
