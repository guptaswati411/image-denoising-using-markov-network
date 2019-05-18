# image-denoising-using-markov-network

Suppose we have an image consisting of a 2-dimensional array of pixels, where each pixel value Zi is binary, i.e. Zi is  +1 or −1. Assume now that we make a noisy copy of the image, where each pixel in the image is flipped with 10% probability. A pixel in this noisy image is denoted by Xi. The image and noisy images are shown below

![original](/Images/original.PNG)
![noisy](/Images/noisy.PNG)

Given the observed array of noisy pixels, our goal is to recover
