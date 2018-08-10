
cd ~/openpose/
cp -r openpose_json/ video_out/ ../gsoc2018-vinay/train_test_data/
cd ../gsoc2018-vinay/train_test_data/video_out/
mv s19-* ../test/videos/
mv s17-* s18-* s20-* ../val/videos/
mv *.avi ../train/videos/
cd ../
rm -r video_out/
cd openpose_json/
mv s17-* s18-* s20-* ../val/folder_wise/
mv s19-* ../test/folder_wise/
mv *.avi ../train/folder_wise/
cd ../
rm -r openpose_json/
