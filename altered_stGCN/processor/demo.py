
import os
import argparse
import json
import shutil

import numpy as np
import torch
import skvideo.io

from .io import IO
import tools
import tools.utils as utils

class Demo(IO):
    def start(self):

        video_name = self.arg.video.split('/')[-1].split('.')[0]
        #print(video_name)
        output_result_dir = self.arg.output_dir
        output_result_path = f'{output_result_dir}/{video_name}.mp4'
        label_name_path = './resource/kinetics_skeleton/n_label.txt'
        with open(label_name_path) as f:
            label_name = f.readlines()
            label_name = [line.rstrip() for line in label_name]

        output_snippets_dir = '/home/paperspace/st-gcn/openpose_output/'
        video = utils.video.get_video_frames(self.arg.video)
        height, width, _ = video[0].shape
        video_info = utils.openpose.json_pack(
            output_snippets_dir, video_name, width, height)
        #print (height)
        #print (len(video_info['data']))
        pose, _ = utils.video.video_info_parsing(video_info)
        data = torch.from_numpy(pose)
        data = data.unsqueeze(0)
        data = data.float().to(self.dev).detach()

        self.model.eval()
        output, feature = self.model.extract_feature(data)
        output = output[0]
        feature = feature[0]
        intensity = (feature*feature).sum(dim=0)**0.5
        intensity = intensity.cpu().detach().numpy()
        label = output.sum(dim=3).sum(dim=2).sum(dim=1).argmax(dim=0)
        label = label/10

        label_sequence = output.sum(dim=2).argmax(dim=0)
        label_name_sequence = [[label_name[p/10] for p in l ]for l in label_sequence]
        edge = self.model.graph.edge
        images = utils.visualization.stgcn_visualize(
            pose, edge, intensity, video,label_name[label] , label_name_sequence, self.arg.height)

        if not os.path.exists(output_result_dir):
            os.makedirs(output_result_dir)
        writer = skvideo.io.FFmpegWriter(output_result_path,
                                        outputdict={'-b': '300000000'})
        for img in images:
            writer.writeFrame(img)
        writer.close()
        print(f'The Demo result has been saved in {output_result_path}.')

    @staticmethod
    def get_parser(add_help=False):
        parent_parser = IO.get_parser(add_help=False)
        parser = argparse.ArgumentParser(
            add_help=add_help,
            parents=[parent_parser],
            description='Demo for Spatial Temporal Graph Convolution Network')
        parser.add_argument('--video',
            default='./resource/media/skateboarding.mp4',
            help='Path to video')
        parser.add_argument('--output_dir',
            default='./final_output/',
            help='Path to save results')
        parser.add_argument('--height',
            default=1080,
            type=int,
            help='Path to save results')
        parser.set_defaults(config='./config/st_gcn/kinetics-skeleton/demo.yaml')
        parser.set_defaults(print_log=False)

        return parser

