while read p; do
  echo "$p"
  grep "$p" "dwnominate_112.csv" >> dwnoms.txt
done <src.txt 