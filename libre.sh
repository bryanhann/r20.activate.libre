export src=$HOME/bch/incoming
export dst=./_build
mkdir -p $dst

function abc () {
    [ -d "$src/$1" ] && return
    #python ./stamp-libre.py $src/$1 >> $dst/acc && cp $src/$1 $dst/$1 || >&2 echo $ii bad
    python ./libre.py $src/$1 >> $dst/$1 && mv $dst/$1 $dst/$12.post  || >&2 echo $ii bad
}

if [ "$1" == "compile" ] ; then
    for fname in $(ls -1f $src) ; do
        abc $fname
    done
    cat $dst/*.post|sort|uniq > $dst/merged
    exit    
    fi
if [ "$1" == "cat" ] ; then
    cat $dst/merged
    exit
    fi
    
echo usage:
echo $0 compile
echo $0 cat
