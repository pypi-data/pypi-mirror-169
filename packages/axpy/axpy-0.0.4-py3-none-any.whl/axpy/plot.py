""" axpy.plot
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

import matplotlib.pyplot as plt

def image_grid(imgs, cols, rows, figsize=(10,10), axis='on', cmap='gray'):
    """ Plot a grid of images """
    fig, ax = plt.subplots(rows, cols, figsize=figsize)
    for i in range(rows):
        for j in range(cols):
            ax[i,j].imshow(imgs[i*cols + j], cmap=cmap)
            ax[i,j].axis(axis)
    plt.show()

def image(img, figsize=(10,10), axis='on', cmap='gray'):
    """ Plot a single image """
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(img, cmap=cmap)
    ax.axis(axis)
    plt.show()
