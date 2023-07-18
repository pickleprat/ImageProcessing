
from skimage.io import imread
from matplotlib.pyplot import imshow, figure, axes, show
from numpy import arange, meshgrid

f = imread('shapes.png', as_gray=True)
# First Representation
imshow(f, cmap='gray')

# Second Representation
print(f)

# Third Representation
M = f.shape[0]
N = f.shape[1]

x = arange(M)
y = arange(N)

X, Y = meshgrid(x,y)

fig = figure()
ax = axes(projection='3d')
ax.plot_surface(X, Y, f.T, cmap='gray')
show()
