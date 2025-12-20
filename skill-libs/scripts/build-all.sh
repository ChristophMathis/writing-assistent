
cd `dirname $0`/..
root=`pwd`
dist=$root/dist

for i in `find claude -type d -name "_*" -prune -o -type d -print `
do
  if [ -f $i/SKILL.md ]
  then
      here=`dirname $i`
      local=`basename $i`
      echo $local at $here
      (cd $here; zip -r $dist/$local * )
  fi
done
