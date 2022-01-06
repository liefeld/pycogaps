#!/bin/sh

docker run -v $PWD:$PWD -w $PWD -t liefeld/pycogaps:latest python /home/user/pycogaps/simple_vignette.py ${PWD}/data/GIST.csv ${PWD}/data/GIST_out.pkl


