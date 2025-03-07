import streamlit as st
import openai
import docx

# קריאת ה-API Key מתוך ה-Secrets של Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("כלי סיכום פגישות - Famillion")

st.header("העלאת קבצי מידע לפגישה")

uploaded_transcript = st.file_uploader("העלה קובץ תמלול או סיכום פגישה", type=['txt', 'docx', 'srt'])
uploaded_excel = st.file_uploader("העלה קובץ אקסל (מידע לקוח, מוצרים)", type=['xlsx'])

st.header("בחירת תהליכים מובנים")
selected_processes = st.multiselect(
    "בחר תהליכים מתוך הרשימה",
    ["ביטוח חיים", "ביטוח בריאות", "ביטוח סיעודי", "חיסכון פנסיוני", "השקעות", "הלוואות", "משכנתאות"]
)

def parse_srt(srt_content):
    """פונקציה להמרת קובץ SRT לטקסט נקי"""
    lines = srt_content.decode('utf-8').splitlines()
    parsed_text = []
    for line in lines:
        if line.strip().isdigit() or '-->' in line:
            continue
        if line.strip():
            parsed_text.append(line.strip())
    return ' '.join(parsed_text)

transcript_text = ""

if st.button("הפק סיכום פגישה"):
    if uploaded_transcript is not None:
        if uploaded_transcript.name.endswith('.txt'):
            transcript_text = uploaded_transcript.read().decode('utf-8')
        elif uploaded_transcript.name.endswith('.srt'):
            transcript_text = parse_srt(uploaded_transcript.read())
        elif uploaded_transcript.name.endswith('.docx'):
            doc = docx.Document(uploaded_transcript)
            transcript_text = '\n'.join([para.text for para in doc.paragraphs])

    if transcript_text:
        st.subheader("תוכן התמלול שהועלה:")
        st.write(transcript_text)

        # יצירת פרומפט לשליחה ל-GPT
        prompt = f"""
        סכם את הטקסט הבא בצורה מובנית וברורה, תוך שימוש בכותרות רלוונטיות:
        {transcript_text}
        """

        # קריאה ל-OpenAI API בגרסה המעודכנת
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        # קבלת הסיכום והצגתו
        summary = response.choices[0].message.content

        st.subheader("סיכום AI:")
        st.write(summary)
    else:
        st.error("הקובץ שהועלה ריק או לא תקין, אנא בדוק שוב.")

else:
    st.info("העלה את הקבצים ולחץ על הכפתור להפקת סיכום הפגישה")
