# %%
import cv2

img = cv2.imread('sign.jpg')
img.shape
# (1728, 2304, 3) 
# 1700 on 2300 this is the image size 
# And 3 this is for every pixel the colors in it
# %%
import matplotlib.pyplot as plt

plt.imshow(img)
# Matplotlib does show the image but the colors seem off. 
# The reason is that OpenCV uses BGR enconding, not RGB.
# %%
#So we can convert using the cv2.cvtColor the image
mpl_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(mpl_img)
#Now it will have the right color
# %%
# A common task is to convert images to gray scale and this task can be done again with the cvtColor functions 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
# It does not look like gray but the reason now is the color map that matplotlib is using
# %%
# If we tell matplotlib to use the gray color map it is going to look just fine
plt.imshow(gray, cmap='gray')

# %%
#Let's find the edges of the image
# We are going to use Canny algorithm and giving is 2 thresholds: 80 and 150
edges = cv2.Canny(gray, 80, 150)
plt.imshow(edges, cmap='gray')
#And now we see it detected most of the edges.