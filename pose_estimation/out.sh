for f in movie_scene_2/*.jpg;
  do
  python demo_image.py --image "$f" --output Output/"$f";
done
