import streamlit as st

st.title("כלי סיכום פגישות - Famillion")

st.header("העלאת קבצי מידע לפגישה")

uploaded_transcript = st.file_uploader("העלה קובץ תמלול או סיכום פגישה", type=['txt', 'docx'])
uploaded_excel = st.file_uploader("העלה קובץ אקסל (מידע לקוח, מוצרים)")

st.header("בחירת תהליכים מובנים")
selected_processes = st.multiselect(
    "בחר תהליכים מתוך הרשימה",
    ["ביטוח חיים", "ביטוח בריאות", "ביטוח סיעודי", "חיסכון פנסיוני", "השקעות", "הלוואות", "משכנתאות"]
)

if st.button("הפק סיכום פגישה"):
    st.success("כאן יוצג הסיכום לאחר הפיתוח")
