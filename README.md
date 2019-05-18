# image-denoising-using-markov-network

Suppose we have an image consisting of a 2-dimensional array of pixels, where each pixel value Zi is binary, i.e. Zi is  +1 or −1. Assume now that we make a noisy copy of the image, where each pixel in the image is flipped with 10% probability. A pixel in this noisy image is denoted by Xi. The image and noisy images are shown below

![original](/Images/original.png)
![noisy](/Images/Noisy.png)

Given the observed array of noisy pixels, our goal is to recover the following MN. We have a latent variable Zi for each noise-free pixel, and an observed variable Xi for each noisy pixel. Each variable Zi has an edge leading to its immediate neighbors (to the Zi associated with pixels above, below, to the left, and to the right, when they exist). Additionally, each variable Zi has an edge leading to its associated observed pixel Xi. 

![graph](/Images/graph.png)

Denote the full array of latent (noise-free) pixels as Z and the full array of observed (noisy) pixels as X. We define the energy function for this model as

![eq](/Images/Equation.png)

where the first and third summations are over the entire array of pixels, the second summation is over all pairs of latent variables connected by an edge, and h belongs to real domain R, b and v belong to positive real domain. Constants that must be chosen are h, b and v.

We want to get the original image from the noisy one by minimizing the above energy function to get the true value of each pixel. The Zi are initialized to the values from noisy image. Then we iterate through all Zi and check which pixel value gives a lower value for the energy function. The process is repeated till the energy has converged.

We try three combinations of the constants:

## Case 1
h = 0.01 b = 0.01 v = 0.01 

![1](/Images/Case1.png)

error rate = 2.6975 %

## Case 2
h = -0.001 b = 100 v = 100

![1](/Images/Case2.png)

error rate = 0.6117857142857143 %

## Case 3
h = 0 b = 1 v = 10

![1](/Images/Case3.png)

error rate = 0.6117857142857143 %

We get similar error rate for case 2 and 3. Hence any of those can be chosen.
