#! /bin/sh
set -e

python3 ./setup.py install --user
python3 ./simple_vignette.py --user
