
for file in /home/vinay/gsoc2018-vinay/Cooking_Activity/resized_videos/*
do
        echo $file
        mkdir ./openpose/openpose_json/"$(basename "$file")"
        /home/vinay/openpose/build/examples/openpose/openpose.bin --video $file --write_video /home/vinay/openpose/video_out/"$(basename "$file")" --write_json /home/vinay/openpose/openpose_json/"$(basename "$file")"/ --display 0 --model_pose COCO
done

cp -r video_out/ /home/vinay/gsoc2018-vinay/Cooking_Activity/
cp -r openpose_json/ /home/vinay/gsoc2018-vinay/Cooking_Activity/
