cd train/folder_wise/
bash all_json.sh
cd ../..
echo "Done!"
cd test/folder_wise/
echo "Preparing Test Data...."
bash all_json.sh
cd ../..
echo "Done!"
cd val/folder_wise/
echo "Preparing Validation Data..."
bash all_json.sh
cd ../..
echo "Done!"
