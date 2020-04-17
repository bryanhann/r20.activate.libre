export R20LIBRE=$(dirname $(grealpath $0))
source ${XDG_CONFIG_HOME}/r20/libre/activate.sh
r20_libre_file  () {${R20LIBRE}/scripts/main.py $1;}
r20_libre_raw   () {__map__ r20_libre_file $(__ls__ $R20LIBRE_incoming);}
r20_libre_parse () {r20_libre_raw|sort|uniq;}

