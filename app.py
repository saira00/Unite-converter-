import streamlit as st

# Custom CSS for full black background and text styling
st.markdown("""
    <style>
        /* Body background */
        body {
            background-color: #000000;
        }
        
        /* Main app container */
        .stApp {
            background-color: #000000;
            color: white;
        }

        /* Sidebar background */
        .css-1d391kg {
            background-color: #111111;
        }

        /* Text color globally */
        .stMarkdown, .stTextInput, .stSelectbox, .stButton, label, .stNumberInput, .stRadio {
            color: white !important;
        }

        /* Input fields and selectboxes */
        .stSelectbox > div > div, .stTextInput > div > div > input {
            background-color: #333333;
            color: white;
            border-radius: 5px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #1DB954;
            color: black;
            border-radius: 10px;
        }

        /* Success messages */
        .stAlert {
            background-color: #1DB954;
            color: black;
            border-radius: 10px;
        }

        /* Markdown Headings */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #1DB954;
        }

        /* Info and warning text */
        .stInfo, .stWarning {
            background-color: #333333;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


# Define accurate conversion factors
conversion_factors = {
    'Length': {
        'Kilometers (km)': 1000, 'Meters (m)': 1, 'Centimeters (cm)': 0.01, 'Millimeters (mm)': 0.001, 
        'Miles (mi)': 1609.34, 'Yards (yd)': 0.9144, 'Feet (ft)': 0.3048, 'Inches (in)': 0.0254
    },
    'Weight': {
        'Kilograms (kg)': 1, 'Grams (g)': 1000, 'Milligrams (mg)': 1000000, 
        'Pounds (lb)': 2.20462, 'Ounces (oz)': 35.274
    },
    'Temperature': {
        'Celsius (°C)': 1, 'Fahrenheit (°F)': 1, 'Kelvin (K)': 1
    },
    'Volume': {
        'Liters (L)': 1, 'Milliliters (mL)': 1000, 'Gallons (gal)': 3.78541
    },
    'Speed': {
        'Kilometers per hour (km/h)': 1, 'Meters per second (m/s)': 0.277778, 'Miles per hour (mph)': 0.621371
    },
    'Time': {
        'Seconds (s)': 1, 'Minutes (min)': 60, 'Hours (h)': 3600, 'Days (d)': 86400
    },
    'Data Storage': {
        'Bytes (B)': 1, 'Kilobytes (KB)': 1024, 'Megabytes (MB)': 1048576, 'Gigabytes (GB)': 1073741824
    }
}

# Function to convert units
def convert_units(value, from_unit, to_unit, unit_type):
    if unit_type == "Temperature":
        if from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)":
            return (value - 32) * 5/9
        elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)":
            return value + 273.15
        elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)":
            return value - 273.15
        elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  
    else:
        return value * (conversion_factors[unit_type][from_unit] / conversion_factors[unit_type][to_unit])

def main():
    st.title("📐 Unit Converter By Hina 🔄")

    # Step 1: Select Type
    unit_type = st.selectbox("🔹 Select Conversion Type", list(conversion_factors.keys()))

    # Step 2: Select From & To Units
    from_unit = st.selectbox("🔄 Convert From", list(conversion_factors[unit_type].keys()))
    to_unit = st.selectbox("➡ Convert To", list(conversion_factors[unit_type].keys()))

    # Step 3: Input Value
    value = st.number_input("✏ Enter Value", min_value=0.0, format="%.4f")

    if st.button("Convert 🚀"):
        try:
            result = convert_units(value, from_unit, to_unit, unit_type)
            st.success(f"✅ {value} {from_unit} is equal to {result:.4f} {to_unit}")
        except:
            st.error("⚠ Invalid conversion! Try again.")

if __name__ == "__main__":
    main()

    # Divider Line
st.markdown("---")

# Section: Available Units & Details
st.subheader("📌 Available Units & Conversion Details")

unit_details = {
    "Length": "Kilometers (km), Meters (m), Centimeters (cm), Millimeters (mm), Miles (mi), Yards (yd), Feet (ft), Inches (in)",
    "Weight": "Kilograms (kg), Grams (g), Milligrams (mg), Pounds (lb), Ounces (oz)",
    "Temperature": "Celsius (°C), Fahrenheit (°F), Kelvin (K) - Uses conversion formulas",
    "Volume": "Liters (L), Milliliters (mL), Gallons (gal)",
    "Speed": "Kilometers per hour (km/h), Meters per second (m/s), Miles per hour (mph)",
    "Time": "Seconds (s), Minutes (min), Hours (h), Days (d)",
    "Data Storage": "Bytes (B), Kilobytes (KB), Megabytes (MB), Gigabytes (GB)"
}

for category, units in unit_details.items():
    st.markdown(f"*🔹 {category}:* {units}")

# Divider Line
st.markdown("---")

# Section: How Conversions Work
st.subheader("📖 How Conversions Work")
st.markdown("""
- *Length:* 1 Kilometer = 1000 Meters, 1 Meter = 100 Centimeters, 1 Inch = 2.54 Centimeters, 1 Foot = 30.48 Centimeters  
- *Weight:* 1 Kilogram = 1000 Grams, 1 Pound = 0.453592 Kilograms, 1 Ounce = 28.3495 Grams  
- *Temperature:*  
    - °C to °F: (°C × 9/5) + 32  
    - °F to °C: (°F - 32) × 5/9  
    - °C to K: °C + 273.15  
- *Speed:* 1 km/h = 0.621 miles/h, 1 m/s = 3.6 km/h  
- *Time:* 1 Hour = 60 Minutes, 1 Day = 24 Hours  
- *Data Storage:* 1 KB = 1024 Bytes, 1 MB = 1024 KB  
""")

# Divider Line
st.markdown("---")

# Section: Copyright Notice
st.markdown("### 📜 All Rights Reserved | Developed by *Hina*")
st.markdown("© 2025 | *Universal Unit Converter* | *All Rights Reserved* ✅")

