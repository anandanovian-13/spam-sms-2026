import streamlit as st

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #050816;
}
h1, h2, label, p {
    color: white !important;
}
.stTextArea textarea {
    background-color: #1E2235 !important;
    color: white !important;
    border-radius: 15px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📩 SMS Spam Detection")
st.subheader("Cek apakah SMS termasuk spam:")

sms = st.text_area("Masukkan pesan SMS:", height=180)

if st.button("Deteksi"):
    if sms.strip():
        if any(k in sms.lower() for k in ["hadiah", "gratis", "menang", "klik", "voucher"]):
            st.error("⚠️ Kemungkinan SPAM")
        else:
            st.success("✅ Kemungkinan BUKAN SPAM")
    else:
        st.warning("Masukkan pesan SMS terlebih dahulu.")
