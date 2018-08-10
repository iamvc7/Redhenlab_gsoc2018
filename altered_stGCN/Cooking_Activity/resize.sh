
for file in ./videos/*
do
        echo $file "is being Resized to 340*256"
	ffmpeg -i $file -r 30 -s 340*256 -c:v libx264 -b:v 3M -strict -2 -movflags faststart ./resized_videos/"$(basename "$file")"
done
