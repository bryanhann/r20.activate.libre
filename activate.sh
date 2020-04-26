r20_libre_file  () { $(r20root libre)/scripts/main.py $1;}
r20_libre_raw   () {__map__ r20_libre_file $(__ls__ $R20_libre_CFG_incoming);}
r20_libre_parse () {r20_libre_raw|sort|uniq;}

