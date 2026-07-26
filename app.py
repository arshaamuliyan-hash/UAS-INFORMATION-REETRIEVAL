import streamlit as st
import json
import os

# Menunjuk ke lokasi file data/books.json
DATA_PATH = "data/books.json"

st.set_page_config(page_title="Book Search (Scraped via Scrapy)", layout="wide")
st.title("📚 Book Search (Scraped via Scrapy)")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("Cari...", "")

# Filter data berdasarkan judul buku
if query:
    filtered = [item for item in data if item.get("title") and query.lower() in item["title"].lower()]
else:
    filtered = data

st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")

# Tampilkan hasil pencarian
for item in filtered:
    st.markdown(f"### [{item.get('title', 'No Title')}]({item.get('link', '#')})")
    
    # Ambil nilai atau berikan default jika None
    price = item.get('price') or "N/A"
    rating = item.get('rating') or "Not rated"
    availability = item.get('availability') or "In stock"
    
    st.markdown(
        f"**Price:** {price} | "
        f"**Rating:** {rating} | "
        f"**Availability:** {availability}"
    )
    st.markdown("---")