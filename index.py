import requests
from io import BytesIO
import streamlit as st
import base64
from streamlit_option_menu import option_menu

import google.generativeai as genai




st.set_page_config(
    page_icon="Logo4.png",
    page_title="Medicine Recommendation System",
    layout="wide"
)


# Function to convert an image file to base64 encoding
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Convert the image "13.jpg" to base64 encoding
# img = get_img_as_base64("13.jpg")

# Convert the local image "HERO.jpg" to base64 encoding
Background_img = get_img_as_base64("1.jpg")  # Replace with your local image path



genai.configure(api_key="AIzaSyBX9BFeAk8HcMmWSuhh0xR_4CnrtEGrHok")






model = genai.GenerativeModel('gemini-pro')

# genmini api

# funcation  1

def generate_disease_name(symptoms_list):
    prompt = f"""
    You are given the following list of symptoms:

    {symptoms_list}

    Your task is to identify and provide the names of possible diseases that match these symptoms. Only list the names of the diseases without additional descriptions.

    The possible diseases could include, but are not limited to:
    - 'Allergies'
    - 'Psoriasis'
    - 'Rheumatoid Arthritis'
    - 'Common Cold'
    - 'Eczema'
    - 'Fungal Infections'
    - 'Chronic Cholestasis'

    Based on the provided symptoms, generate the following:

    **Possible Diseases:**
    [List of possible disease names]

    Ensure that the disease names are relevant to the symptoms provided.
    """

    response = model.generate_content(prompt)
    return response



def generate_additional_symptoms(symptoms_list):
    prompt = f"""
    You are given the following list of symptoms:

    {symptoms_list}

    Your task is to:
    1. Identify possible diseases that match these symptoms.
    2. Provide a list of additional common symptoms associated with the identified diseases. 
    Only list the additional symptoms without providing the names of the diseases.

    The possible diseases could include, but are not limited to:
    - 'Allergies'
    - 'Psoriasis'
    - 'Rheumatoid Arthritis'
    - 'Common Cold'
    - 'Eczema'
    - 'Fungal Infections'
    - 'Chronic Cholestasis'

    Based on the provided symptoms, generate the following:

    **Additional Symptoms:**
    [List of additional common symptoms associated with the identified diseases]

    Ensure that the symptoms listed are relevant to the diseases inferred from the provided symptoms.
    """

    response = model.generate_content(prompt)
    return response


def suggest_medications(symptoms_list):
    prompt = f"""
    You are given the following list of symptoms:

    {symptoms_list}

    Your task is to:
    1. Identify possible diseases that match these symptoms.
    2. Provide a list of recommended medications for the identified diseases.
    Only list the medications without providing the names of the diseases.

    The possible diseases could include, but are not limited to:
    - 'Allergies'
    - 'Psoriasis'
    - 'Rheumatoid Arthritis'
    - 'Common Cold'
    - 'Eczema'
    - 'Fungal Infections'
    - 'Chronic Cholestasis'

    Based on the provided symptoms, generate the following:

    **Recommended Medications:**
    [List of recommended medications for the identified diseases]

    Ensure that the medications listed are relevant to the diseases inferred from the provided symptoms.
    """

    response = model.generate_content(prompt)
    return response





def suggest_workouts(symptoms_list):
    prompt = f"""
    You are given the following list of symptoms:

    {symptoms_list}

    Your task is to:
    1. Identify possible diseases that match these symptoms.
    2. Provide a list of recommended workouts or lifestyle changes for the identified diseases.
    Only list the recommended workouts without providing the names of the diseases.

    The possible diseases could include, but are not limited to:
    - 'Allergies'
    - 'Psoriasis'
    - 'Rheumatoid Arthritis'
    - 'Common Cold'
    - 'Eczema'
    - 'Fungal Infections'
    - 'Chronic Cholestasis'

    Based on the provided symptoms, generate the following:

    **Recommended Workouts or Lifestyle Changes:**
    [List of recommended workouts or lifestyle changes for the identified diseases]

    Ensure that the workouts or lifestyle changes listed are relevant to the diseases inferred from the provided symptoms.
    """

    response = model.generate_content(prompt)
    return response




def suggest_diet(symptoms_list):
    prompt = f"""
    You are given the following list of symptoms:

    {symptoms_list}

    Your task is to:
    1. Identify possible diseases that match these symptoms.
    2. Provide a list of recommended dietary changes or foods for the identified diseases.
    Only list the recommended dietary changes or foods without providing the names of the diseases.

    The possible diseases could include, but are not limited to:
    - 'Allergies'
    - 'Psoriasis'
    - 'Rheumatoid Arthritis'
    - 'Common Cold'
    - 'Eczema'
    - 'Fungal Infections'
    - 'Chronic Cholestasis'

    Based on the provided symptoms, generate the following:

    **Recommended Dietary Changes:**
    [List of recommended dietary changes or foods for the identified diseases]

    Ensure that the dietary changes listed are relevant to the diseases inferred from the provided symptoms.
    """

    response = model.generate_content(prompt)
    return response







