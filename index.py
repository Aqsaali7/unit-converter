import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color : #EEF1DA;
        color : black;
    }
    .stApp{
        background: linear-gradiant(135deg, #FFF5E4 , #FBF8EF );
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
       text-align: center;
       font-size: 36px;
       color: black;
    }
    .stButton>button{
       background: linear-gradient(45deg , #2C3930);
       color: white;
       font-size: 18px;
       padding: 10px 20px;
       border-radius: 10px;
       transition: 0.3s;
       box-shadow: 0px 5px 15px   #3F4F44;
    }
    .stButton>button:hover {
       transform: scale (1.05);
       background: linear-gradient(45deg,  #3F4F44);
      color: white;
    }
    .result-box {
      font-size: 20px;
      font-weight: bold;
      text-align: center;
      background: slate ;
      padding: 25px;
      border-radius: 10px
      marging-top: 20px;
      box-shadow: slate ;
    }
    .footer{
       text-align: center;
        marging-top: 50px;
        font-size: 14px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description:
st.markdown("<h1> Unit Converter </h1>",  unsafe_allow_html=True )
st.write("Easily convert between different units of measurement.")
  
  #sidebar menu
conversion_type = st.sidebar.selectbox( "Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input ("Enter Value", value=0.0, min_value=0.0, step=0.1) 
col1, col2 = st.columns(2)

if conversion_type == "Length":
        with col1:
           from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Feet", "Inches"])
        with col2:
            to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Feet", "Inches"])
elif conversion_type == "Weight": 
        with col1:
           from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])  
        with col2:
           to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])    
elif conversion_type == "Temperature":
        with col1:
           from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"]) 
        with col2:
           to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])  

def length_converter(value,from_unit,to_unit):
   length_units = {
    "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Milimeters": 1000,
    "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28, "Inches": 39.37
   } 
   return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
   weight_units = {
      "Kilograms": 1,
      "Grams": 1000,
      "Milligrams": 1000000,
      "Pounds": 2.20462,
      "Ounces": 35.27
   }
   return (value / weight_units[from_unit]) * weight_units[to_unit]

def temprature_converter(value,from_unit,to_unit):
   if from_unit =="Celsius":
      return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 237.15 if to_unit == "Kelvin" else value
   elif from_unit == "Fahrenheit":
      return (value - 32) *5/9 if to_unit == "Celsius" else (value -32)  * 5/9 + 273.15 if to_unit == "kelvin" else value
   elif from_unit =="Kelvin":
      return (value -273.15) if to_unit =="Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
   return value


if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temprature_converter(value, from_unit, to_unit)

    st.markdown(f'<div class="result-box">{value} {from_unit} = {result:.4f} {to_unit}</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer">Developed by Aqsa Ali</div>', unsafe_allow_html=True)


      
      



















