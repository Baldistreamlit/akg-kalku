import streamlit as st
import pandas as pd

def hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin, faktor_aktivitas):
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi) - (5.677 * umur)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi) - (4.330 * umur)
    else:
        return "Jenis kelamin tidak valid"

    tee = bmr * faktor_aktivitas
    return tee

def page_kebutuhan_energi():
    image_path = 'hitung.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='menghitung yang dibutuhkan')
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&display=swap');
    </style>
    <h1 style="font-family: 'Roboto Condensed', sans-serif; color: white; text-transform: uppercase; background-color: #4E154D; padding: 10px;">
        HITUNG KALORI YANG DIBUTUHKAN
    </h1>
    """, unsafe_allow_html=True)

    with st.expander("Tentang Kalkulator Ini"):
        st.markdown("""
        *Fungsi dari Kalkulator Kebutuhan Energi:*
        Kalkulator ini dirancang untuk membantu Anda memahami jumlah kalori yang Anda butuhkan setiap hari berdasarkan beberapa faktor seperti umur, berat badan, tinggi badan, jenis kelamin, dan tingkat aktivitas. Menggunakan rumus Basal Metabolic Rate (BMR) dan faktor aktivitas, kalkulator ini mengestimasi Total Daily Energy Expenditure (TDEE) Anda. TDEE adalah jumlah total kalori yang Anda butuhkan untuk mempertahankan berat badan Anda saat ini. Jika Anda ingin menurunkan atau menaikkan berat badan, Anda dapat menyesuaikan asupan kalori Anda berdasarkan TDEE yang dihitung.
        """)

    umur = st.number_input('Masukkan umur (tahun)', min_value=0, step=1)
    berat_badan = st.number_input('Masukkan berat badan (kg)', min_value=0.0, step=0.1)
    tinggi = st.number_input('Masukkan tinggi (cm)', min_value=0.0, step=0.1)
    jenis_kelamin = st.selectbox('Pilih jenis kelamin', ['Laki-laki', 'Perempuan'])
    faktor_aktivitas = st.selectbox('Pilih tingkat aktivitas', [
        (1.2, 'Sedentari: Sedikit atau tidak ada olahraga'),
        (1.375, 'Ringan aktif: Olahraga ringan/sport 1-3 hari/minggu'),
        (1.55, 'Moderat aktif: Olahraga moderat/sport 3-5 hari/minggu'),
        (1.725, 'Sangat aktif: Olahraga berat/sport 6-7 hari seminggu'),
        (1.9, 'Super aktif: Olahraga sangat berat/pekerjaan fisik & olahraga 2x/hari')
    ], format_func=lambda x: x[1])
    kalori_dikonsumsi = st.number_input('Masukkan jumlah kalori yang dikonsumsi hari ini', min_value=0.0, step=0.1)

    if st.button('Hitung Kebutuhan Energi'):
        tdee = hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin, faktor_aktivitas[0])
        if isinstance(tdee, str):
            st.error(tdee)
        else:
            st.success(f"Total Kebutuhan Energi Harian Anda (TDEE) adalah: {tdee:.2f} kalori")
            if kalori_dikonsumsi > tdee:
                st.warning(f"Anda mengonsumsi {kalori_dikonsumsi - tdee:.2f} kalori lebih banyak dari yang dibutuhkan.")
                st.markdown("""
                *Saran untuk Mengurangi Asupan Kalori:*
                - Kurangi porsi makanan tinggi kalori.
                - Perbanyak konsumsi buah dan sayuran.
                - Hindari minuman manis dan alkohol.
                - Tingkatkan aktivitas fisik untuk membakar kalori lebih banyak.
                - Pertimbangkan untuk berkonsultasi dengan ahli gizi.
                """)
            elif kalori_dikonsumsi < tdee:
                st.warning(f"Anda mengonsumsi {tdee - kalori_dikonsumsi:.2f} kalori kurang dari yang dibutuhkan.")
                st.markdown("""
                *Saran untuk Menambah Asupan Kalori:*
                - Tingkatkan porsi makanan bergizi.
                - Konsumsi makanan yang kaya protein dan karbohidrat kompleks.
                - Makanan ringan di antara waktu makan untuk meningkatkan asupan kalori.
                - Pertimbangkan untuk mengonsumsi suplemen kalori jika diperlukan.
                - Berkonsultasilah dengan ahli gizi untuk membuat rencana diet yang sesuai.
                """)
            else:
                st.success("Asupan kalori Anda sesuai dengan kebutuhan energi harian Anda.")

def page_konsumsi_kalori():
    image_path = 'kalor.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='kalori makanan')
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&display=swap');
    </style>
    <h1 style="font-family: 'Roboto Condensed', sans-serif; color: white; text-transform: uppercase; background-color: #4E154D; padding: 10px;">
        HITUNG KALORI YANG DIKONSUMSI
    </h1>
    """, unsafe_allow_html=True)
    
   data_kalori = {
        "Apel": 52, "Pisang": 89, "Ayam goreng": 240, "Roti gandum": 247, "Telur rebus": 155,
        "Salmon panggang": 206, "Nasi putih": 130, "Kentang rebus": 87, "Brokoli": 34,
        "Yogurt rendah lemak": 63, "Nasi goreng": 190, "Sate": 290, "Bakso": 120,
        "Gado-gado": 149, "Rendang": 195, "Pempek": 180, "Martabak": 320, "Kerak telor": 250,
        "Tahu bulat": 275, "Tempe goreng": 193, "Soto ayam": 89, "Bubur ayam": 65,
        "Mie goreng": 206, "Lumpia": 175, "Es cendol": 90, "Kue cubit": 221, "Pisang goreng": 150,
        "Kerupuk": 480, "Opor ayam": 245, "Sayur asem": 40, "Serabi": 216, "Otak-otak": 134,
        "Klepon": 120, "Lemper": 198, "Pastel": 289, "Risoles": 229, "Kue lapis": 289,
        "Bika Ambon": 320, "Kue Lumpur": 198, "Kue Sus": 300, "Kue Serabi": 221, "Kue Pukis": 321,
        "Kue Putu": 130, "Kue Cucur": 150, "Kue Dadar Gulung": 182, "Kue Kastengel": 500,
        "Kue Nastar": 480, "Kue Semprit": 450, "Kue Soes": 260, "Kue Tape": 160, "Kue Wingko": 350,
        "Kue Bawang": 530, "Kue Kering": 500, "Kue Bolu": 340, "Kue Donat": 452, "Kue Brownies": 466,
        "Kue Tart": 270, "Kue Pandan": 220, "Kue Talam": 180
    }

    if 'makanan_terpilih' not in st.session_state:
        st.session_state.makanan_terpilih = []
        st.session_state.total_kalori = 0

    makanan_dipilih = st.selectbox('Pilih nama makanan', list(data_kalori.keys()))
    berat_makanan = st.number_input('Masukkan berat makanan yang dikonsumsi (gram)', min_value=0.0, step=0.1)

    if st.button('Tambahkan Makanan'):
        kalori_per_100g = data_kalori[makanan_dipilih]
        kalori = (kalori_per_100g * berat_makanan) / 100
        st.session_state.makanan_terpilih.append((makanan_dipilih, berat_makanan, kalori))
        st.session_state.total_kalori += kalori
        st.success(f"Anda telah menambahkan {makanan_dipilih} dengan {kalori:.2f} kalori.")
        st.info(f"Total kalori yang dikonsumsi: {st.session_state.total_kalori:.2f} kalori")

    if st.session_state.makanan_terpilih:
        st.write("Daftar Makanan yang Dikonsumsi:")
        for makanan, berat, kal in st.session_state.makanan_terpilih:
            st.write(f"{makanan} ({berat} gram) - {kal:.2f} kalori")

