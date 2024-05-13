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
    st.image(image_path, caption='Ilustrasi gambar')
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
    st.image("c:\\Users\\mrbal\\Pictures\\Saved Pictures\\kalor.jpg", use_column_width=True)
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&display=swap');
    </style>
    <h1 style="font-family: 'Roboto Condensed', sans-serif; color: white; text-transform: uppercase; background-color: #4E154D; padding: 10px;">
        HITUNG KALORI YANG DIKONSUMSI
    </h1>
    """, unsafe_allow_html=True)
    
    # Daftar makanan yang diperluas dengan makanan populer di Indonesia
    daftar_makanan = [
        "Apel", "Pisang", "Ayam goreng", "Roti gandum", "Telur rebus", "Salmon panggang", "Nasi putih", "Kentang rebus", "Brokoli", "Yogurt rendah lemak",
        "Kacang almond", "Tomat", "Oatmeal", "Bayam", "Wortel", "Mangga", "Beras coklat", "Roti putih", "Daging sapi panggang", "Keju cheddar",
        "Kacang kedelai", "Jeruk", "Quinoa", "Lobak", "Ikan tuna kalengan dalam air", "Kacang polong", "Susu rendah lemak", "Mentimun", "Dada ayam tanpa kulit panggang",
        "Anggur", "Telur orak-arik", "Kacang merah", "Labu", "Roti gandum utuh panggang", "Bayam", "Brokoli", "Jagung manis", "Buncis", "Nanas",
        "Seledri", "Kembang kol", "Pepaya", "Paprika merah", "Bawang bombay", "Aprikot", "Kiwi", "Labu kuning", "Labu air", "Semangka", "Salak",
        "Nasi goreng", "Sate", "Bakso", "Gado-gado", "Rendang", "Pempek", "Martabak", "Kerak telor", "Tahu bulat", "Tempe goreng"
    ]

    # Inisialisasi list untuk menyimpan makanan dan kalori
    if 'makanan_terpilih' not in st.session_state:
        st.session_state.makanan_terpilih = []
        st.session_state.total_kalori = 0

    makanan_dipilih = st.selectbox('Pilih nama makanan', daftar_makanan)
    kalori = st.number_input('Masukkan jumlah kalori makanan', min_value=0.0, step=0.1)

    if st.button('Tambahkan Makanan'):
        st.session_state.makanan_terpilih.append((makanan_dipilih, kalori))
        st.session_state.total_kalori += kalori
        st.write(f"Anda telah menambahkan {makanan_dipilih} dengan {kalori:.2f} kalori.")
        st.write(f"Total kalori yang dikonsumsi: {st.session_state.total_kalori:.2f} kalori")

    # Menampilkan daftar makanan yang telah ditambahkan
    if st.session_state.makanan_terpilih:
        st.write("Daftar Makanan yang Dikonsumsi:")
        for makanan, kal in st.session_state.makanan_terpilih:
            st.write(f"{makanan} - {kal:.2f} kalori")

def page_tips_trick():
    st.image("c:\\Users\\mrbal\\Pictures\\Saved Pictures\\yoga.jpg", use_column_width=True)
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