# CSS styling for the Streamlit app
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{Background_img}");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    # opacity: 0.3;
    # transition: opacity 2s ease-in-out; /* 2 seconds transition */
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stSidebar"] > div:first-child {{
    background-repeat: no-repeat;
    background-attachment: fixed;
    # background: rgb(18 18 18 / 0%);
    background: #0d425d;
}}


.st-emotion-cache-1gv3huu {{
    position: relative;
    top: 2px;
    background-color: #000;
    z-index: 999991;
    min-width: 244px;
    max-width: 550px;
    transform: none;
    transition: transform 300ms, min-width 300ms, max-width 300ms;
}}

.st-emotion-cache-1jicfl2 {{
    width: 100%;
    padding: 4rem 1rem 4rem;
    min-width: auto;
    max-width: initial;

}}


.st-emotion-cache-4uzi61 {{
    border: 1px solid rgba(49, 51, 63, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(240 242 246);
    box-shadow: 0 5px 8px #6c757d;
}}

.st-emotion-cache-1vt4y43 {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    COLOR: WHITE;
    user-select: none;
    background-color: #0461f1;
    border: 1px solid rgba(49, 51, 63, 0.2);
}}

.st-emotion-cache-qcpnpn {{
    border: 1px solid rgb(163, 168, 184);
    border-radius: 0.5rem;
    # padding: calc(-1px + 1rem);
    padding: calc(40px + 0rem);
    background-color: rgb(38, 39, 48);
    MARGIN-TOP: 9PX;
    box-shadow: 0 5px 8px #6c757d;


}}




.st-emotion-cache-15hul6a {{
    user-select: none;
    background-color: #ffc107;
    border: 1px solid rgba(250, 250, 250, 0.2);
    
}}

.st-emotion-cache-1hskohh {{
    margin: 0px;
    padding-right: 2.75rem;
    color: rgb(250, 250, 250);
    border-radius: 0.5rem;
    background: #000;
}}

.st-emotion-cache-12pd2es {{
    margin: 0px;
    padding-right: 2.75rem;
    color: #f0f2f6;
    border-radius: 0.5rem;
    background: #000;
}}

.st-emotion-cache-1r6slb0 {{
    width: calc(33.3333% - 1rem);
    flex: 1 1 calc(33.3333% - 1rem);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}}
.st-emotion-cache-12w0qpk {{
    width: calc(25% - 1rem);
    flex: 1 1 calc(25% - 1rem);
    display: flex;
    flex-direction: row;
    justify-content: CENTER;
    ALIGN-ITEMS: CENTER;
}}



.st-emotion-cache-1kyxreq {{
    display: flex;
    flex-flow: wrap;
    row-gap: 1rem;
    align-items: center;
    justify-content: center;
}}

img {{
    vertical-align: middle;
    border-radius: 10px;
 
}}


    h5 {{
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 600;
    color: rgb(14 14 14);
    padding: 0px 0px 1rem;
    margin: 0px;
    line-height: 1.2;
}}



div[data-baseweb="tab-list"] {{
    background-color: #00BCD4;
    padding: 5px;
    border-radius: 3px;
}}


div[data-baseweb="tab-list"] button[aria-selected="true"] {{
    background-color: #0008ff;
    color: white;
    border-radius: 20px;
    padding: 22px;
    border: none;
}}

div[data-baseweb="tab-list"] button:hover {{
    background-color: #ffcc00;
    color: white;
    border-radius: 20px;
    padding: 22px;
}}



.st-d4 {{
 background-color: #00BCD4; 
}}

# .st-dh {{
#     padding-top: 2rem;
#     padding: 40px;
#     # background: #1191bd;
#     background: white;
#     border-radius: 10px;
#     margin-top: 16px;
#     # color:white;
# }}

.st-dh {{
    padding-top: 1rem;
    margin-top: 10px;
    padding: 25px;
    background: white;
    border-radius: 10px;
    color:black;

}}