def page_tips_trick():
    image_path = 'yoga.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='tips sehat')
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&display=swap');
    </style>
    <h1 style="font-family: 'Roboto Condensed', sans-serif; color: white; text-transform: uppercase; background-color: #4E154D; padding: 10px;">
        TIPS & TRICK KESEHATAN
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Tips Menjaga Kesehatan
    - *Olahraga Teratur:* Lakukan olahraga secara teratur untuk menjaga kebugaran dan kesehatan tubuh.
    - *Pola Makan Seimbang:* Konsumsi makanan yang seimbang dengan gizi yang cukup dan variatif.
    - *Cukup Tidur:* Pastikan untuk mendapatkan tidur yang cukup setiap malam untuk pemulihan energi.
    - *Hidrasi yang Cukup:* Minum cukup air setiap hari untuk menjaga hidrasi tubuh.
    - *Manajemen Stres:* Lakukan aktivitas yang dapat mengurangi stres seperti meditasi, membaca, atau hobi lainnya.
    """)

    st.markdown("""
    ### Tips Menjaga Kalori
    - *Pantau Asupan:* Gunakan aplikasi atau catatan harian untuk melacak jumlah kalori yang Anda konsumsi setiap hari.
    - *Pilih Makanan Rendah Kalori:* Fokus pada buah, sayuran, dan protein tanpa lemak.
    - *Hindari Minuman Manis:* Minuman manis dapat menambah asupan kalori yang tidak perlu.
    """)

    st.markdown("""
    ### Tips Memilih Makanan Sehat
    - *Baca Label Nutrisi:* Perhatikan label nutrisi dan pilih makanan dengan sedikit tambahan gula, garam, dan lemak jenuh.
    - *Variasi Makanan:* Konsumsi berbagai jenis makanan untuk mendapatkan berbagai nutrisi.
    - *Masak di Rumah:* Memasak di rumah membantu Anda mengontrol bahan dan porsi makanan.
    """)

def main():
    st.sidebar.title("Menu Navigasi")
    choice = st.sidebar.radio("Pilih Halaman:", ["Kebutuhan Energi", "Konsumsi Kalori", "Tips & Trick"])

    if choice == "Kebutuhan Energi":
        page_kebutuhan_energi()
    elif choice == "Konsumsi Kalori":
        page_konsumsi_kalori()
    elif choice == "Tips & Trick":
        page_tips_trick()

    # Sidebar untuk Informasi Tim
    with st.sidebar.expander("Informasi Tim"):
        st.write('Kelompok 4')
        st.write('Anggota:')
        st.write('- Amara Rifa Pratamy')
        st.write('- Muhammad Baldiyansyah')
        st.write('- Shofi Nabila Khoirunnisa')
        st.write('- Tabitha Zoeana Salsabila')
        st.write('- Afdatul Saputra')

    # Sidebar untuk Informasi Rumus
    with st.sidebar.expander("Informasi Rumus"):
        st.write("""
        Rumus Basal Metabolic Rate (BMR):
        - Untuk laki-laki: BMR = 88.362 + (13.397 x berat badan dalam kg) + (4.799 x tinggi dalam cm) - (5.677 x umur dalam tahun)
        - Untuk perempuan: BMR = 447.593 + (9.247 x berat badan dalam kg) + (3.098 x tinggi dalam cm) - (4.330 x umur dalam tahun)
        """)

if __name__ == "__main__":
    main()
