DEST_PATH='/home/vinay/gsoc2018-vinay/train_test_data/train/train_json'
for d in */; do
echo "$d"
cd "$d"
for file in *;do
  cp $file "$DEST_PATH"
done
cd ..
done
exit 1
