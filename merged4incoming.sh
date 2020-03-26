here=$(dirname $(grealpath $0))
export src=$HOME/.incoming
export BUILD=${here}/__build__
mkdir -p $BUILD

for fname in $(ls -1 $src) ; do
    PRE=$src/$fname
    POST=$BUILD/$fname.post
    echo $fname >&2
    [ -f "$PRE" ] && bin/main.py $PRE > $POST
done
cat $BUILD/*.post|sort|uniq
