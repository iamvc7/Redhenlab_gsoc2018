
for file in /home/paperspace/Cooking_Activity/resized_videos/*
do
        echo $file
        python trim.py --video /home/paperspace/Cooking_Activity/resized_videos/"$(basename "$file")" --res /home/paperspace/Cooking_Activity/trimmed_videos/"$(basename "$file")"
done
