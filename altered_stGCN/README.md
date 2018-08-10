### Installation
* pytorch
* openpose
* ```sh 
  cd torchlight; python setup.py install; cd .. 
```
* ```sh 
pip install moviepy
```
* ```sh 
sudo apt-get install ffmpeg
```
* Other dependencies, ```sh 
pip install -r requirements.txt
```


### Data Preperation
#### Place the [dataset](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/human-activity-recognition/mpii-cooking-activities-dataset/) and labels inside folder named, *Cooking_Activity*

> To resize the videos data into required format
```sh
$ bash resize.sh
```

> To sort labels
```sh
$ bash labels.sh
```

> To extract openpose skeletons on all data, run this script inside builtopenpose folder
```sh
$ cd openpose/  
$ bash execute_openpose.sh
```

> For placing train/val/test data, The script can be changed or ignored based on one's own requirement of splitting the data
```sh
$ cd train_test_data/
$ bash move_data.sh
```

> To prepare data (dumps all framewise skeletons for each video in train,test and val into one based on the videos present in the split)
```sh
$ bash prepare_data.sh
$ cd tools/
```

> To convert train/test/val/ pose_data into necessary format
```sh
$ bash convert_pose.sh
```

> Data Generation into npy and pkl files as required
```sh
$ cd ../
$ bash gendata.sh
```

### Training
```sh
$ python main.py recognition -c config/st_gcn/kinetics-skeleton/train.yaml --device 0 --batch_size 1
Note : parameters can be changed in train.yaml. Other parameters are --base_lr (val) --optimizer (eg. Adam). For using pretrained weights, --weights (path to weights) --ignore_weights (list of layers to ignore)
```


### Testing
```sh
$ python main.py recognition -c config/st_gcn/kinetics-skeleton/test.yaml --device 0 --batch_size 1 
Note : parameters can be changed in test.yaml
```
### Visualization
```sh
$ python main.py demo --video (path to video) --pose_input_dir (path to folder containing openpose skeletons) --output_dir (path to save the result video)
```


### Structure
```sh
.
├── config 
│   └── st_gcn
│       └── kinetics-skeleton
│           ├── demo.yaml
│           ├── test.yaml
│           └── train.yaml
├── Cooking_Activity
│   ├── data.py               (To modify data into required formats)
│   ├── labels.sh
│   └── resize.sh
│   └── per_video_trim.py     (trims videos class wise from the given dataset, after resizing is performed)
├── feeder
│   ├── feeder_kinetics.py    (Class to load data into test, train etc. Problems might arise with torchloader due to memory)
│   ├── feeder.py             
│   ├── __init__.py
│   └── tools.py
├── gendata.sh                
├── main.py
├── net
│   ├── __init__.py
│   ├── st_gcn.py             (Network Class)
│   └── utils
├── openpose
│   └── execute_openpose.sh   (To run openpose skeletons on videos)
├── processor
│   ├── demo.py               
│   ├── __init__.py
│   ├── io.py
│   ├── processor.py          (Processing the data that is being loaded, includes all hyperparameters)
│   └── recognition.py        (Contains functions for Train/Test accuracy calculation functions etc)
├── tools
│   ├── change_pose.py        (To convert raw poses obtained from openpose into required format)
│   ├── convert_pose.sh
│   ├── __init__.py
│   ├── kinetics_gendata.py   
│   └── utils
│       ├── openpose.py
│       ├── video.py
│       └── visualization.py  
├── torchlight
├── train_test_data
│   ├── move_data.sh 
│   ├── prepare_data.sh
│   ├── processed_data
│   ├── test
│   │   ├── data_list.dat
│   │   ├── folder_wise
│   │   │   └── all_json.sh
│   │   ├── test_json
│   │   └── videos
│   ├── train
│   │   ├── "Similar to test above"
│   └── val
│       └── "Similar to test above"
    
```
