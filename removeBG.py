#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:08:24 2024
The script uses the rembg library to remove the background of an image, saves the processed 
image, and opens it for viewing.

@author: abinjacob
"""

# libraries 
import os.path as op
from rembg import remove
from PIL import Image

# file and folder
folderpath = r'/Users/abinjacob/Documents/Fun Coding/resources'
filename = 'sampleimage1.jpeg'
loadpath = op.join(folderpath,filename)
savepath = op.join(folderpath,f'{op.splitext(filename)[0]}_BGremoved.png')
# opening image 
img = Image.open(loadpath)
# removing bacground
output = remove(img)
# save and open image 
output.save(savepath)
Image.open(savepath)