h1 {{
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 700;
    color: #2edcf2;
    padding: 1.25rem 0px 1rem;
    margin: 0px;
    line-height: 1.2;
}}
</style>
"""

# Apply CSS styling to the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)


# Sidebar configuration
with st.sidebar:
    # Display logo image
    st.image("https://raw.githubusercontent.com/Salman7292/Medicine-Recommendation-System-Project/main/Logo4.png", use_column_width=True)

    # Adding a custom style with HTML and CSS for sidebar
    st.markdown("""
        <style>
            .custom-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color:#ffc107
            }
            .custom-text span {
                color: #04ECF0; /* Color for the word 'Recommendation' */
            }
        </style>
    """, unsafe_allow_html=True)
  
  
    # Displaying the subheader with custom styling
    st.markdown('<p class="custom-text"> Medicine <span>Recommendation</span> System</p>', unsafe_allow_html=True)

    # HTML and CSS for the GitHub button
    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Salman7292" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>

    <style>
        /* Button styles */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ffc107;
            color: black;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #000345;
            color: white;
            text-decoration: none; /* Remove underline on hover */
        }
    </style>
    """

    # Display the GitHub button in the sidebar
    st.markdown(github_button_html, unsafe_allow_html=True)
    
    # Footer HTML and CSS
    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:20px; color:#ffffff;">Made with ❤️ by Salman Malik</p>
    </div>
    """

    # Display footer in the sidebar
    st.markdown(footer_html, unsafe_allow_html=True)


# Define the option menu for navigation
selections = option_menu(
    menu_title=None,
    options=['Home', "Cheack Up"],
    icons=['house-fill', "file-earmark-medical-fill"],

    menu_icon="cast",
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {
            "padding": "5px 23px",
            "background-color": "#0d6efd",
            "border-radius": "8px",
            "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.25)"
        },
        "icon": {"color": "#f9fafb", "font-size": "18px"},
        "hr": {"color": "#0d6dfdbe"},
        "nav-link": {
            "color": "#f9fafb",
            "font-size": "15px",
            "text-align": "center",
            "margin": "0 10px",
            "--hover-color": "#0761e97e",
            "padding": "10px 10px",
            "border-radius": "16px"
        },
        "nav-link-selected": {"background-color": "#ffc107", "font-size": "12px"},
    }
)

if selections == "Home":
# Define HTML and CSS for the hero section
    code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
 .hero-section {
    padding: 40px 20px;
    font-family: Arial, sans-serif;
    BACKGROUND: WHITE;
    BORDER-RADIUS: 10PX;
}

    .hero-heading {
        font-size: 2.5rem;
        margin-bottom: 20px;
        color: #343a40;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }
    .hero-text {
        font-size: 1.2rem;
        # line-height: 1.6;
        color: #6c757d;
        # max-width: 800px;
        # margin: 0 auto;
    }

    

    ul{
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 1rem;
    font-weight: 400;
    COLOR: black;

    }
</style>
</head>
<body>
<section class="hero-section">
<div class="container">
    <h1 class="hero-heading">Medicine Recommendation System</h1>
    <p class="hero-text">
        Welcome to our Medicine Recommendation System. Effortlessly receive tailored treatment suggestions based on your symptoms. Simply input your symptoms or provide details to get instant and personalized recommendations. Our system offers:
        <ul>
            <li><strong>Detailed Descriptions:</strong> Understand potential conditions associated with your symptoms.</li>
            <li><strong>Dietary Suggestions:</strong> Discover dietary changes that can help manage your health.</li>
            <li><strong>Medication Recommendations:</strong> Find suitable medications for your symptoms.</li>
            <li><strong>Workout Tips:</strong> Get advice on exercises and lifestyle adjustments to improve your well-being.</li>
        </ul>
        Empower your healthcare journey with our reliable and precise recommendations, designed to assist both individuals and healthcare professionals alike.
    </p>
</div>

</section>
</body>
</html>
"""





# Use Streamlit to display the HTML content
    st.markdown(code, unsafe_allow_html=True)

elif selections == "Cheack Up":
    st.markdown(
        """
        <h1 style='text-align: center;'>Insert Your Detail Here</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <hr style="border: none; height: 2px;width: 50%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%); margin: 0 auto;" />
        """,
        unsafe_allow_html=True
    )



    input_to_Model=st.form("Detail")
    # Text input
    user_input = input_to_Model.text_input(
       placeholder='Insert symptoms eg. (itching,Continuous sneezing,Runny nose)',
       label="Insert symptoms")
    
    submit=input_to_Model.form_submit_button("Predict Diseases")





    # Submit button
    if submit:
        
        st.markdown(
        """
        <h1 style='text-align: center;'>Our AI System Recommendations</h1>
        """,
        unsafe_allow_html=True
    )

        st.markdown(
        """
        <hr style="border: none; height: 2px;width: 50%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%); margin: 0 auto;" />
        """,
        unsafe_allow_html=True
    )

        Diseases,additional_symptoms,medications,workouts,diet=st.tabs(["Diseases","Additional Symptoms","Medications","workouts","diet"])



        with Diseases:
           st.markdown(generate_disease_name(user_input).text)



        with additional_symptoms:
           st.markdown(generate_additional_symptoms(user_input).text)
           

        with medications:
           st.markdown(suggest_medications(user_input).text)



        with workouts:
           st.markdown(suggest_workouts(user_input).text)

        with diet:
           st.markdown(suggest_diet(user_input).text)


           


