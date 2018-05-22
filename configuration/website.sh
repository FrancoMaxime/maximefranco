#! /bin/sh
# /etc/init.d/website

# The following part always gets executed.
echo "Start the redirection"

python /home/debian/Documents/maximefranco/redirection.py 80
