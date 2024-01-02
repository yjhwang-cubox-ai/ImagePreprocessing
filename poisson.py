import os
import sys

import numpy as np
import cv2 as cv

def main():
    # im_src = cv.imread("test/5.jpeg")
    # im_dst = cv.imread("nature.png")
    im_src = cv.imread("nature.png")
    im_src = cv.resize(im_src, dsize=(960,600))
    im_dst = cv.imread("test/5.jpeg")
    im_dst = cv.resize(im_dst, dsize=(768,512))
    
    im_mask = np.full(im_dst.shape, 255, dtype = np.uint8)
    
    center = (im_src.shape[1]//2, im_src.shape[0]//2)

    im_clone = cv.seamlessClone(im_dst, im_src, im_mask, center, cv.MIXED_CLONE)

    cv.imshow("clone", im_clone)
    cv.waitKey(0)

if __name__ == '__main__':
    main()