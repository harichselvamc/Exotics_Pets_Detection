# import streamlit as st
# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# import numpy as np

# # Load the trained model
# model = tf.keras.models.load_model("exoticsclassification.h5")

# # Define class names
# class_names = {
#         "0": "Chameleon",
#         "1": "Crocodile_Alligator",
#         "2": "Frog",
#         "3": "Gecko",
#         "4": "Iguana",
#         "5": "Lizard",
#         "6": "Salamander",
#         "7": "Snake",
#         "8": "Toad",
#         "9": "Turtle_Tortoise"
# }
# st.markdown(
#     """
#     <style>
#     .centered-title {
#         text-align: center;
#     }
   
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.title("Exotics Pet Detection App")

# # Upload an image for classification
# uploaded_image = st.file_uploader("Upload a Exotics Pet image", type=["jpg", "png", "jpeg"])

# if uploaded_image is not None:
#     image = tf.image.decode_image(uploaded_image.read(), channels=3)
#     image = tf.image.resize(image, (224, 224))
#     image = np.expand_dims(image, axis=0) / 255.0

#     st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
#     if st.button("Classify"):
#         prediction = model.predict(image)
#         predicted_class = np.argmax(prediction, axis=-1)
#         st.write(f"Predicted Type: {class_names[str(predicted_class[0])]}")
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("exoticsclassification.h5")

# Define class names
class_names = {
    "0": "Chameleon",
    "1": "Crocodile_Alligator",
    "2": "Frog",
    "3": "Gecko",
    "4": "Iguana",
    "5": "Lizard",
    "6": "Salamander",
    "7": "Snake",
    "8": "Toad",
    "9": "Turtle_Tortoise"
}

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Exotics Pet Detection App")

# Upload an image for classification
uploaded_image = st.file_uploader("Upload an Exotics Pet image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = tf.image.decode_image(uploaded_image.read(), channels=3)
    image = tf.image.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0) / 255.0

    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    if st.button("Classify"):
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction, axis=-1)

        if predicted_class[0] >= len(class_names):
            st.write("This doesn't seem to be an Exotics Pet image.")
        else:
            st.write(f"Predicted Type: {class_names[str(predicted_class[0])]}")
       
       
st.write("Note: The model is trained specifically for Exotics Pets, and may not be accurate for other animals like cats or dogs.")
