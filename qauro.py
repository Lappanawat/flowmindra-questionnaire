import streamlit as st
import base64
from pathlib import Path

# Function to add custom styling
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

        /* Increase font size for questions */
        .stRadio > label {{
            font-size: 26px !important; /* Larger question text */
            background-color: #FFFDD0 !important; /* Cream yellow background for all questions */
            padding: 10px; /* Add padding around the question text */
            border-radius: 5px; /* Rounded corners for questions */
            margin-bottom: 10px; /* Add space between questions */
        }}

        /* Buttons styling */
        .stButton > button {{
            font-size: 20px !important; /* Larger button text */
            background-color: #0056b3 !important;  /* Darker blue for buttons */
            color: #FFFFFF !important;             /* White button text */
            font-family: Arial, sans-serif !important;
        }}

        /* Sidebar dropdown and select box styling */
        [data-testid="stSidebar"] .stSelectbox > div > div {{
            background-color: #FFFFFF !important; /* White background for selectbox */
            border-radius: 5px !important;        /* Rounded corners */
            padding: 5px !important;              /* Padding for better spacing */
        }}

        /* Sidebar text */
        [data-testid="stSidebar"] .stSelectbox > div > div > label {{
            color: #000000 !important; /* Black text */
            font-size: 20px !important; /* Larger font size */
            font-family: Arial, sans-serif !important;
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
        "2. ในช่วง 1 เดือนที่ผ่านมา คุณต้องปัสสาวะซ้ำหลังจากที่ปัสสาวะไปแล้วไม่ถึง 2 ชั่วโมงบ่อยแค่ไหน",
        "3. ในช่วง 1 เดือนที่ผ่านมา ขณะที่คุณกำลังปัสสาวะ คุณต้องหยุดและเริ่มปัสสาวะใหม่หลายๆ ครั้งบ่อยแค่ไหน",
        "4. ในช่วง 1 เดือนที่ผ่านมา เมื่อคุณปวดปัสสาวะ คุณพบว่าคุณกลั้นปัสสาวะไม่ได้เลยบ่อยแค่ไหน",
        "5. ในช่วง 1 เดือนที่ผ่านมา คุณสังเกตเห็นว่าปัสสาวะไม่ค่อยพุ่งบ่อยแค่ไหน",
        "6. ในช่วง 1 เดือนที่ผ่านมา คุณต้องเบ่งเพื่อที่จะเริ่มปัสสาวะบ่อยแค่ไหน"
    ]
    options = [
        ["ไม่เคย (0 คะแนน)", "ประมาณ 1 ใน 5 ครั้ง (1 คะแนน)", "ประมาณ 1 ใน 3 ครั้ง (2 คะแนน)", 
         "ประมาณ 1 ใน 2 ครั้ง (3 คะแนน)", "ประมาณ 2 ใน 3 ครั้ง (4 คะแนน)", "เกือบทุกครั้ง (5 คะแนน)"]
    ] * len(questions)
    scores = []

    for idx, question in enumerate(questions):
        response = st.radio(question, options[idx], key=f"ipss_{idx}")
        scores.append(int(response.split('(')[1].split()[0]))  # Extract score from text

    # Add the 7th question with different options
    st.write("7. ในช่วง 1 เดือนที่ผ่านมา หลังจากเข้านอนตอนกลางคืนจนกระทั่งตื่นนอนตอนเช้า คุณต้องลุกขึ้นมาปัสสาวะกี่ครั้ง")
    question_7_options = [
        "ไม่เลย (0 คะแนน)", 
        "1 ครั้ง (1 คะแนน)", 
        "2 ครั้ง (2 คะแนน)", 
        "3 ครั้ง (3 คะแนน)", 
        "4 ครั้ง (4 คะแนน)", 
        "5 ครั้ง หรือมากกว่า (5 คะแนน)"
    ]
    response_7 = st.radio("", question_7_options, key="ipss_7")
    scores.append(int(response_7.split('(')[1].split()[0]))  # Extract score from text

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
            st.info("อาการเล็กน้อย")
        elif total_score >= 4 and scores[2] >= 2:
            st.warning("สงสัยมีภาวะกระเพาะปัสสาวะบีบตัวไวเกิน")
        st.write("[ข้อมูลเพิ่มเติมเกี่ยวกับยา](https://flowmind-ra.my.canva.site/drugs-for-bladder-prostate-disorders)")
    
    st.write("[ตรวจคัดกรองอัตราการไหลปัสสาวะด้วยตนเอง](https://flowmindra.streamlit.app/)")

# Function to render IIEF-5 questionnaire
def render_iief5():
    st.header("แบบประเมิน IIEF-5 Thailand (ภาวะหย่อนสมรรถภาพทางเพศ)")
    st.write("แบบสอบถามนี้ใช้สำหรับประเมินภาวะหย่อนสมรรถภาพทางเพศ (Erectile Dysfunction)")

    questions = [
        "1. ท่านมีความมั่นใจเพียงใดว่าอวัยวะเพศสามารถแข็งตัวได้และแข็งได้นานพอ",
        "2. เมื่อมีการกระตุ้นทางเพศ อวัยวะเพศแข็งตัวบ่อยแค่ไหน",
        "3. เมื่ออวัยวะเพศแข็งตัวแล้ว ท่านสามารถคงความแข็งตัวไว้ได้ยาวนานแค่ไหน",
        "4. ระหว่างมีเพศสัมพันธ์ อวัยวะเพศแข็งตัวได้มากน้อยเพียงใด",
        "5. หลังจากเสร็จสิ้นการมีเพศสัมพันธ์ ท่านมีความพึงพอใจเพียงใด"
   ]
    options = [
        [
            "ต่ำมาก (1 คะแนน)",
            "ต่ำ (2 คะแนน)",
            "ปานกลาง (3 คะแนน)",
            "สูง (4 คะแนน)",
            "สูงมาก (5 คะแนน)"
        ],
        [
            "แทบจะไม่เคยหรือไม่เคยเลย (1 คะแนน)",
            "นานๆ ครั้ง (น้อยกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (2 คะแนน)",
            "บางครั้ง (ประมาณครึ่งหนึ่งของการมีเพศสัมพันธ์ทั้งหมด) (3 คะแนน)",
            "บ่อยครั้ง (มากกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (4 คะแนน)",
            "แทบทุกครั้งหรือทุกครั้ง (5 คะแนน)"
        ],
        [
            "แทบจะไม่เคยหรือไม่เคยเลย (1 คะแนน)",
            "นานๆ ครั้ง (น้อยกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (2 คะแนน)",
            "บางครั้ง (ประมาณครึ่งหนึ่งของการมีเพศสัมพันธ์ทั้งหมด) (3 คะแนน)",
            "บ่อยครั้ง (มากกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (4 คะแนน)",
            "แทบทุกครั้งหรือทุกครั้ง (5 คะแนน)"
        ],
        [
            "ยากมากจริงๆ (1 คะแนน)",
            "ยากมาก (2 คะแนน)",
            "ค่อนข้างยาก (3 คะแนน)",
            "ง่ายเล็กน้อย (4 คะแนน)",
            "ไม่ยากเลย (5 คะแนน)"
        ],
        [
            "ไม่เคยเลย (1 คะแนน)",
            "นานๆ ครั้ง (น้อยกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (2 คะแนน)",
            "บางครั้ง (ประมาณครึ่งหนึ่งของการมีเพศสัมพันธ์ทั้งหมด) (3 คะแนน)",
            "บ่อยครั้ง (มากกว่าครึ่งของการมีเพศสัมพันธ์ทั้งหมด) (4 คะแนน)",
            "แทบทุกครั้งหรือทุกครั้ง (5 คะแนน)"
        ]
    ]

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