import matplotlib.pyplot as plt

# Define the colors in hexadecimal format
color1 = '#B58D84'
color2 = '#FFAA00'

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot a bar chart with the specified colors
ax.bar([0, 1], [1, 1], color=[color1, color2])

# Show the plot
plt.show()



"""
Step 1 - get user's picture, body size info, wardrobe

import cv2
import numpy as np
from user.utils import identify_skin_color

import cv2
import numpy as np

# Path to the image file
image_path = 'user/test_image.jpg'

# Call the identify_skin_color function to identify skin color in the image
skin_color_hex = identify_skin_color(image_path)

# Print the skin color in hexadecimal format
print('Skin color:', skin_color_hex)

# =========================================================
# Step 2 - process wardrobe and detect cloth type, color etc.
import tensorflow as tfF
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load the ResNet50 model

model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')

# Define a list of possible cloth types

cloth_types = ['shirt', 'jeans', 'dress', 'sweater', 'jacket', 'skirt']

# Load the input image

img_path = 'path/to/input/image.jpg'
img = image.load_img(img_path, target_size=(224, 224))

# Preprocess the image for ResNet50

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make a prediction with the ResNet50 model

preds = model.predict(x)

# Decode the predictions and print the top result

predicted_class = cloth_types[np.argmax(preds)]
print('The input image is classified as a:', predicted_class)

# detect cloth color(s)
import cv2
import numpy as np
from sklearn.cluster import KMeans

# Load the input image

img_path = 'path/to/input/image.jpg'
img = cv2.imread(img_path)

# Convert the image to RGB format

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Flatten the image into a 2D array of pixels

pixels = img.reshape((-1, 3))

# Apply k-means clustering to group similar colors together

kmeans = KMeans(n_clusters=3)
kmeans.fit(pixels)

# Find the most common color cluster

counts = np.bincount(kmeans.labels*)
dominant_color = kmeans.cluster_centers*[np.argmax(counts)]

# Convert the color to a string representation

dominant_color = np.uint8(dominant_color).tolist()
dominant_color = ','.join(str(c) for c in dominant_color)

print('The dominant color of the clothing is:', dominant_color)

# =========================================================
# Step 3 - suggest matching top and bottom pairs
"""