import streamlit as st
import docx

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
            transcript_content = uploaded_transcript.read()
            transcript_text = parse_srt(transcript_content)
        elif uploaded_transcript.name.endswith('.docx'):
            import docx
            doc = docx.Document(uploaded_transcript)
            transcript_text = "\n".join([para.text for para in doc.paragraphs])
        
        st.subheader("תוכן הקובץ שהועלה:")
        st.write(transcript_text)

        # בהמשך יבוצע כאן עיבוד מול GPT
        st.success("כאן יוצג הסיכום לאחר הפיתוח")

else:
    st.info("יש להעלות את הקבצים וללחוץ על 'הפק סיכום פגישה'")  

---

### הסבר על השינויים:

- הוספתי תמיכה בקבצי **SRT** בנוסף ל-**TXT ו-DOCX**.
- הקוד מזהה את סוג הקובץ ומטפל בכל פורמט בהתאם.
- תצוגה מקדימה לתוכן התמלול לאחר ההעלאה.

תוכל להעתיק את הקוד החדש לתוך הקובץ ב-GitHub, ללחוץ על commit, ולראות את השינוי ב-Streamlit Cloud לאחר שתטען מחדש.

עדכן אותי כשזה עובד או אם נדרש דיוק נוסף!
