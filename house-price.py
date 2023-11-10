import numpy as np
import pickle
import streamlit as st #create account in Streamlit
#map the data
#location,status,property type and facing
location_mapping = {
    "Kesarapalli":10,
    "Auto Nagar":12,
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 11,
    "Penamaluru": 7,
    "Payakapuram": 6
}

#in smilar way we do for status,facing and property type
status_mapping = {'Ready to move':1,
                  'New':0,'Resale':2,'Under Construction':3}



direction_mapping = {
    "Not Mentioned": 0,
    "East": 1,
    "West": 3,
    "NorthEast": 2
}

property_type_mapping = {
    "Apartment": 0,
    "Independent Floor": 1,
    "Independent House": 2,
    "Residential Plot": 3
}

with open('House.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(bed, bath, loc, size, status, face, Type):
    selected_location_numeric = location_mapping[loc]
    selected_status_numeric = status_mapping[status]
    selected_direction_numeric = direction_mapping[face]
    selected_property_type_numeric = property_type_mapping[Type]

    input_data = np.array([[bed, bath, selected_location_numeric, size, selected_status_numeric, selected_direction_numeric, selected_property_type_numeric]])

    return model.predict(input_data)[0]

if __name__ == '__main__':
    st.header('House Price Prediction')

    # Create a column layout to add the image alongside the prediction
    col1, col2 = st.columns([2, 1])

    bed = col1.slider('No of Bedrooms', max_value=10, min_value=1, value=2)
    bath = col1.slider('No of Bathrooms', max_value=8, min_value=0, value=2)
    loc = col1.selectbox("Select a Location", list(location_mapping.keys()))
    size = col1.number_input('Enter the Sq Feet', max_value=10000, min_value=100, value=1000, step=500)
    status = col1.selectbox("Select a Status", list(status_mapping.keys()))
    face = col1.selectbox("Select a Direction", list(direction_mapping.keys()))
    Type = col1.selectbox("Select a Property Type", list(property_type_mapping.keys()))

    result = predict(bed, bath, loc, size, status, face, Type)
    submit_button = st.button("Submit")
    # Check if the button is clicked
    if submit_button:
        #st.write(f"The predicted value is: {result} Lakhs")
        larger_text = f"<h2 style='color: blue;'>The predicted value is : {result} Lakhs</h2>"
        st.markdown(larger_text, unsafe_allow_html=True)






