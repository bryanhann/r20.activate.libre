r20export R20_LIBRE $(dirname $(grealpath $0))
r20export R20_LIBRE_incoming ${HOME}/.incoming
r20_libre_file  () {${R20_LIBRE}/scripts/main.py $1;}
r20_libre_raw   () {__map__ r20_libre_file $(__ls__ $R20_LIBRE_incoming);}
r20_libre_parse () {r20_libre_raw|sort|uniq;}

