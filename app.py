import streamlit as st
from datetime import datetime, timedelta

st.title("🕒 Arbeitszeit-Rechner")

# 🔤 Manuelle Eingabe der Startzeit
startzeit_str = st.text_input("Wann hast du angefangen zu arbeiten? (HH:MM)", value="08:00")

# ⌛ Arbeitsdauer eingeben
stunden = st.number_input("Stunden, die du arbeiten willst:", min_value=0, max_value=24, value=8)
minuten = st.number_input("Zusätzliche Minuten:", min_value=0, max_value=59, value=0)

# 💻 Berechnen, wenn Button gedrückt
if st.button("🧮 Feierabendzeit berechnen"):
    try:
        # 🔍 Zeit parsen
        startzeit = datetime.strptime(startzeit_str, "%H:%M")
        arbeitsdauer = timedelta(hours=stunden, minutes=minuten)
        feierabend = startzeit + arbeitsdauer

        st.success(f"✅ Du kannst um **{feierabend.strftime('%H:%M')} Uhr** Feierabend machen!")
    except ValueError:
        st.error("❌ Bitte gib die Zeit im Format HH:MM ein (z. B. 08:15)")
