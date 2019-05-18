from scipy.io import loadmat
from PIL import Image
import numpy as np

# Function to plot image given pixel data
def plot_image(pixel_data):
    img = Image.new( 'RGB', (len(pixel_data[0]),len(pixel_data)), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            if pixel_data[j,i]==-1:
                pixels[i,j] = (0, 0, 0) # set the colour accordingly
            else:
                pixels[i,j] = (255, 255, 255) # set the colour accordingly

    img.show()

#load data
x = loadmat('images.mat')
original=np.array(x['origImg'])
noisy=np.array(x['noisyImg'])
height=len(original)
width=len(original[0])

plot_image(original)
plot_image(noisy)

# Set values for parameters
parameters = [[0.01,0.01,0.01],[-0.001,100,100],[0,1,10]]
for h,b,v in parameters:
    # for b in b_parameters:
    #     for v in v_parameters:
    # initialize z
    z=noisy
    # Calculate initial energy
    first_term=np.sum(z)
    last_term=np.sum(np.multiply(z,noisy))
    middle_term=0
    for i in range (height-1):
        for j in range (width-1):
            middle_term+=z[i,j]*z[i,j+1]
            middle_term+=z[i,j]*z[i+1,j]

    #Total energy
    energy=h*first_term-b*middle_term-v*last_term
    old_energy=energy+100
    while old_energy-energy>1:
        old_energy=energy
        for i in range (height):
            for j in range (width):
                flip=-1 if z[i,j]==1 else 1
                first_term=flip-z[i,j]
                last_term=flip*noisy[i,j]-z[i,j]*noisy[i,j]
                if i==0:
                    if j==0:
                        middle_term=flip*z[i+1,j]+flip*z[i,j+1]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j+1]
                    elif j==width-1:
                        middle_term=flip*z[i+1,j]+flip*z[i,j-1]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j-1]
                    else:
                        middle_term=flip*z[i+1,j]+flip*z[i,j-1]+flip*z[i,j+1]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j-1]-z[i,j]*z[i,j+1]
                elif i==height-1:
                    if j==0:
                        middle_term=flip*z[i-1,j]+flip*z[i,j+1]-z[i,j]*z[i-1,j]-z[i,j]*z[i,j+1]
                    elif j==width-1:
                        middle_term=flip*z[i-1,j]+flip*z[i,j-1]-z[i,j]*z[i-1,j]-z[i,j]*z[i,j-1]
                    else:
                        middle_term=flip*z[i-1,j]+flip*z[i,j-1]+flip*z[i,j+1]-z[i,j]*z[i-1,j]-z[i,j]*z[i,j-1]-z[i,j]*z[i,j+1]
                else:
                    if j==0:
                        middle_term=flip*z[i-1,j]+flip*z[i+1,j]+flip*z[i,j+1]-z[i,j]*z[i-1,j]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j+1]
                    elif j==width-1:
                        middle_term=flip*z[i-1,j]+flip*z[i+1,j]+flip*z[i,j-1]-z[i,j]*z[i-1,j]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j-1]
                    else:
                        middle_term=flip*z[i-1,j]+flip*z[i+1,j]+flip*z[i,j-1]+flip*z[i,j+1]-z[i,j]*z[i-1,j]-z[i,j]*z[i+1,j]-z[i,j]*z[i,j-1]-z[i,j]*z[i,j+1]
                new_energy=energy+h*first_term-b*middle_term-v*last_term
                if new_energy<energy:
                    energy=new_energy
                    z[i,j]=flip
    score=0
    for i in range (height):
        for j in range (width):
            if z[i,j]!=original[i,j]:
                score+=1
    score=score/(height*width)
    print("For h =",h,"b =",b,"v =",v,", error rate =",score*100,"%")
    plot_image(z)

# plot_image(original)

