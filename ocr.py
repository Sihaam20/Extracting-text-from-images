import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Extract Text from Images")

#subtitle
st.markdown("## using EASYOCR")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model
from PIL import Image
im = Image.open("outliers.jpeg")

im

reader = ocr.Reader(['en'],model_storage_directory='.')

bounds = reader.readtext("outliers.jpeg")


from PIL import Image, ImageDraw, ImageFont

def draw_boxes(image,bounds, color = 'blue', width =2):
  draw = ImageDraw.Draw(image)
  for bound in bounds:
    p0,p1,p2,p3 = bound[0]
    draw.line([*p0,*p1,*p2,*p3,*p0], fill=color, width = width)
  return image

draw_boxes(im, bounds)

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("SIHAAM")





