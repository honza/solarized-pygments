#/bin/env sh

# Create a virtualenv, install pygments and symlink the style file to the right
# place
#
# Requires virtualenv

PWD=`pwd`
virtualenv env
source env/bin/activate
pip install pygments
ln -s $PWD/solarized.py $PWD/env/lib/python2.7/site-packages/pygments/styles/solarized.py
mkdir _build
