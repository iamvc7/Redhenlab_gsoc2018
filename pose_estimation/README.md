> Pose estimation using pretrained models and without using openpose (Structure)
```sh
├── config
├── config_reader.py
├── demo_for_all_frames.py                    (Pose estimation for a folder containing images)
├── demo_image.py                             (Pose estimation for a single image)
├── model.py                                  (Model in keras from scratch, adapted version)
├── models
├── out.sh 
├── pose_classification
│   ├── labanotation_based_label_name.txt     (Names of low level actions defined)
│   └── pose_classification.py                (Keras MLP network for different pose vector classification, works very well for limited number of poses)
├── README.md
├── simple_pose_opencv.py                     (OpenCV based pose using pretrained caffe pose models availble)
├── util.py                                   (Writing colour labels over RGB images)
└── video_to_frames.py                        (Video to frames script)

```
