import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model

# Load the MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Load the user's image
image = load_img('./user/test_image.jpg')

# Convert the image to an array
image_array = img_to_array(image)

# Resize the image to the input size of the MobileNetV2 model
image_array = tf.image.resize(image_array, (224, 224))

# Preprocess the image
image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)

# Predict the top wear, bottom wear, hair, sunglasses, and shoes of the user
top_wear_prediction = model.predict(image_array)[0]
bottom_wear_prediction = model.predict(image_array)[1]
hair_prediction = model.predict(image_array)[2]
sunglasses_prediction = model.predict(image_array)[3]
shoes_prediction = model.predict(image_array)[4]

# Get the top wear, bottom wear, hair, sunglasses, and shoes classes
top_wear_class = top_wear_prediction.argmax()
bottom_wear_class = bottom_wear_prediction.argmax()
hair_class = hair_prediction.argmax()
sunglasses_class = sunglasses_prediction.argmax()
shoes_class = shoes_prediction.argmax()

# Get the top wear, bottom wear, hair, sunglasses, and shoes names
top_wear_names = ['dress', 'shirt', 't-shirt', 'sweater', 'jacket']
bottom_wear_names = ['pants', 'skirt', 'shorts', 'jeans']
hair_names = ['bald', 'short hair', 'long hair']
sunglasses_names = ['no sunglasses', 'sunglasses']
shoes_names = ['no shoes', 'sneakers', 'dress shoes']

# Get the colors of the detected objects
top_wear_color = image_array[top_wear_prediction.argmax()]
bottom_wear_color = image_array[bottom_wear_prediction.argmax()]
hair_color = image_array[hair_prediction.argmax()]
sunglasses_color = image_array[sunglasses_prediction.argmax()]
shoes_color = image_array[shoes_prediction.argmax()]

# Get the top 2 dominant colors of the detected objects
top_2_dominant_colors = []
for color in image_array:
  top_2_dominant_colors.append(sorted(color, key=lambda x: x[0], reverse=True)[:2])

# Create a dictionary with detected object type and its color
detected_objects = {
  'top wear': top_wear_color,
  'bottom wear': bottom_wear_color,
  'hair': hair_color,
  'sunglasses': sunglasses_color,
  'shoes': shoes_color
}

# Print the detected objects and their colors
for object_type, color in detected_objects.items():
  print(f'{object_type}: {color}')

# Print the top 2 dominant colors of the detected objects
for object_type, colors in top_2_dominant_colors.items():
  print(f'{object_type}: {colors}')