""" axpy.plastic
    Copyright (C) 2022 gv-sh and contributors

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.

    Contact: gv-sh@outlook.com
"""

import os 
import cv2
import mip
import random 
import math
import numpy as np

ls              = lambda dir    : [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
read_img        = lambda dir, f : cv2.imread(os.path.join(dir, f))
read_vid        = lambda dir, f : cv2.VideoCapture(os.path.join(dir, f))

def load_dfx(path, margin=[0,0,0,0], size=64, padding=8):
    """ Load Data from Directory """

    frames = []

    files = ls(path)

    for file in files:
        if file.endswith('.jpeg'):
            frames.append(mip.roi(read_img(path, file), margin, size, padding))
            print('Read 1 frame from ' + file)
        if file.endswith('.mp4'):
            video = read_vid(path, file)
            success, frame = video.read()
            i = 0
            while success:
                frames.append(mip.roi(frame, margin, size, padding))
                success, frame = video.read()
                i += 1
            video.release()
            print('Read ' + str(i) + ' frames from ' + file)

    return frames

def augment(frames, target, flip=True, rotate=True):
    """ Augment the given frames """

    output_frames = []

    for i in range(target):
        frame = random.choice(frames)
        op = random.choice(['flip', 'rotate', None])

        if op == 'flip' and flip == True:
            output_frames.append(mip.flip_r(frame))
        elif op == 'rotate' and rotate == True:
            output_frames.append(mip.rotate_r(frame, -10, 10))
        else:
            output_frames.append(frame)

    return output_frames

def trace(frame, 
    features = { 'max_corners': 32, 'quality_level': 0.01, 'min_distance': 6, 'display': False },
    thickness = 2,
    distance_threshold = 16
    ):
    """ Trace the given frames

        Examples:
            >>> frames = get_frames('data')
            >>> traced_frames = trace(frames)
        
        Args:
            frames (list): frames to be traced
            features (dict): parameters for features
            draw_on_frame (bool): whether to draw on the frame
            distance_threshold (int): distance threshold
        
        Returns:
            (list): List of traced frames
    """

    alpha = 1 if thickness == 1 else 0.5
    radius = 2 if thickness == 1 else 1


    corners = cv2.goodFeaturesToTrack(frame,features['max_corners'],features['quality_level'],features['min_distance'])
    w,h = frame.shape

    blank = np.zeros((w,h), np.uint8)

    if corners is not None:
        corners = np.int0(corners)
        for i in corners:
            x,y = i.ravel()
            if features['display'] == True:
                cv2.circle(blank,(x,y),radius,255*alpha,-1, cv2.LINE_AA)

        # Draw lines between corners
        for i in range(len(corners)):
            for j in range(len(corners)):
                if i != j:
                    x1,y1 = corners[i].ravel()
                    x2,y2 = corners[j].ravel()

                    # Calculate distance between corners
                    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                    if dist < distance_threshold:
                        cv2.line(blank, (x1,y1), (x2,y2), 255 * alpha, 1 , lineType=cv2.LINE_AA)
    
    return blank
