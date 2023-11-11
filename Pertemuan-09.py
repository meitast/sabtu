import streamlit as st

# ini bagian heading aplikasi streamlit
st.title("Pertemuan Praktikum Big Data")
st.write("Meita Indah Fadilla")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")
st.write("#### Semangat") #maksimal 6 hastag

# kinerja unit
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)

# pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

"""
ini komentar
"""

makanan = st.radio('Makanan kesukaan',['Bakso', 'Nasi Goreng', 'Mie Ayam'])

st.write(makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan', ['Es Teh', 'Kopi', 'Jus'])

st.write(minuman)

bayar = st.multiselect('Bayar pakai', ['Tunai', 'Ovo', 'Gopay'])
st.write(bayar)