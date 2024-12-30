import streamlit as st
import base64
from pathlib import Path

def add_custom_styling(image_file):
    st.markdown(
        f"""
        <style>
        /* Universal text color */
        * {{
            color: #000000 !important; /* Set all text to black */
            font-family: Arial, sans-serif !important; /* Ensure consistent font */
        }}

        /* Background styling */
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), 
                        url(data:image/png;base64,{image_file}) no-repeat center center fixed;
            background-size: cover;
        }}

        /* Header and general text styling */
        .stHeader, .stMarkdown, .stText, .stWrite, .css-1d391kg, .css-1v3fvcr {{
            font-size: 24px !important;  /* Increase header and general text size */
            color: #000000 !important;   /* Black text for high contrast */
            font-family: Arial, sans-serif !important;  /* Clean and smooth font */
        }}

        /* Ensure all headers are black */
        h1, h2, h3, h4, h5, h6 {{
            color: #000000 !important;
        }}

        /* Radio button labels */
        .stRadio > label {{
            font-size: 20px !important;  /* Increase radio button label size */
            color: #000000 !important;   /* Black text for readability */
            font-family: Arial, sans-serif !important;
            background-color: #ffeb3b !important; /* Yellow background for every choice */
            border-radius: 5px;          /* Rounded corners */
            padding: 5px;                /* Padding for better spacing */
            margin-bottom: 5px;          /* Space between choices */
            display: block;              /* Ensure proper layout */
        }}
        .stRadio > label:hover {{
            background-color: #fff59d !important;  /* Lighter yellow on hover */
        }}

        /* Buttons styling */
        .stButton > button {{
            font-size: 20px !important; /* Larger button text */
            background-color: #0056b3 !important;  /* Darker blue for buttons */
            color: #000000 !important;             /* Black button text */
            font-family: Arial, sans-serif !important;
        }}

        /* Highlight selected radio button */
        div[data-baseweb="radio"] > label[data-selected="true"] {{
            font-weight: bold;          /* Bold font for selected option */
            background-color: #ffeb3b !important;  /* Keep yellow background for selected option */
            border: 2px solid #ffca28 !important;  /* Slightly darker yellow border */
            padding: 6px !important;               /* Add slight padding for prominence */
            border-radius: 5px !important;         /* Rounded corners */
            color: #000000 !important;             /* Ensure selected text is dark */
        }}

        /* Additional selectors to cover more text elements */
        .css-1aumxhk, .css-1siy2j7, .css-1d391kg, .css-1v3fvcr {{
            color: #000000 !important;
        }}

        /* --- New CSS for Bright Text in Specific Areas --- */

        /* Make the main app title bright (white) */
        .stApp h1 {{
            color: #FFFFFF !important; /* Set main title to white */
        }}

        /* --- New CSS for Sidebar Selectbox Background and Text --- */

        /* Target the sidebar selectbox container */
        [data-testid="stSidebar"] .stSelectbox > div > div {{
            background-color: #FFFFFF !important; /* White background for the selectbox */
            border-radius: 5px !important;        /* Rounded corners for the selectbox */
            padding: 5px !important;               /* Padding for better spacing */
        }}

        /* Set the text color of the selectbox label to black */
        [data-testid="stSidebar"] .stSelectbox > div > div > label {{
            color: #000000 !important; /* Black text for the selectbox label */
            font-size: 16px !important; /* Adjust font size as needed */
            font-family: Arial, sans-serif !important;
        }}

        /* Optional: Adjust the dropdown menu background and text */
        [data-testid="stSidebar"] .stSelectbox .css-1wa3eu0-placeholder, 
        [data-testid="stSidebar"] .stSelectbox .css-1pahdxg-control {{
            background-color: #FFFFFF !important; /* White background for dropdown */
            color: #000000 !important;            /* Black text for dropdown items */
        }}

        /* Optional: Adjust dropdown menu items on hover */
        [data-testid="stSidebar"] .stSelectbox .css-1n7v3ny-option {{
            background-color: #FFFFFF !important; /* White background on hover */
            color: #000000 !important;            /* Black text on hover */
        }}

        /* Ensure the selected option display has white background and black text */
        [data-testid="stSidebar"] .stSelectbox .css-1uccc91-singleValue {{
            color: #000000 !important; /* Black text for the selected value */
            background-color: #FFFFFF !important; /* White background for the selected value */
        }}

        /* Remove any previously set sidebar text color to white */
        .css-1d391kg, .css-1v3fvcr {{
            color: #000000 !important; /* Override previous white text color */
        }}

        /* Ensure sidebar titles (h2 in sidebar) are also black */
        [data-testid="stSidebar"] h2 {{
            color: #000000 !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# Load the image as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Add the background image and custom styles
background_image = "Home.png"  # Ensure the image is in the same folder as this script
encoded_image = get_base64_of_bin_file(background_image)
add_custom_styling(encoded_image)

# Function to render IPSS questionnaire
def render_ipss():
    st.header("แบบสอบถามอาการของต่อมลูกหมาก (ฉบับนานาชาติ) (IPSS)")
    st.write("แบบสอบถามนี้ใช้สำหรับประเมินอาการเกี่ยวกับต่อมลูกหมาก เพื่อช่วยในการวินิจฉัยและจัดการกับอาการที่เกี่ยวข้องกับทางเดินปัสสาวะส่วนล่าง")

    questions = [
        "1. ในช่วง 1 เดือนที่ผ่านมา หลังจากที่คุณปัสสาวะเสร็จแล้ว คุณรู้สึกว่าปัสสาวะไม่สุดบ่อยแค่ไหน",
        "2. ในช่วง 1 เดือนที่ผ่านมา คุณต้องปัสสาวะบ่อยแค่ไหน",
        "3. ในช่วง 1 เดือนที่ผ่านมา ขณะที่คุณปัสสาวะ คุณต้องหยุดและเริ่มปัสสาวะใหม่บ่อยแค่ไหน",
        "4. ในช่วง 1 เดือนที่ผ่านมา เมื่อคุณปัสสาวะ คุณพบว่าปัสสาวะไม่ไหลเลยบ่อยแค่ไหน",
        "5. ในช่วง 1 เดือนที่ผ่านมา คุณต้องปัสสาวะเพียงเพื่อถ่ายปัสสาวะบ่อยแค่ไหน",
        "6. ในช่วง 1 เดือนที่ผ่านมา คุณต้องลุกจากที่นอนกลางดึกเพื่อปัสสาวะบ่อยแค่ไหน"
    ]
    options = [
        ["ไม่เคย (0 คะแนน)", "ประมาณ 1 ใน 5 ครั้ง (1 คะแนน)", "ประมาณ 1 ใน 3 ครั้ง (2 คะแนน)", 
         "ประมาณ 1 ใน 2 ครั้ง (3 คะแนน)", "ประมาณ 2 ใน 3 ครั้ง (4 คะแนน)", "เกือบทุกครั้ง (5 คะแนน)"]
    ] * len(questions)
    scores = []

    for idx, question in enumerate(questions):
        response = st.radio(question, options[idx], key=f"ipss_{idx}")
        scores.append(int(response.split('(')[1].split()[0]))  # Extract score from text

    if st.button("ประมวลผลคะแนน IPSS"):
        total_score = sum(scores)
        st.write(f"คะแนนรวมของคุณ: {total_score}")
        if total_score <= 7:
            st.success("อาการของคุณมีเพียงเล็กน้อย")
        elif total_score <= 19:
            st.warning("อาการของคุณอยู่ในระดับปานกลาง")
        else:
            st.error("อาการของคุณอยู่ในระดับรุนแรง")
        st.write("[ข้อมูลเพิ่มเติมเกี่ยวกับยา](https://flowmind-ra.my.canva.site/drugs-for-bladder-prostate-disorders)")
    
    # Add additional link
    st.write("[ตรวจคัดกรองอัตราการไหลปัสสาวะด้วยตนเอง](https://flowmindra.streamlit.app/)")

# Function to render OABSS questionnaire
def render_oabss():
    st.header("แบบสอบถามเพื่อประเมินภาวะกระเพาะปัสสาวะบีบตัวไวเกิน (OABSS)")
    st.write("แบบสอบถามนี้ใช้เพื่อประเมินอาการของกระเพาะปัสสาวะบีบตัวไวเกิน (Overactive Bladder) ซึ่งสามารถช่วยในการวินิจฉัยและประเมินระดับความรุนแรงของอาการ")

    questions = [
        "1. ปกติท่านปัสสาวะกี่ครั้งในหนึ่งวัน ตั้งแต่หลังตื่นนอนในตอนเช้าถึงก่อนนอนตอนกลางคืน",
        "2. ปกติตื่นนอนขึ้นมาปัสสาวะตอนกลางคืนกี่ครั้ง นับตั้งแต่เข้านอนหลับแล้วถึงตื่นนอนในตอนเช้า",
        "3. บ่อยแค่ไหนที่ท่านรู้สึกปวดปัสสาวะอย่างทันทีทันใด ที่ไม่สามารถกลั้นไว้ได้",
        "4. บ่อยแค่ไหนที่ท่านมีปัสสาวะเล็ดราดในขณะรู้สึกปวดปัสสาวะอย่างทันทีทันใด ที่ไม่สามารถกลั้นไว้ได้"
    ]
    options = [
        ["น้อยกว่าหรือเท่ากับ 7 ครั้ง (0 คะแนน)", "8-14 ครั้ง (1 คะแนน)", "เท่ากับหรือมากกว่า 15 ครั้ง (2 คะแนน)"],
        ["0 ครั้ง (0 คะแนน)", "1 ครั้ง (1 คะแนน)", "2 ครั้ง (2 คะแนน)", "เท่ากับหรือมากกว่า 3 ครั้ง (3 คะแนน)"],
        ["ไม่มีเลย (0 คะแนน)", "น้อยกว่าสัปดาห์ละครั้ง (1 คะแนน)", "เท่ากับหรือมากกว่าสัปดาห์ละครั้ง (2 คะแนน)",
         "1 ครั้งต่อวัน (3 คะแนน)", "2 ถึง 4 ครั้งต่อวัน (4 คะแนน)", "เท่ากับหรือมากกว่า 5 ครั้งต่อวัน (5 คะแนน)"],
        ["ไม่มีเลย (0 คะแนน)", "น้อยกว่าสัปดาห์ละครั้ง (1 คะแนน)", "เท่ากับหรือมากกว่าสัปดาห์ละครั้ง (2 คะแนน)",
         "1 ครั้งต่อวัน (3 คะแนน)", "2 ถึง 4 ครั้งต่อวัน (4 คะแนน)", "เท่ากับหรือมากกว่า 5 ครั้งต่อวัน (5 คะแนน)"]
    ]
    scores = []

    for idx, question in enumerate(questions):
        response = st.radio(question, options[idx], key=f"oabss_{idx}")
        scores.append(int(response.split('(')[1].split()[0]))  # Extract score from text

    if st.button("ประมวลผลคะแนน OABSS"):
        total_score = sum(scores)
        st.write(f"คะแนนรวมของคุณ: {total_score}")
        if total_score <= 3:
            st.info("สงสัยภาวะกระเพาะปัสสาวะบีบตัวไวเกินน้อย")
        elif total_score >= 4 and scores[2] >= 2:
            st.warning("สงสัยมีภาวะกระเพาะปัสสาวะบีบตัวไวเกิน")
        st.write("[ข้อมูลเพิ่มเติมเกี่ยวกับยา](https://flowmind-ra.my.canva.site/drugs-for-bladder-prostate-disorders)")
    
    # Add additional link
    st.write("[ตรวจคัดกรองอัตราการไหลปัสสาวะด้วยตนเอง](https://flowmindra.streamlit.app/)")

# Function to render IIEF-5 questionnaire
def render_iief5():
    st.header("แบบประเมิน IIEF-5 Thailand (ภาวะหย่อนสมรรถภาพทางเพศ)")
    st.write("แบบสอบถามนี้ใช้สำหรับประเมินภาวะหย่อนสมรรถภาพทางเพศ (Erectile Dysfunction) โดยการวัดระดับความพึงพอใจและความสามารถในการทำกิจกรรมทางเพศ")

    questions = [
        "1. ท่านมีความมั่นใจเพียงใดว่าอวัยวะเพศสามารถแข็งตัวได้และแข็งได้นานพอ",
        "2. เมื่อมีการกระตุ้นทางเพศ อวัยวะเพศแข็งตัวบ่อยแค่ไหน",
        "3. เมื่ออวัยวะเพศแข็งตัวแล้ว ท่านสามารถคงความแข็งตัวไว้ได้ยาวนานแค่ไหน",
        "4. ระหว่างมีเพศสัมพันธ์ อวัยวะเพศแข็งตัวได้มากน้อยเพียงใด",
        "5. หลังจากเสร็จสิ้นการมีเพศสัมพันธ์ ท่านมีความพึงพอใจเพียงใด"
    ]
    options = [
        ["ต่ำมาก (1 คะแนน)", "ต่ำ (2 คะแนน)", "ปานกลาง (3 คะแนน)", "สูง (4 คะแนน)", "สูงมาก (5 คะแนน)"]
    ] * len(questions)
    scores = []

    for idx, question in enumerate(questions):
        response = st.radio(question, options[idx], key=f"iief5_{idx}")
        scores.append(int(response.split('(')[1].split()[0]))  # Extract score from text

    if st.button("ประมวลผลคะแนน IIEF-5"):
        total_score = sum(scores)
        st.write(f"คะแนนรวมของคุณ: {total_score}")
        if total_score <= 7:
            st.error("คุณมีปัญหาสมรรถภาพทางเพศรุนแรง")
        elif total_score <= 11:
            st.warning("คุณมีปัญหาสมรรถภาพทางเพศปานกลาง")
        elif total_score <= 16:
            st.info("คุณมีปัญหาสมรรถภาพทางเพศเล็กน้อยถึงปานกลาง")
        elif total_score <= 21:
            st.success("คุณมีปัญหาสมรรถภาพทางเพศเล็กน้อย")
        else:
            st.success("สมรรถภาพทางเพศของคุณปกติ")
        st.write("[ข้อมูลเพิ่มเติมเกี่ยวกับยา](https://flowmind-ra.my.canva.site/drugs-for-erectile-dysfunction)")
    
    # Add additional link
    st.write("[ตรวจคัดกรองอัตราการไหลปัสสาวะด้วยตนเอง](https://flowmindra.streamlit.app/)")

# Main app
def main():
    st.title("แบบสอบถามสุขภาพ")

    menu = ["IPSS", "OABSS", "IIEF-5"]
    choice = st.sidebar.selectbox("เลือกแบบสอบถาม", menu)

    if choice == "IPSS":
        render_ipss()
    elif choice == "OABSS":
        render_oabss()
    elif choice == "IIEF-5":
        render_iief5()

if __name__ == "__main__":
    main()