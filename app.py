import streamlit as st
import docx

st.title("כלי סיכום פגישות - Famillion")

st.header("העלאת קבצי מידע לפגישה")

uploaded_transcript = st.file_uploader("העלה קובץ תמלול או סיכום פגישה", type=['txt', 'docx', 'srt'])
uploaded_excel = st.file_uploader("העלה קובץ אקסל (מידע לקוח, מוצרים)", type=['xlsx'])

st.header("בחירת תהליכים מתוך רשימה סגורה")

selected_processes = st.multiselect(
    "בחר תהליכים",
    ["ביטוח חיים", "ביטוח בריאות", "ביטוח סיעודי", "חיסכון פנסיוני", "השקעות", "הלוואות", "משכנתאות"]
)

def parse_srt(srt_content):
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
        st.success("כאן יוצג הסיכום לאחר פיתוח המערכת")
    else:
        st.error("הקובץ שהועלה ריק או לא תקין, אנא בדוק שוב.")

else:
    st.info("העלה את הקבצים ולחץ על הכפתור להפקת סיכום הפגישה")
