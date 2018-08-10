
#Test:
echo "Testing Started...."
python change_pose.py --videos_path /home/vinay/gsoc2018-vinay/train_test_data/test/videos --openpose_json_path /home/vinay/gsoc2018-vinay/train_test_data/test/test_json --stgcn_json_path /home/vinay/gsoc2018-vinay/train_test_data/processed_data/kinetics_test/ --video_list_file /home/vinay/gsoc2018-vinay/train_test_data/test/data_list.dat
echo "Testing Done!"

#Val:
echo "Validation Started...."
python change_pose.py --videos_path /home/vinay/gsoc2018-vinay/train_test_data/val/videos --openpose_json_path /home/vinay/gsoc2018-vinay/train_test_data/val/val_json --stgcn_json_path /home/vinay/gsoc2018-vinay/train_test_data/processed_data/kinetics_val/ --video_list_file /home/vinay/gsoc2018-vinay/train_test_data/val/data_list.dat
echo "Validation Done!"

#Train:
echo "Training Started...."
python change_pose.py --videos_path /home/vinay/gsoc2018-vinay/train_test_data/train/videos --openpose_json_path /home/vinay/gsoc2018-vinay/train_test_data/train/train_json --stgcn_json_path /home/vinay/gsoc2018-vinay/train_test_data/processed_data/kinetics_train/ --video_list_file /home/vinay/gsoc2018-vinay/train_test_data/train/data_list.dat
echo "Training Done!"
