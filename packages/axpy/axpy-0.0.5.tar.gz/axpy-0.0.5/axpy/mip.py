""" axpy.mip
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

import cv2 
import numpy as np 
import random   

width           = lambda M          : M.shape[1]                                                                # Width of the image
height          = lambda M          : M.shape[0]                                                                # Height of the image
long            = lambda M          : max(height(M), width(M))                                                  # Long side of the image
short           = lambda M          : min(height(M), width(M))                                                  # Short side of the image

scale           = lambda M, s       : cv2.resize(M, s, interpolation=cv2.INTER_AREA)                            # Scale the image
scale_w         = lambda M, w       : scale(M, (w, int(height(M)*(w/width(M)))))                                # Scale the image width
scale_h         = lambda M, h       : scale(M, (int(width(M)*(h/height(M))), h))                                # Scale the image height
scale_l         = lambda M, s       : scale_w(M, s) if width(M)>height(M) else scale_h(M, s)                    # Scale the image to long side 

crop            = lambda M, m       : M[m[0]:height(M)-m[1], m[2]:width(M)-m[3]]                                # Crop the image

gray            = lambda M          : cv2.cvtColor(M, cv2.COLOR_BGR2GRAY)                                       # Convert to grayscale
binary          = lambda M, x       : cv2.threshold(M, x, 255, cv2.THRESH_BINARY)[1]                            # Convert to binary
invert          = lambda M          : cv2.bitwise_not(M)

as_np           = lambda M          : np.array(M, dtype=np.float16)
norm            = lambda M          : M / max(1, M.max())
interp          = lambda M, x, y    : np.interp(M, (M.min(), M.max()), (x, y)).astype(np.uint8)                 # Interpolate the image

canny           = lambda M, x, y    : cv2.Canny(M, x, y)                                                        # Canny edge detection
dilate          = lambda M, k, i    : cv2.dilate(M, (k, k), iterations=i)                                       # Dilate the image
filter2d        = lambda M, K       : cv2.filter2D(M, -1, K)                                                    # Apply a 2D filter to the given image

empty           = lambda w, h       : np.zeros((h, w))                                                          # Create a blank image
empty_s         = lambda a          : empty(a, a)                                                               # Create a blank square image
empty_sl        = lambda M          : empty_s(long(M))                                                          # Create a square blank image based on long side of the image
kernel0         = lambda a          : empty_s(a)                                                                # Create a kernel
ones            = lambda a          : np.ones((a))                                                              # Create a kernel of ones

blur_g          = lambda M, k       : cv2.GaussianBlur(M, (k, k), 0)                                            # Gaussian blur


def blur_h(frame, kernel_size=5):
    """ Apply a horizontal blur to the given image using the given kernel size """
    k = kernel0(kernel_size)                                                                                    # Create a kernel
    k[int((kernel_size-1)/2), :] = ones(kernel_size)                                                            # Set the middle row to ones
    k /= kernel_size                                                                                            # Normalise the kernel
    return filter2d(frame, k)                                                                                   # Apply the kernel to the image


def blur_v(frame, kernel_size=5):
    """ Apply a vertical blur to the given image using the given kernel size """
    
    k = kernel0(kernel_size)                                                                                    # Create a kernel
    k[:, int((kernel_size-1)/2)] = ones(kernel_size)                                                            # Set the middle column to ones
    k /= kernel_size                                                                                            # Normalise the kernel
    return filter2d(frame, k)                                                                                   # Apply the kernel to the image


select          = lambda M, b       : M[b[1]:b[1]+b[3], b[0]:b[0]+b[2]] if b[2]>0 and b[3]>0 else M             # Select using given bound
roi_rect        = lambda M          : cv2.boundingRect(invert(M))                                               # Detect the region of interest
roi_select      = lambda M, b       : select(invert(M), roi_rect(M))                                            # Select the region of interest
roi_scale       = lambda M, s       : scale_l(roi_select(M, roi_rect(M)), s)                                    # Scale the region of interest
pad             = lambda M, p       : cv2.copyMakeBorder(M, p, p, p, p, cv2.BORDER_CONSTANT, value=0)           # Pad the image


def roi(img, margin=[0,0,0,0], size=64, padding=8):
    """ Extract the region of interest from the given image

        :param img: img to be cropped
        :type img: np.ndarray

        :param size: size of the region of interest
        :type size: int

        :param padding: padding of the region of interest
        :type padding: int

        :return: Cropped image
        :rtype: np.ndarray
    """

    img_bin                         = binary(gray(img), 128)                                                    # Convert to binary
    img_cropped                     = crop(img_bin, margin)                                                     # Crop the image
    img_roi_rect                    = roi_scale(img_cropped, size)                                              # Detect and scale the region of interest
    empty_square                    = empty_s(size)                                                             # Create a blank square image
    w, h                            = width(img_roi_rect), height(img_roi_rect)                                 # Width and height of the region of interest
    x1, y1                          = int((size-w)/2), int((size-h)/2)                                          # Top left corner of the region of interest to be pasted
    x2, y2                          = x1+w, y1+h                                                                # Bottom right corner of the region of interest to be pasted
    empty_square[y1:y2, x1:x2]      = img_roi_rect                                                              # Paste the region of interest to the blank square image
    img_roi_padded                  = pad(empty_square, padding)                                                # Pad the image
    img_roi                         = scale(img_roi_padded, (size, size))
    
    # Convert to np
    img_roi                         = as_np(img_roi)

    # Normalise
    img_roi                         = norm(img_roi)
    img_interp                      = interp(img_roi, 0, 255)
    
    return img_interp

flip_h          = lambda M          : cv2.flip(M, 1)                                                            # Flip the image horizontally
flip_v          = lambda M          : cv2.flip(M, 0)                                                            # Flip the image vertically
flip_r          = lambda M          : cv2.flip(M, random.randint(0, 2))                                         # Flip the image randomly
rot_mat         = lambda M, a       : cv2.getRotationMatrix2D((width(M)/2, height(M)/2), a, 1)                  # Rotation matrix
warp_affine     = lambda M, a       : cv2.warpAffine(M, a, (width(M), height(M)))                               # Affine warp
rotate          = lambda M, a       : warp_affine(M, rot_mat(M, a))                                             # Rotate the image by the given angle
rotate_r        = lambda M, a, b    : rotate(M, random.randint(a, b))                                           # Rotate the image randomly by the given angle range