# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

# %%
# Create figure and axes
fig, ax = plt.subplots()

#Display the image
ax.imshow(img)

# Create a blue square
import matplotlib.patches as patches
square = patches.Rectangle((190,350),490,500,linewidth=5, edgecolor='blue', facecolor='none')

# Add the patch to the Axes
ax.add_patch(square)

plt.show()

# %%
# Answer of the challenge (no entiendo muy bien asi)
# First dimension is rows (y)
tl_x, tl_y = 350, 190 # top-left
br_x, br_y = 850, 680 # bottom-right
width = 5

color = [0, 0, 0xFF] # blue

# Top line # using slicing
img[tl_x:tl_x+width, tl_y:br_y] = color

# Bottom line
img[br_x:br_x+width, tl_y:br_y] = color

# Left line
img[tl_x:br_x, tl_y:tl_y+width] = color

# Right line
img[tl_x:br_x, br_y-width:br_y] = color

plt.imshow(img)
# %%
