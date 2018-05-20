#! /bin/sh
# /etc/init.d/redirection
#ajouter au fichier
#sudo chmod 755 /etc/init.d/redirection
#sudo update-rc.d redirection defaults
#remove
#sudo update-rc.d -f redirection remove

# The following part always gets executed.
echo "Start the redirection"

python /home/debian/Documents/maximefranco/redirection.py 80
