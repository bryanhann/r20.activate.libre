export R20LIBRE=$(dirname $(grealpath $0))
source ${XDG_CONFIG_HOME}/r20/libre/activate.sh
r20libre_file  () {${R20LIBRE}/scripts/main.py $1;}
r20libre_raw   () {__map__ r20libre_file $(__ls__ $R20LIBRE_incoming);}
r20libre_parse () {r20libre_raw|sort|uniq;}

