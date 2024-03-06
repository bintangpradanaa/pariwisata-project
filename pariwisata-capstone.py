import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
from streamlit_folium import st_folium
import folium
import requests


# set wide layout
st.set_page_config(layout='wide')
st.markdown('<div style="text-align: center;font-size:48px;font-weight:bold;line-height:1.5;"">Menilik Perkembangan dan Potensi</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:38px;font-weight:bold;line-height:1.5;margin-bottom:20px">Sektor Pariwisata Indonesia</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:14px;">Oleh: Bintang Ary Pradana</div>', unsafe_allow_html=True)

url_geojson = 'https://raw.githubusercontent.com/bintangpradanaa/capstone-project-pariwisata/main/indonesia-prov.geojson'

# Membaca data GeoJSON dari URL menggunakan requests
response = requests.get(url_geojson)
geo_data = response.json()

#Preparing data
kontribusi_pdb = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT8iE1Ad5jXNE-H2q9qbkFZu4880rox7emIcbGyIO4YCuOQSpvKmuVqSMxZFcHJkeEmAIb_tOyOxXuM/pub?gid=1545651756&single=true&output=csv')
devisa = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQy8potYfuEl1wQqjXRFC4br5SYZqRdrvebeOKZQeF7c2W8ZNcpfa89NM-db6_x7cP_P7LW8SaUVbyw/pub?gid=817736906&single=true&output=csv')
wisman_negara = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRzjtkBbX6dGavfqFqhGmLvVVXi7MOmGRQIETwxA9w95-sh9Vmenq7UNoAFzdLKboOcSHX5T-5j-IOG/pub?gid=1252955691&single=true&output=csv')
wisman_pintu_masuk = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTlHom2fhNefsOYiq56J_ANGl5qLByGLnD2scOmRW6JfzWI92FgbUhsT5kyWMjsysIO9gErBjBBqrzB/pub?gid=1140289420&single=true&output=csv')
wisnus_perprov = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vS3_oSEgKxgImAdVgE-yZ2Lqo9rRQqvZILTe4wkj4DuqBdpDOLIQWpzjexCEvbpFJnzhGGgXyyguvI_/pub?gid=1127350039&single=true&output=csv')
tpk_hotel = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vS0CG6a7AT-t_Y7pNSROV7wk87k3rHelcKGh6Ci_PTboGfPTUGTh4EqiEO2YY-C9CAfR0mR7mAi0BVS/pub?gid=1585487888&single=true&output=csv')
hotel_akomodasi_kamar = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSs7ogde93nAZMymVWAWq3bfWKuqwvby9ZYvjeRbtWDIDoaDv3majjOMoTeW2PYXITlD_4SIGeIRZul/pub?gid=1328289260&single=true&output=csv')
asean_wisatawan = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTJ5wWR7Nn2nfMFJ4bnQLRABIMJGGokt5Xnpu7P8_0e15SXlTgeanW1_aZ32oj0FlONJRho4sPK_B5w/pub?gid=997253045&single=true&output=csv')
status_pariwisata = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSnD_dRmw-m1uSpBk5H4mYjOPWIcemuRXqAb151KCUNEX342W7rjvUR5sZuXOAjcm1MdL10kZyh8cSi/pub?gid=1209728406&single=true&output=csv')
dtw_sisparnas = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQA6KoarZJtOIgFNWZ-YN06htkDWJusN3ZK_1sUC3ml3hBgbZV-tQH8e1eqiRptQLAyCzCzF6THtEFv/pub?gid=417353498&single=true&output=csv')
jenis_dtw_pariwisata = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRGbAGJLm-F9TY2TpeoGVMg0ydSKkFLolg_sG2Kr-sTGhAJX8WbSetWxr63CrZuT4XJyl_llvwVLj53/pub?gid=188056455&single=true&output=csv')

curr_year_pdb = int(max(kontribusi_pdb['tahun']))
prev_year_pdb = curr_year_pdb - 1
curr_year_devisa = int(max(devisa['tahun']))
prev_year_devisa = curr_year_devisa - 1
curr_year_wisman = int(max(wisman_negara['tahun']))
prev_year_wisman = curr_year_wisman - 1
curr_year_wisman_pintu = int(max(wisman_pintu_masuk['tahun']))
prev_year_wisman_pintu = curr_year_wisman_pintu - 1
curr_year_wisnus = int(max(wisnus_perprov['tahun']))
prev_year_wisnus = curr_year_wisnus - 1
curr_year_tpk = int(max(tpk_hotel['tahun']))
prev_year_tpk = curr_year_tpk - 1
curr_year_hotel_akomodasi_kamar = int(max(hotel_akomodasi_kamar['tahun']))
prev_year_hotel_akomodasi_kamar = curr_year_hotel_akomodasi_kamar - 1
curr_year_asean = int(max(asean_wisatawan['year']))
prev_year_asean = curr_year_asean - 1


# data kunjungan wisman negara
kunjungan_wisman_pertahun = pd.pivot_table(
    data=wisman_negara,
    index='tahun',
    aggfunc={
        'jumlah_kunjungan_wisman':'sum',
}
).reset_index()

# data kunjungan wisman perbulan 
kunjungan_wisman_perbulan = pd.pivot_table(
    data=wisman_negara,
    index=['bulan', 'tahun'],
    aggfunc={
        'jumlah_kunjungan_wisman':'sum'
}
).reset_index()

# data kunjungan wisman perpintu masuk
kunjungan_wisman_perpintu = pd.pivot_table(
    data=wisman_pintu_masuk,
    index=['tahun', 'jenis_pintu_masuk'],
    aggfunc={
        'jumlah_kunjungan_wisman':'sum'
    }
).reset_index()

# data kunjungan wisman pintu masuk (tujuan provinsi)
kunjungan_wisman_perprov = pd.pivot_table(
    data=wisman_pintu_masuk,
    index=['tahun', 'provinsi','jenis_pintu_masuk'],
    aggfunc={
        'jumlah_kunjungan_wisman':'sum'
    }
).reset_index()
kunjungan_wisman_perprov = kunjungan_wisman_perprov.sort_values(by='tahun', ascending=False)
# data kunjungan wisnus pertahun
kunjungan_wisnus_pertahun = pd.pivot_table(
    data = wisnus_perprov,
    index = 'tahun',
    aggfunc = {
        'jumlah_kunjungan_wisnus':'sum',
}
).reset_index()

# data rata-rata tpk hotel pertahun
avg_tpk_hotel = pd.pivot_table(
    data = tpk_hotel,
    index = 'tahun',
    aggfunc = {
        'persentase_tpk_hotel_bintang':'mean',
        'persentase_tpk_hotel_nonbintang' : 'mean'
}
).reset_index()
avg_tpk_hotel['avg_persentase_tpk_hotel_nasional'] = (avg_tpk_hotel['persentase_tpk_hotel_bintang'] + avg_tpk_hotel['persentase_tpk_hotel_nonbintang']) / 2

# data jumlah hotel, akomodasi, dan kamar
hotel_akomodasi_kamar_pertahun = pd.pivot_table(
    data = hotel_akomodasi_kamar,
    index = 'tahun',
    aggfunc = {
        'jumlah_hotel':'sum',
        'jumlah_kamar':'sum'
        
}
).reset_index()

    #helper function
def format_big_number(num):
    if num >= 1e9:
        return f"{num / 1e9:.2f} B"
    elif num >= 1e6:
        return f"{num / 1e6:.2f} M"
    elif num >= 1e3:
        return f"{num / 1e3:.2f} K"
    else:
        return f"{num:.2f}"

st.markdown('''<div style="font-size: 17px; text-align: center; margin-top: 50px; margin-bottom: 40px; margin-right:35px; margin-left:35px;">
           Indonesia memiliki keindahan alam yang memukau dan kekayaan budaya yang melimpah, menjadikannya destinasi pariwisata yang menarik di mata dunia. 
           Namun, terdapat tantangan dan potensi yang perlu diperhatikan dengan cermat. Dengan ini, perlunya memahami bagaimana kondisi sektor pariwisata Indonesia
           dengan melihat kontribusinya terhadap ekonomi, jumlah kunjungan wisatawan, tingkat hunian hotel, perbandingan dengan negara-negara tetangga di ASEAN, 
           serta potensi pariwisata Indonesia. Dengan pemahaman yang mendalam terhadap dinamika industri pariwisata, diharapkan kita dapat memiliki pandangan yang 
           lebih komprehensif mengenai kondisi dan prospek masa depan pariwisata Indonesia. </div>''', unsafe_allow_html=True)
# Highlight
st.markdown('---')
st.markdown("<p style='color: gray; font-style: italic;'>Compared to Last Year</p>", unsafe_allow_html=True)
mx_pdb, mx_devisa, mx_wisman, mx_wisnus = st.columns(4)
with mx_pdb:
    curr_pdb = kontribusi_pdb.loc[kontribusi_pdb['tahun'] == curr_year_pdb, 'persentase_kontribusi_pariwisata_terhadap_pdb'].values[0]
    prev_pdb = kontribusi_pdb.loc[kontribusi_pdb['tahun'] == prev_year_pdb, 'persentase_kontribusi_pariwisata_terhadap_pdb'].values[0]
    pdb_diff = curr_pdb - prev_pdb
    st.metric("Kontribusi Pariwisata (PDB) 2023", value=f'{curr_pdb:.2f}%', delta=f'{pdb_diff:.2f}%')
with mx_devisa:
    curr_devisa = devisa.loc[devisa['tahun'] == curr_year_devisa, 'jumlah_devisa_pariwisata_milyar_usd'].values[0]
    prev_devisa = devisa.loc[devisa['tahun'] == prev_year_devisa, 'jumlah_devisa_pariwisata_milyar_usd'].values[0]
    devisa_diff_percent = 100.0 * (curr_devisa - prev_devisa) / prev_devisa
    st.metric("Devisa Pariwisata 2023", value=f'{curr_devisa}B USD', delta=f'{devisa_diff_percent:.2f}%')
with mx_wisman:
    curr_wisman = kunjungan_wisman_pertahun.loc[kunjungan_wisman_pertahun['tahun'] == curr_year_wisman, 'jumlah_kunjungan_wisman'].values[0]
    prev_wisman = kunjungan_wisman_pertahun.loc[kunjungan_wisman_pertahun['tahun'] == prev_year_wisman, 'jumlah_kunjungan_wisman'].values[0]
    wisman_diff_percent = 100.0 * (curr_wisman - prev_wisman) / prev_wisman
    st.metric("Kunjungan Wisatawan Mancanegara 2023", value=format_big_number(curr_wisman), delta=f'{wisman_diff_percent:.2f}%')
with mx_wisnus:
    curr_wisnus = kunjungan_wisnus_pertahun.loc[kunjungan_wisnus_pertahun['tahun'] == curr_year_wisnus, 'jumlah_kunjungan_wisnus'].values[0]
    prev_wisnus = kunjungan_wisnus_pertahun.loc[kunjungan_wisnus_pertahun['tahun'] == prev_year_wisnus, 'jumlah_kunjungan_wisnus'].values[0]
    wisnus_diff_percent = 100.0 * (curr_wisnus - prev_wisnus) / prev_wisnus
    st.metric("Kunjungan Wisatawan Nusantara 2023", value=format_big_number(curr_wisnus), delta=f'{wisnus_diff_percent:.2f}%')
st.markdown('---')

st.markdown('''<div style="font-size: 16px; text-align: center; margin-top: 30px;">
        Pada tahun 2023, Indonesia mencatat peningkatan yang signifikan dalam sektor pariwisata. Kontribusi pariwisata terhadap Produk Domestik Bruto (PDB) 
        dan devisa pariwisata meningkat, menunjukkan dampak positifnya terhadap ekonomi negara. Jumlah kunjungan wisatawan mancanegara (wisman) meningkat hampir dua 
        kali lipat, menjadi 11.26 juta kunjungan. Sementara itu, kenaikan kunjungan wisatawan nusantara (wisnus) tercatat relatif lebih rendah, hanya sebesar 
        1.94%. Peningkatan ini mencerminkan daya tarik Indonesia yang kaya akan keindahan alam, kekayaan budaya, dan beragam pengalaman yang ditawarkan kepada 
        para wisatawan.\
        
        <p style="font-size: 23px; text-align: center; font-weight:bold; margin-bottom:30px; margin-top:60px; margin-left:20px; margin-right:20px">
        Lantas, Apakah tren pertumbuhan ini akan berlanjut secara konsisten setiap tahun?</p></div>''', unsafe_allow_html=True)
st.markdown('---')

# Header 1: ekonomi pariwisata
st.header('Kontribusi Pariwisata terhadap Ekonomi Indonesia')
st.write('**Grafik 1.** Devisa Pariwisata dan Kontribusi Pariwisata terhadap PDB')
st.write('')

pariwisata_eco,_, isi_eco = st.columns([1.5, 0.1, 1.4])
with pariwisata_eco:
    pdb_line = alt.Chart(kontribusi_pdb[kontribusi_pdb['tahun'] >= 2017]).mark_line(strokeWidth=3.5).encode(
    alt.X('tahun:N', title='Tahun', axis=alt.Axis(labelAngle=0)),
    alt.Y('persentase_kontribusi_pariwisata_terhadap_pdb', 
          title='Kontribusi Pariwisata terhadap PDB (%)', 
          scale=alt.Scale(padding=20)),
    color=alt.value('#1647C1')
    ).properties(width = 120, height= 380)
    
    devisa_bar = alt.Chart(devisa[devisa['tahun'] >= 2017]).mark_bar().encode(
    alt.X('tahun:N', title='Tahun', axis=alt.Axis(labelAngle=0)),
    alt.Y('jumlah_devisa_pariwisata_milyar_usd:Q', 
          title='Devisa Pariwisata (Miliar USD)',
          scale=alt.Scale(padding=20, domain=[0, 18]), 
          axis=alt.Axis(labels=True)),
    color=alt.value('#E95C1D'), 
    ).properties(width = 120, height= 380)

    eco_combo_chart = alt.layer(devisa_bar, pdb_line).resolve_scale(y='independent')
    st.altair_chart(eco_combo_chart, use_container_width=True)
    
with isi_eco:
    target_minimum_devisa_2023 = 2.07
    target_maksimum_devisa_2023 = 5.95
    target_devisa_2024 = 7.38
    capaian_devisa_2023 = devisa.loc[devisa['tahun'] == curr_year_devisa, 'jumlah_devisa_pariwisata_milyar_usd'].values[0]
    capaian_devisa_2024 = 'No Data'
        
    if capaian_devisa_2023 > target_maksimum_devisa_2023:
        capaian_devisa_2023_percent = 100*  (capaian_devisa_2023 / target_maksimum_devisa_2023) 
    else:
        capaian_devisa_2023_percent = 100 * (capaian_devisa_2023 / target_minimum_devisa_2023)
                    
    target_2023_eco_col, target_2024_eco_col = st.columns(2)
    with target_2023_eco_col:
        st.metric('Target Minimum Devisa Pariwisata 2023', f'{target_minimum_devisa_2023}B USD')
        capaian_devisa_2023_text = f'<span style="font-size: 20px; font-weight: bold;">{capaian_devisa_2023_percent:.2f}%</span>'
        capaian_devisa_2023_color = "green" if capaian_devisa_2023_percent > 100 else "red"
        st.write(f'Capaian: <span style="color: {capaian_devisa_2023_color};">{capaian_devisa_2023_text}</span>', unsafe_allow_html=True)
    with target_2024_eco_col:
        st.metric('Target Minimum Devisa Pariwisata 2024', f'{target_devisa_2024}B USD')
        capaian_devisa_2024_color = "green" if capaian_devisa_2024 != 'No Data' else "red"
        st.write(f'Capaian: <span style="color: {capaian_devisa_2024_color};">{capaian_devisa_2024}</span>', unsafe_allow_html=True)
    
    st.write('''<p style = "font-size:15px; text-align:justify;">
            Kementerian Pariwisata dan Ekonomi Kreatif (Kemenparekraf) telah menetapkan target devisa pariwisata tahun 2023 sebesar 
            2,07 - 5,95 miliar USD. Ternyata, devisa yang berhasil dihasilkan jauh melampaui target yang ditetapkan, bahkan mencapai 
            lebih dari dua kali lipat dari yang diharapkan.</p>''', unsafe_allow_html=True)
    st.warning('''
               _Di tahun 2024, Kemenparekraf menetapkan target baru devisa minimum sebesar 7.38 juta USD. Langkah ini mencerminkan optimisme dan 
               keyakinan akan potensi pertumbuhan lebih lanjut dalam industri pariwisata Indonesia._''')
    
st.write('''<p style = "font-size:15px; text-align:justify;">
        Dalam rentang tahun 2017 hingga 2019, sektor pariwisata Indonesia menunjukkan pertumbuhan yang stabil, baik dalam hal 
        pendapatan devisa maupun kontribusinya terhadap Produk Domestik Bruto (PDB). Namun, ketika pandemi melanda pada tahun 2020, 
        sektor pariwisata mengalami dampak yang sangat signifikan. Pada puncaknya, yaitu tahun 2021, pendapatan devisa dari pariwisata 
        hanya mencapai 520 juta USD. Meskipun demikian, seiring berjalannya waktu, sektor pariwisata mulai perlahan naik dan menunjukkan 
        tanda-tanda pemulihan. </p>''', unsafe_allow_html=True)
st.info('''
        _**Setelah tahun 2023, sektor pariwisata Indonesia diharapkan terus menunjukkan pertumbuhan positif, dengan asumsi situasi 
        global tetap stabil dan minimnya faktor-faktor yang mempengaruhi pariwisata, seperti pembatasan interaksi lintas negara atau
        kebijakan yang merugikan industri pariwisata.** Selain itu, pemerintah juga perlu gencar meningkatkan daya tarik pariwisata, 
        memperbaiki infrastruktur pariwisata, dan menyajikan pengalaman wisata yang lebih menarik._''')


                
# Header 2: Wisman
st.header('Tren dan Profile Kunjungan Wisatawan Mancanegara')

wisman_pertahun,_, isi_wisman_pertahun = st.columns([1.5, 0.1, 1.4])
with wisman_pertahun:
    fig_bar_wisman_pertahun = px.bar(kunjungan_wisman_pertahun, 
                                    x='tahun', 
                                    y='jumlah_kunjungan_wisman',
                                    title='Grafik 2. Jumlah Kunjungan Wisman per Tahun',
                                    labels={'tahun': 'Tahun', 'jumlah_kunjungan_wisman': 'Jumlah Kunjungan Wisman'},
                                    color_discrete_sequence=['#8892E1'])
    fig_bar_wisman_pertahun.update_layout(width=800, height=480)
    st.plotly_chart(fig_bar_wisman_pertahun, use_container_width=True)
    
with isi_wisman_pertahun:
    st.write('')
    st.write('')
    target_wisman_2023 = 8500000
    target_wisman_2024 = 14.30
    capaian_wisman_2023 = kunjungan_wisman_pertahun.loc[kunjungan_wisman_pertahun['tahun'] == curr_year_wisman, 'jumlah_kunjungan_wisman'].values[0]
    capaian_wisman_2024 = 'No Data'
    capaian_wisman_2023_percent = 100 * (capaian_wisman_2023 / target_wisman_2023)
    
    target_2023_wisman_col, target_2024_wisman_col = st.columns(2)
    with target_2023_wisman_col:
        st.metric('Target Minimum Kunjungan Wisman 2023', format_big_number(target_wisman_2023))
        capaian_wisman_2023_text = f'<span style="font-size: 20px; font-weight: bold;">{capaian_wisman_2023_percent:.2f}%</span>'
        capaian_wisman_2023_color = "green" if capaian_wisman_2023_percent > 100 else "red"
        st.write(f'Capaian: <span style="color: {capaian_wisman_2023_color};">{capaian_wisman_2023_text}</span>', unsafe_allow_html=True)

    with target_2024_wisman_col:
        st.metric('Target Minimum Kunjungan Wisman 2024', f'{target_wisman_2024} M')
        capaian_wisman_2024_color = "green" if capaian_wisman_2024 != 'No Data' else "red"
        st.write(f'Capaian: <span style="color: {capaian_wisman_2024_color};">{capaian_wisman_2024}</span>', unsafe_allow_html=True)
        
    st.write('''<p style= "font-size:15px; text-align:justify;">
            Walaupun masih berada dalam fase pemulihan pasca-pandemi, pencapaian ini menandakan kemajuan yang luar biasa. Dengan mencapai 
            132.45% dari target kunjungan wisatawan pada tahun 2023, prestasi ini memberikan bukti konkret akan keberhasilan upaya yang 
            telah dilakukan dan ini harus dipertahankan.</p>''', unsafe_allow_html=True)
    st.warning('''
        _Untuk mencapai target selanjutnya, dapat dilakukan dengan memperkuat digitalisasi dalam sektor pariwisata. Hal ini meliputi peningkatan 
        promosi pariwisata Indonesia secara agresif di pasar internasional dan perluasan kerja sama dengan berbagai pihak terkait seperti maskapai 
        penerbangan dan agen perjalanan._''')

st.write('''<p style = "font-size:15px; text-align:justify;">
        Pada tahun 2020, dampak pandemi COVID-19 menyebabkan pembatasan interaksi masyarakat yang mengakibatkan <span style="font-weight:bold;">penurunan tajam 
        dalam jumlah kunjungan wisman hingga 74,4%,</span> tercatat hanya sebesar 3,9 juta kunjungan di tahun tersebut. Di tahun 2021, kunjungan wisman juga 
        mengalami penurunan menjadi 2.45 juta kunjungan. Penurunan ini secara langsung sangat berdampak pada pendapatan sektor pariwisata. Meskipun demikian,
        secara perlahan kunjungan wisman membaik di tahun berikutnya, hal ini artinya pembatasan interaksi masyarakat secara perlahan dilonggarkan.</p>''', unsafe_allow_html=True)
st.info('''
        _Pembatasan perjalanan, penutupan tempat wisata, dan ketidakpastian yang meluas adalah beberapa faktor utama yang menyebabkan penurunan kunjungan 
        wisman di Indonesia. Namun, seiring dimulainya relaksasi kebijakan dan pemulihan ekonomi global, terjadi peningkatan bertahap dalam jumlah kunjungan 
        wisman. **Dari sini, kita dapat melihat bahwa kunjungan wisman dan kesehatan ekonomi sektor pariwisata Indonesia saling terkait erat.**_''')

# Subeheader: Wisman pernegara
st.write('')
st.subheader('Profile Kunjungan Wisatawan Mancanegara')   
wisman_pernegara, _, wisman_pintu_masuk = st.columns([1.1, 0.1, 1.8])   
with wisman_pernegara:  
    selected_wisman_pernegara = st.selectbox('Pilih Tahun:', list(wisman_negara['tahun'].unique()), key="selected_wisman_pernegara")
    filtered_data = wisman_negara.copy()
    if selected_wisman_pernegara != 'Semua':
        filtered_data = filtered_data[filtered_data['tahun'] == selected_wisman_pernegara]

    top5_wisman_negara = filtered_data.groupby('negara')['jumlah_kunjungan_wisman'].sum().nlargest(5).reset_index()
    fig_bar_negara = px.bar(top5_wisman_negara, 
                            x='jumlah_kunjungan_wisman', 
                            y='negara', 
                            color='negara',
                            title= f'Grafik 3. Top 5 Negara dengan Asal Wisman Terbanyak',
                            labels={'jumlah_kunjungan_wisman': 'Jumlah Kunjungan Wisman', 'negara': 'Negara'})
    fig_bar_negara.update_layout(width=600, height=400)
    fig_bar_negara.update_traces(showlegend=False) 
    st.plotly_chart(fig_bar_negara, use_container_width=True)
    
with wisman_pintu_masuk:
    select_pintu_space, _ = st.columns([1.71, 0.29])
    with select_pintu_space:
        select_pintu_prov = st.selectbox('Pilih Provinsi:', ['Semua'] + list(kunjungan_wisman_perprov['provinsi'].unique()), key="select_pintu_prov")

    filtered_data = kunjungan_wisman_perprov.copy()
    if select_pintu_prov != 'Semua':
        filtered_data = filtered_data[filtered_data['provinsi'] == select_pintu_prov]

    grouped_data = filtered_data.groupby(['jenis_pintu_masuk', 'tahun']).sum().reset_index()
    color_map = {'Darat': '#10AD3D', 'Laut': '#1031AD', 'Udara': '#7532FF'}
    fig_bar_pintu = px.bar(grouped_data, 
                           x='tahun', 
                           y='jumlah_kunjungan_wisman', 
                           color='jenis_pintu_masuk',
                           color_discrete_map=color_map,
                           title='Grafik 4. Jumlah Kunjungan Wisman per Pintu Masuk',
                           barmode='group',
                           labels={'tahun': 'Tahun', 'jumlah_kunjungan_wisman': 'Jumlah Kunjungan Wisman','jenis_pintu_masuk': 'Jenis Pintu Masuk'})
    fig_bar_pintu.update_layout(width=800, height=420)
    st.plotly_chart(fig_bar_pintu, use_container_width=True)

st.markdown('''<p style="font-size:15px; text-align:justify;">
            <a href="#profile-kunjungan-wisatawan-mancanegara" style="text-decoration: none;">Grafik 3</a> diatas menggambarkan tren jumlah kunjungan 
            wisatawan per negara ke Indonesia selama beberapa tahun terakhir. Data menunjukkan bahwa <span style="font-size:15px; font-weight:bold">Malaysia 
            secara konsisten menjadi negara dengan asal wisman terbanyak</span>, mencapai puncaknya pada tahun 2019 dengan 2,9 juta pengunjung. Selain Malaysia, 
            terdapat juga kontribusi yang signifikan dari negara-negara lain seperti Australia, Timor Leste, China, Singapura, dan negara-negara Asia lainnya. 
            Selama masa pandemi tahun 2020-2021, terlihat bahwa kunjungan dari Timor Leste menjadi yang paling tinggi, meskipun secara kuantitas juga mengalami 
            penurunan. Hal ini karena adanya pembatasan perjalanan di berbagai pintu masuk.\
                 
            <p style="font-size:15px; text-align:justify;">
            <a href="#profile-kunjungan-wisatawan-mancanegara" style="text-decoration: none;">Grafik 4</a> memperlihatkan perubahan pola kunjungan wisatawan 
            ke Indonesia melalui berbagai jalur masuk, termasuk udara, darat, dan laut. Meskipun jalur udara secara historis menjadi 
            opsi utama, terjadi penurunan yang signifikan dalam kunjungan melalui jalur udara saat pandemi. Sebaliknya, jalur darat, mendominasi sebagai jalur 
            masuk utama saat pandemi, walaupun secara angka juga mengalami penurunan. Hal ini dikarenakan negara-negara yang berbatasan langsung dengan Indonesia seperti 
            Malaysia dan Timor Leste, masih tetap melakukan kunjungan ke Indonesia melalui jalur darat.</p></p>''', unsafe_allow_html=True)
st.info('''
            _Dari data tersebut, Indonesia perlu mengambil strategi untuk meningkatkan kunjungan wisman. Beberapa strategi 
            yang dapat diterapkan adalah **Border Tourism**, yaitu melalui kerjasama dengan negara-negara tetangga untuk mengembangkan destinasi 
            pariwisata di wilayah perbatasan. Ini akan memungkinkan aksesibilitas yang lebih baik ke destinasi tersebut dan merangsang 
            pertumbuhan kunjungan wisman dari negara-negara tetangga._
            
            _Selain itu, investasi dalam infrastruktur jalur udara, seperti 
            **pembangunan Low Cost Carrier Terminal (LCCT)**, dapat meningkatkan aksesibilitas dan daya tarik bagi wisatawan, terutama 
            dalam hal biaya transportasi. Strategi pemasaran juga penting, seperti **menawarkan paket wisata dengan harga diskon atau penawaran istimewa (Hot Deals)** 
            untuk event-event atau periode tertentu. Untuk memperluas daya tarik, pemerintah juga dapat **memperbanyak event seperti konser, festival budaya, dan acara 
            olahraga internasional di Indonesia** yang dapat menarik perhatian lebih banyak wisatawan mancanegara._''')

# Subheader: Wisman perprovinsi
st.write('')
st.subheader('Provinsi dengan Jumlah Kunjungan Wisman Terbanyak')
isi_wisman_most, _, wisman_most = st.columns([1.6, 0.1, 1.3])
with isi_wisman_most:
    st.write('')
    st.markdown('''<p style="font-size:15px; text-align:justify;">
                Dari <a href="#provinsi-dengan-jumlah-kunjungan-wisman-terbanyak" style="text-decoration: none;">Grafik 5</a> disamping, dapat dilihat bahwa 
                <span style="font-size:15px; font-weight:bold">Bali secara konsisten menjadi provinsi dengan jumlah kunjungan wisman terbanyak</span>, bahkan 
                melampaui provinsi-provinsi lain dengan jarak yang signifikan. Meskipun Bali juga mengalami dampak signifikan selama pandemi, dengan penurunan 
                jumlah kunjungan akibat pembatasan perjalanan, popularitasnya sebagai destinasi pariwisata terkemuka tetap tidak tergoyahkan.\
                    
                <p style="font-size:15px; text-align:justify;">
                Data kunjungan wisman di Bali menunjukkan peningkatan signifikan setiap tahunnya, dengan lebih dari 2 juta pengunjung pada 
                tahun 2022 dan melonjak menjadi lebih dari 5 juta pada tahun 2023. Namun, untuk memastikan pertumbuhan berkelanjutan 
                dan memperkuat posisi Bali sebagai destinasi unggulan, penting untuk mengimplementasikan strategi yang efektif.</p></p>''', unsafe_allow_html=True)
    
    st.info(''' 
            _**Dominasi Bali ini menunjukkan bahwa Bali tetap menjadi magnet bagi wisatawan merupakan bukti akan daya tarik yang kuat dan potensinya 
            untuk menjadi pendorong utama dalam pemulihan sektor pariwisata di Indonesia.**_
            
            _**Dengan target 7 juta kunjungan wisman di tahun 2024**, diharapkan 
            Bali dapat mencapainya dengan baik. Stretegi yang dapat dilakukan mencakup peningkatan aksesibilitas, peningkatan atraksi wisata, 
            dan promosi yang efektif._''')
    
with wisman_most:
    select_wisman_prov_most = st.selectbox('Pilih Tahun:', list(kunjungan_wisman_perprov['tahun'].unique()), key="select_wisman_prov_most")  
    filtered_data = kunjungan_wisman_perprov.copy()
    if select_wisman_prov_most != 'Semua':
        filtered_data = filtered_data[filtered_data['tahun'] == select_wisman_prov_most]
        
    top10_wisman_prov = filtered_data.groupby('provinsi')['jumlah_kunjungan_wisman'].sum().nlargest(10).reset_index() 
    wisman_bar_perprov = px.bar(top10_wisman_prov,  
                                x='jumlah_kunjungan_wisman',
                                y='provinsi',
                                title=f'Grafik 5. Top 10 Provinsi Tujuan Wisman pada Tahun {select_wisman_prov_most}',
                                color= 'provinsi',
                                labels={'jumlah_kunjungan_wisman': 'Jumlah Kunjungan Wisman', 'provinsi': 'Provinsi'})
    wisman_bar_perprov.update_layout(width=800, height=470, showlegend=False )
    st.plotly_chart(wisman_bar_perprov, use_container_width=True)

# Header: Wisnus
st.header("Tren dan Profile Kunjungan Wisatawan Nusantara")

wisnus_pertahun, _, isi_wisnus_pertahun = st.columns([1.5, 0.1, 1.4])
with wisnus_pertahun:
    wisnus_bar_pertahun = px.bar(kunjungan_wisnus_pertahun,
                                 x='tahun',
                                 y='jumlah_kunjungan_wisnus',
                                 title='Grafik 6. Jumlah Kunjungan Wisnus per Tahun',
                                 labels={'tahun': 'Tahun', 'jumlah_kunjungan_wisnus': 'Jumlah Kunjungan Wisnus'},
                                 color_discrete_sequence=['#94244B'])
    wisnus_bar_pertahun.update_layout(width=600, height=480, yaxis=dict(dtick=1e8, range=[0, 9e8]))
    st.plotly_chart(wisnus_bar_pertahun, use_container_width=True)

with isi_wisnus_pertahun:
    st.write('')
    st.write('')
    target_wisnus_2023 = 1200000000
    target_wisnus_2024 = 1250000000
    capaian_wisnus_2023 = kunjungan_wisnus_pertahun.loc[kunjungan_wisnus_pertahun['tahun'] == curr_year_wisnus, 'jumlah_kunjungan_wisnus'].values[0]
    capaian_wisnus_2024 = 'No Data'
    capaian_wisnus_2023_percent = 100 * (capaian_wisnus_2023 / target_wisnus_2023)

    target_2023_wisnus_col, target_2024_wisnus_col = st.columns(2)
    with target_2023_wisnus_col:
        st.metric('Target Minimum Kunjungan Wisnus 2023', format_big_number(target_wisnus_2023))
        capaian_wisnus_2023_text = f'<span style="font-size: 20px; font-weight: bold;">{capaian_wisnus_2023_percent:.2f}%</span>'
        capaian_wisnus_2023_color = "green" if capaian_wisnus_2023_percent > 100 else "red"
        st.write(f'Capaian: <span style="color: {capaian_wisnus_2023_color};">{capaian_wisnus_2023_text}</span>', unsafe_allow_html=True)

    with target_2024_wisnus_col:
        st.metric('Target minimum Kunjungan Wisnus 2024',format_big_number(target_wisnus_2024))
        capaian_wisnus_2024_color = "green" if capaian_wisnus_2024 != 'No Data' else "red"
        st.write(f'Capaian: <span style="color: {capaian_wisnus_2024_color};">{capaian_wisnus_2024}</span>', unsafe_allow_html=True)
    
    st.markdown('''<p style="font-size:15px; text-align:justify;">
            Pada tahun 2023, Indonesia menetapkan target kunjungan wisnus sebanyak 1.2 miliar perjalanan, namun capaiannya hanya 
            mencapai 62.43% dari target tersebut. Hal ini merupakan dampak lanjutan dari pandemi, termasuk pembatasan perjalanan, 
            ketidakmampuan daya beli masyarakat, dan ketidakstabilan ekonomi menjadi faktor utama yang mempengaruhi minat dan kemampuan 
            masyarakat untuk melakukan perjalanan. </p>''', unsafe_allow_html=True)
    st.warning('''
            _Dari sini, pentingnya kolaborasi antara lembaga pemerintahan, seperti Kemenparekraf dengan Kementerian Perhubungan (Kemenhub) 
            untuk memfasilitasi akses transportasi dan menekan harga tiket pesawat, layanan kereta api, dan transportasi lainnya._''')
        
st.markdown('''<p style="font-size:15px; text-align:justify;">
        Pada <a href= "#tren-dan-profile-kunjungan-wisatawan-nusantara" style="text-decoration: none;">Grafik 6 </a> di atas, terlihat bahwa 
        pada tahun 2020 terjadi penurunan yang signifikan dalam jumlah kunjungan wisatawan nusantara (wisnus) hingga 27,4% atau hanya menjadi 
        524 juta kunjungan. Penurunan ini tidak hanya mencerminkan dampak pandemi COVID-19 terhadap industri pariwisata, tetapi juga menimbulkan 
        keprihatinan di kalangan masyarakat karena mengganggu aktivitas ekonomi serta mengakibatkan berbagai pembatasan interaksi dan perjalanan.\
             
        <p style="font-size:15px; text-align:justify;">
        Menariknya, di tahun 2021, meskipun diperkirakan akan adanya penurunan yang berkelanjutan, <span style="font-weight:bold">jumlah perjalanan 
        wisnus justru meningkat sebesar 16.9% menjadi 613 juta perjalanan</span>, dan tren ini berlanjut hingga tahun berikutnya. Namun, peningkatan 
        ini juga membawa potensi risiko penyebaran COVID-19 yang lebih tinggi dikarenakan interaksi yang lebih sering terjadi. Hal ini terlihat dari 
        data <a href=https://infeksiemerging.kemkes.go.id/dashboard/covid-19" style="text-decoration: none;">Kementerian Kesehatan</a>
        yang mencatat peningkatan jumlah kasus konfirmasi COVID-19 tertinggi terjadi pada tahun 2021-2022. </p></p>''', unsafe_allow_html=True)
st.info('''
        _Tren ini menunjukkan bahwa pariwisata domestik telah menjadi salah satu pendorong dalam pemulihan ekonomi nasional di Indonesia. 
        Meskipun demikian, pengaruh yang paling signifikan terhadap devisa pariwisata masih ditentukan oleh jumlah kunjungan wisman. 
        Hal ini tergambar dari **[Grafik 1](#kontribusi-pariwisata-terhadap-ekonomi-indonesia)** dan **[Grafik 2](#tren-dan-profile-kunjungan-wisatawan-mancanegara)**, 
        yang menunjukkan pada tahun 2021 terjadi penurunan devisa pariwisata dan kunjungan wisman, sementara jumlah kunjungan wisnus justru mengalami peningkatan. 
        Namun, peningkatan ini tidak diiringi oleh peningkatan nilai devisa pariwisata secara signifikan. Meskipun begitu, minat masyarakat untuk menjelajahi 
        destinasi lokal memberikan harapan bagi industri pariwisata Indonesia untuk masa depan yang lebih baik._''')

# Subheader: Wisnus
st.write('')
st.subheader('Profile Kunjungan Wisatawan Nusantara')

filter_wisnus_tahun, _,filter_wisnus_provinsi = st.columns([1.2,0.1, 1.7])
with filter_wisnus_tahun:
    selected_year = st.selectbox("Pilih Tahun:", wisnus_perprov['tahun'].unique(), key="selected_year_wisnus_tahun")
with filter_wisnus_provinsi:
    selected_provinces = st.selectbox("Pilih Provinsi:", ['Semua'] + list(wisnus_perprov['provinsi'].unique()),key="selected_provinces_wisnus_tahun")

wisnus_provinsi, _, wisnus_prov_perbulan = st.columns([1.2, 0.1, 1.7])
with wisnus_provinsi:
    if selected_provinces == 'Semua':
        filtered_data = wisnus_perprov[wisnus_perprov['tahun'] == selected_year]
        top10_wisnus_prov = filtered_data.groupby('provinsi')['jumlah_kunjungan_wisnus'].sum().nlargest(10).reset_index()
    else:
        filtered_data = wisnus_perprov[(wisnus_perprov['provinsi'] == selected_provinces) & (wisnus_perprov['tahun'] == selected_year)]
        top10_wisnus_prov = filtered_data.groupby('provinsi')['jumlah_kunjungan_wisnus'].sum().reset_index()
        
    fig_bar_wisnus_prov = px.bar(top10_wisnus_prov,
                                x='jumlah_kunjungan_wisnus',
                                y='provinsi',
                                color='provinsi',
                                title='Grafik 7. Top 10 Provinsi dengan Kunjungan Wisnus Terbanyak',
                                labels={'jumlah_kunjungan_wisnus': 'Jumlah Kunjungan Wisnus',
                                        'provinsi': 'Provinsi'})
    fig_bar_wisnus_prov.update_layout(width=800, height=400, showlegend=False)
    st.plotly_chart(fig_bar_wisnus_prov, use_container_width=True)

with wisnus_prov_perbulan:
    bulan_order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    if selected_provinces == 'Semua':
        filtered_data = wisnus_perprov[wisnus_perprov['tahun'] == selected_year]
    else:
        filtered_data = wisnus_perprov[(wisnus_perprov['provinsi'] == selected_provinces) & (wisnus_perprov['tahun'] == selected_year)]
        
    filtered_data['bulan'] = pd.Categorical(filtered_data['bulan'], categories=bulan_order, ordered=True)
    grouped_data = filtered_data.groupby('bulan')['jumlah_kunjungan_wisnus'].sum().reset_index()

    fig_line_wisnus_prov = px.line(grouped_data,
                                   x='bulan',
                                   y='jumlah_kunjungan_wisnus',
                                   title= f'Grafik 8. Tren Jumlah Kunjungan Wisnus per Bulan di Tahun {selected_year}',
                                   labels={'bulan': 'Bulan', 'jumlah_kunjungan_wisnus': 'Jumlah Kunjungan Wisnus'})
    fig_line_wisnus_prov.update_layout(width=800, 
                                       height=400, 
                                       xaxis={'title': {'text': 'Bulan', 'standoff': 20}, 'tickangle': 0})
    st.plotly_chart(fig_line_wisnus_prov, use_container_width=True)
    
_, text_source_data_wisnus = st.columns([3.5,1.5])
with text_source_data_wisnus:
    st.write('''<p style="font-size:12px; text-align:right; font-style:italic; border-radius:10px;">
            Data yang digunakan dari tahun 2019 - November 2023 </p>''', unsafe_allow_html=True)
    
st.write('''<p style="font-size:15px; text-align:justify;">
        Selama lima tahun terakhir, data menunjukkan bahwa <span style="font-weight:bold;">lebih dari 70% perjalanan wisatawan nusantara 
        (wisnus) di Indonesia terjadi di Pulau Jawa</span>. Provinsi-provinsi seperti Jawa Timur, Jawa Tengah, dan Jawa Barat secara konsisten menjadi 
        tujuan favorit dengan jumlah kunjungan wisnus selalu melebihi 80 juta setiap tahunnya. Hal ini menegaskan dominasinya menjadikan pulau Jawa 
        sebagai pusat destinasi utama bagi wisatawan nusantara.\
            
        <p style="font-size:15px; text-align:justify;"> 
        Hal yang menarik untuk diamati yaitu provinsi <span style="font-weight:bold;">Bali belum pernah mencapai lima besar provinsi dengan jumlah kunjungan 
        wisnus terbanyak di Indonesia selama lima tahun terakhir.</span> Padahal popularitasnya sebagai destinasi internasional sangat tinggi. Hal 
        ini menunjukkan bahwa preferensi wisatawan nusantara cenderung berbeda dengan wisatawan mancanegara. Hal-hal seperti biaya perjalanan, 
        perbedaan ragam destinasi pariwisata, kedekatan geografis dan keterkaitan budaya dengan destinasi wisata menjadi
        faktor-faktor yang dipertimbangkan oleh wisatawan.</p></p>''', unsafe_allow_html=True)
st.info('''
        _Dengan ini, penting untuk mengadopsi pendekatan yang beragam dalam mengoptimalkan sektor pariwisata. Beberapa diantaranya
        yaitu dengan **meningkatkan aksesibilitas dan promosi destinasi di luar Pulau Jawa dan perlunya penyesuaian tingkat harga wisata 
        dan perjalanan wisnus ataupun wisman.** Selain itu, kolaborasi antar pemerintah daerah, industri pariwisata, dan sektor terkait lainnya 
        diperlukan untuk mengembangkan infrastruktur pariwisata yang memadai dan memastikan wisatawan mendapatkan pengalaman wisata yang 
        menyenangkan dan aman._''')

# Header: TPK Hotel
st.write('')
st.header('Tingkat Penghunian Kamar Hotel')
st.markdown("<p style='color: gray; font-style: italic;'>Compared to Last Year</p>", unsafe_allow_html=True)

tpk_hotel_bintang_col, tpk_hotel_nonbintang_col, jumlah_hotel_akomodasi_col, jumlah_kamar_akomodasi_col = st.columns(4)
with tpk_hotel_bintang_col:
    curr_tpk_bintang = avg_tpk_hotel.loc[avg_tpk_hotel['tahun'] == curr_year_tpk, 'persentase_tpk_hotel_bintang'].values[0]
    prev_tpk_bintang = avg_tpk_hotel.loc[avg_tpk_hotel['tahun'] == prev_year_tpk, 'persentase_tpk_hotel_bintang'].values[0]
    tpk_bintang_diff = curr_tpk_bintang - prev_tpk_bintang
    st.metric("TPK Hotel Bintang 2023", value=f'{curr_tpk_bintang:.2f}%', delta=f'{tpk_bintang_diff:.2f}%')
with tpk_hotel_nonbintang_col:
    curr_tpk_nonbintang = avg_tpk_hotel.loc[avg_tpk_hotel['tahun'] == curr_year_tpk, 'persentase_tpk_hotel_nonbintang'].values[0]
    prev_tpk_nonbintang = avg_tpk_hotel.loc[avg_tpk_hotel['tahun'] == prev_year_tpk, 'persentase_tpk_hotel_nonbintang'].values[0]
    tpk_nonbintang_diff = curr_tpk_nonbintang - prev_tpk_nonbintang
    st.metric("TPK Hotel Non Bintang 2023", value=f'{curr_tpk_nonbintang:.2f}%', delta=f'{tpk_nonbintang_diff:.2f}%')
with jumlah_hotel_akomodasi_col:
    curr_hotel_akomodasi = hotel_akomodasi_kamar_pertahun.loc[hotel_akomodasi_kamar_pertahun['tahun'] == curr_year_hotel_akomodasi_kamar, 'jumlah_hotel'].values[0]
    prev_hotel_akomodasi = hotel_akomodasi_kamar_pertahun.loc[hotel_akomodasi_kamar_pertahun['tahun'] == prev_year_hotel_akomodasi_kamar, 'jumlah_hotel'].values[0]
    hotel_akomodasi_diff = curr_hotel_akomodasi - prev_hotel_akomodasi
    curr_hotel_akomodasi = '{:,}'.format(curr_hotel_akomodasi)
    st.metric("Jumlah Hotel dan Akomodasi Lainnya 2023", value=f'{curr_hotel_akomodasi}', delta=f'{hotel_akomodasi_diff:.2f}%')
with jumlah_kamar_akomodasi_col:
    curr_hotel_kamar = hotel_akomodasi_kamar_pertahun.loc[hotel_akomodasi_kamar_pertahun['tahun'] == curr_year_hotel_akomodasi_kamar, 'jumlah_kamar'].values[0]
    prev_hotel_kamar = hotel_akomodasi_kamar_pertahun.loc[hotel_akomodasi_kamar_pertahun['tahun'] == prev_year_hotel_akomodasi_kamar, 'jumlah_kamar'].values[0]
    hotel_kamar_diff = curr_hotel_kamar - prev_hotel_kamar
    curr_hotel_kamar = '{:,}'.format(curr_hotel_kamar)
    st.metric("Jumlah Kamar dan Akomodasi Lainnya 2023", value=f'{curr_hotel_kamar}', delta=f'{hotel_kamar_diff:.2f}%')


isi_tpk_hotel_pertahun_col, _, tpk_hotel_pertahun_col = st.columns([1.3,0.05, 1.6])
with isi_tpk_hotel_pertahun_col:
    st.write('')
    st.write('')
    st.write('''<p style="font-size:15px; text-align:justify;">
            Puncak tingkat penghunian kamar hotel berbintang terjadi pada tahun 2018, didorong oleh berbagai faktor seperti event besar dan kondisi ekonomi yang 
            menguntungkan pada saat itu. <span style = "font-weight:bold;">Tingkat penghunian kamar di Hotel bintang yang tertinggi mencapai 52.2%, sedangkan hotel 
            non-bintang mencapai 32.1%.</span>\
                 
            <p style="font-size:15px; text-align:justify;">
            Namun, pandemi pada tahun 2020 menyebabkan penurunan drastis, dengan tingkat penghunian hotel bintang turun menjadi 33.3%, dan hotel non-bintang 
            turun secara signifikan menjadi 17.1%. Meskipun demikian, ada tanda-tanda pemulihan bertahap pada tahun-tahun 
            berikutnya. </p></p>''', unsafe_allow_html=True)
    st.info('''
            _Dari data tersebut, terlihat bahwa baik hotel bintang maupun non-bintang sama-sama terdampak oleh pandemi yang seiring juga dengan 
            penurunan jumlah kunjungan wisman dan wisnus. **Hal ini menandakan bahwa tantangan yang dihadapi oleh sektor pariwisata melibatkan 
            berbagai aspek, termasuk penurunan tingkat penghunian kamar sebagai hasil langsung dari kurangnya aktivitas wisatawan.**_''')
    
with tpk_hotel_pertahun_col:
    fig_line_hotel_pertahun = px.line(avg_tpk_hotel, 
                                        x='tahun', 
                                        y=['persentase_tpk_hotel_bintang', 'persentase_tpk_hotel_nonbintang'],
                                        title = 'Grafik 9. Tren Tingkat Penghunian Kamar Hotel Bintang dan Non Bintang',
                                        labels={'tahun': 'Tahun', 'value': 'Persentase TPK Hotel'},
                                        color_discrete_map={'persentase_tpk_hotel_bintang': '#1D5CF9 ', 'persentase_tpk_hotel_nonbintang': '#EE6A03'})
    fig_line_hotel_pertahun.update_layout(width=800, height=480, yaxis=dict(dtick=5, range=[0, 60]))
    st.plotly_chart(fig_line_hotel_pertahun, use_container_width=True)

# Subheader: Hotel
st.write('')
st.subheader("Menilik Lebih dalam lagi Mengenai Hotel di Indonesia")

tpk_hotel_perprov_col, _, hotel_col = st.columns([1.65, 0.1, 1.25])
with tpk_hotel_perprov_col:
    filter_hotel_tahun_col, filter_hotel_jenis_col = st.columns(2)
    with filter_hotel_tahun_col:
        select_tpk_prov_most = st.selectbox('Pilih Tahun:', list(reversed(tpk_hotel['tahun'].unique())))  
        filtered_data = tpk_hotel.copy()
        if select_tpk_prov_most != 'Semua':
            filtered_data = filtered_data[filtered_data['tahun'] == select_tpk_prov_most]
    with filter_hotel_jenis_col:
        sort_by = st.selectbox('Urutkan berdasarkan:', ['Hotel Bintang', 'Hotel Non Bintang'])
        if sort_by == 'Hotel Bintang':
            top5_tpk_prov = filtered_data.groupby('provinsi')['persentase_tpk_hotel_bintang'].mean().nlargest(5).reset_index()
        else:
            top5_tpk_prov = filtered_data.groupby('provinsi')['persentase_tpk_hotel_nonbintang'].mean().nlargest(5).reset_index()
    
    tpk_bar_perprov = px.bar(top5_tpk_prov, 
                            x='provinsi', 
                            y=top5_tpk_prov.columns[1],
                            title=f'Grafik 10. Top 5 Provinsi dengan TPK {sort_by} Tertinggi pada Tahun {select_tpk_prov_most}',
                            labels={'persentase_tpk_hotel_bintang': 'Persentase TPK Hotel', 'persentase_tpk_hotel_nonbintang': 'Persentase TPK Hotel', 'provinsi': 'Provinsi'},
                            color='provinsi')
    tpk_bar_perprov.update_layout(width=800, height=460, yaxis=dict(dtick=4, range=[20, 80]))
    st.plotly_chart(tpk_bar_perprov, use_container_width=True)
    
with hotel_col:
    selected_year_hotel = st.selectbox('Pilih Tahun:', list(reversed(hotel_akomodasi_kamar['tahun'].unique())))
    filtered_data = hotel_akomodasi_kamar.copy()
    if selected_year_hotel:
        filtered_data = filtered_data[filtered_data['tahun'] == selected_year_hotel]

    top5_data_hotel = filtered_data.groupby('provinsi').sum().nlargest(5, columns='jumlah_hotel').reset_index()
    top5_data_hotel = top5_data_hotel.sort_values(by='jumlah_hotel', ascending=False)
    fig_bar_hotel = px.bar(top5_data_hotel, 
                x='jumlah_hotel',
                y='provinsi',
                color='provinsi',
                title='Grafik 11. Top 5 Jumlah Hotel dan Akomodasi Terbanyak per Provinsi',
                labels={'jumlah_hotel': 'Jumlah Hotel dan Akomodasi Lainnya', 'provinsi': 'Provinsi'})
    fig_bar_hotel.update_layout(width=800, height=460)
    st.plotly_chart(fig_bar_hotel, use_container_width=True)
            
st.write('''<p style="font-size:15px; text-align:justify;">
        <span style="font-weight:bold;">Sejak tahun 2020, tingkat penghunian kamar di Hotel Bintang di Kalimantan Timur cenderung lebih tinggi 
        dibandingkan dengan wilayah lainnya.</span> Hal ini kemungkinan dipengaruhi oleh lonjakan kunjungan di daerah tersebut, terutama dengan 
        adanya proyek Ibu Kota Nusantara (IKN) yang menarik minat wisatawan untuk menginap di hotel-hotel Kalimantan Timur. Sementara 
        itu, DKI Jakarta tetap menjadi yang tertinggi untuk hotel non-bintang, menunjukkan dominasi bisnis perhotelan di ibu kota yang 
        stabil.\

        <p style="font-size:15px; text-align:justify;">
        Menariknya, <span style="font-weight:bold;">DKI Jakarta mencatat tingkat penghunian kamar tertinggi pada tahun 2018, mencapai 
        66.87%, yang merupakan angka tertinggi dalam delapan tahun terakhir.</span> Salah satu faktor pengaruhnya adalah adanya event besar seperti 
        Asian Games dan event-event lain yang mendorong tingkat hunian hotel di provinsi tersebut. Fenomena serupa juga terjadi di Provinsi 
        Sumatera Selatan, yang mendongkrak angka hunian kamar hotel menjadi 59.3%.\
        
        <p style="font-size:15px; text-align:justify;"> 
        <span style="font-weight:bold;">Bali menempati posisi terbanyak dalam hal jumlah hotel dan akomodasi lainnya di Indonesia.</span> Meskipun demikian, 
        penurunan juga tetap terjadi di tahun 2021 yang mencerminkan dampak pandemi terhadap jumlah hotel dan akomodasi yang tersedia. Di sisi lain, 
        provinsi-provinsi di Pulau Jawa secara konsisten berada di lima besar. Hal ini menyoroti adanya hubungan yang erat antara infrastruktur akomodasi 
        dengan jumlah kunjungan wisatawan, karena ketersediaan akomodasi yang memadai sangat penting bagi para wisatawan. </p></p></p>''', unsafe_allow_html=True)
st.info('''
        _Untuk memperkuat sektor pariwisata di seluruh Indonesia, **perlu adanya investasi lebih lanjut dalam pembangunan infrastruktur hotel 
        dan akomodasi lainnya di luar Pulau Jawa dan Bali.** Hal ini akan membantu meningkatkan ketersediaan fasilitas penginapan yang memadai
        bagi wisatawan di berbagai destinasi, sehingga mendukung pertumbuhan sektor pariwisata secara keseluruhan._''')
          
# Header: Perbandingan wisatawan asing di negara ASEAN  
st.write('')
st.write('')
st.header("Perbandingan Wisatawan Asing di Negara ASEAN")
asean_wisatawan = asean_wisatawan.sort_values(by='year', ascending=False)
isi_asean_data_col, _, asean_data_col = st.columns([1.3, 0.2, 1.6])
with asean_data_col:
    selected_year_asean = st.selectbox('Pilih Tahun:', asean_wisatawan['year'].unique(), key="selected_year_asean")
    filtered_data_asean = asean_wisatawan[asean_wisatawan['year'] == selected_year_asean]
    filtered_data_asean = filtered_data_asean.sort_values(by='visitors_arrival_in_person', ascending=False)
    
    fig_bar_asean_compared = px.bar(filtered_data_asean,
                                    y='country',
                                    x='visitors_arrival_in_person',
                                    color='country',
                                    title=f'Grafik 12. Jumlah kunjungan Wisatawan di Berbagai Negara ASEAN tahun {selected_year_asean}',
                                    labels={'value': 'Negara', 'year': 'Tahun', 'variable': 'Negara', 'visitors_arrival_in_person': 'Jumlah Kunjungan per Orang'})
    fig_bar_asean_compared.update_layout(width=800, 
                                         height=400, 
                                         xaxis={'title': {'text': 'Negara', 'standoff': 20}, 'tickangle': 0})
    st.plotly_chart(fig_bar_asean_compared, use_container_width=True)
with isi_asean_data_col:
    st.write('')
    st.write('''<p style="font-size:15px; text-align:justify;">
            Meskipun Indonesia memiliki pesona alam yang memukau, namun sektor pariwisata masih menghadapi tantangan dalam menarik 
            perhatian wisatawan asing. Data disamping menunjukkan bahwa <span style="font-weight:bold;">Thailand secara konsisten menjadi negara yang 
            paling banyak dikunjungi oleh wisatawan asing, dengan jumlah kunjungan yang mencapai puncaknya sebesar 39.9 juta per orang pada tahun 2019.</span>\
                 
            <p style="font-size:15px; text-align:justify;">
            Sementara itu, Indonesia masih berada jauh di bawah Thailand, Malaysia, dan Singapura, dengan jumlah kunjungan wisatawan asing 
            yang paling tinggi hanya 16.1 juta per orang pada tahun 2018. <span style ="font-weight:bold;">Hal ini menandakan bahwa daya tarik pariwisata Indonesia masih
            kurang di dunia internasional dibandingkan dengan negara-negara ASEAN lainnya.</span></p></p>''', unsafe_allow_html=True)
    
    st.info('''
            _Salah satu faktor yang menyebabkan Indonesia belum mampu menarik perhatian wisatawan asing secara maksimal adalah 
            kurangnya promosi destinasi-destinasi wisata potential Indonesia dan kurangnya konektivitas antar destinasi di Indonesia._''')
    
# Header: Potensi Pariwisata 
st.header('Potensi Pariwisata Indonesia')

# preparing for potensi pariwisata
beach_emo = '🏖️'
boat_emo = '🚤'
mountain_emo = '⛰️'
lake_emo = '🏞️'
island_emo = '🏝️'

metric_title1 = f'{beach_emo} Total Daya Tarik Wisata'
metric_title2 = f'{boat_emo} Total DPSP'
metric_title3 = f'{mountain_emo} Total DPN'
metric_title4 = f'{lake_emo} Total KPPN'
metric_title5 = f'{island_emo} Total KSPN'

total_dtw = jenis_dtw_pariwisata['jumlah_dtw'].sum()
total_dpsp = jenis_dtw_pariwisata['jumlah_dpsp'].sum()
total_dpn = jenis_dtw_pariwisata['jumlah_dpn'].sum()
total_kppn = jenis_dtw_pariwisata['jumlah_kppn'].sum()
total_kspn = jenis_dtw_pariwisata['jumlah_kspn'].sum()

# Kolom
total_dtw_col, total_dpsp_col, total_dpn_col, total_kppn_col, total_kspn_col = st.columns(5)

# Menampilkan metrik dengan emotikon
with total_dtw_col:
    st.metric(metric_title1, '{:,}'.format(total_dtw))
with total_dpsp_col:
    st.metric(metric_title2, '{:,}'.format(total_dpsp))
with total_dpn_col:
    st.metric(metric_title3, '{:,}'.format(total_dpn))
with total_kppn_col:
    st.metric(metric_title4, '{:,}'.format(total_kppn))
with total_kspn_col:
    st.metric(metric_title5, '{:,}'.format(total_kspn))

# making map folium
map = folium.Map(location=[-1, 118], zoom_start=5, scrollWheelZoom=False, tiles='CartoDB positron')

choropleth = folium.Choropleth(
    geo_data=geo_data,
    data=jenis_dtw_pariwisata,  
    columns=['provinsi', 'jumlah_dtw'],  
    key_on='feature.properties.Propinsi', 
    fill_color = 'Greens',
    line_opacity=1,
    hightlight=True,
    legend_name='Daya Tarik Wisata'
)
choropleth.add_to(map)

df = jenis_dtw_pariwisata['provinsi']

for feature in choropleth.geojson.data['features']:
    nama_provinsi = feature['properties']['Propinsi']
    jumlah_dtw = jenis_dtw_pariwisata.loc[jenis_dtw_pariwisata['provinsi'] == nama_provinsi, 'jumlah_dtw'].values
    jumlah_dpsp = jenis_dtw_pariwisata.loc[jenis_dtw_pariwisata['provinsi'] == nama_provinsi, 'jumlah_dpsp'].values
    jumlah_dpn = jenis_dtw_pariwisata.loc[jenis_dtw_pariwisata['provinsi'] == nama_provinsi, 'jumlah_dpn'].values
    jumlah_kppn = jenis_dtw_pariwisata.loc[jenis_dtw_pariwisata['provinsi'] == nama_provinsi, 'jumlah_kppn'].values
    jumlah_kspn = jenis_dtw_pariwisata.loc[jenis_dtw_pariwisata['provinsi'] == nama_provinsi, 'jumlah_kspn'].values
    feature['properties']['jumlah_dtw'] = f'Daya Tarik Wisata: {jumlah_dtw[0]:,.0f}' if len(jumlah_dtw) > 0 else 'N/A'
    feature['properties']['jumlah_dpsp'] = f'DPSP: {jumlah_dpsp[0]:,.0f}' if len(jumlah_dpsp) > 0 else 'N/A'
    feature['properties']['jumlah_dpn'] = f'DPN: {jumlah_dpn[0]:,.0f}' if len(jumlah_dpn) > 0 else 'N/A'
    feature['properties']['jumlah_kppn'] = f'KPPN: {jumlah_kppn[0]:,.0f}' if len(jumlah_kppn) > 0 else 'N/A'
    feature['properties']['jumlah_kspn'] = f'KSPN: {jumlah_kspn[0]:,.0f}' if len(jumlah_kspn) > 0 else 'N/A'
    
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['Propinsi', 'jumlah_dtw', 'jumlah_dpsp', 'jumlah_dpn', 'jumlah_kppn', 'jumlah_kspn'], labels=False)
)
# title map
st.write('')
st.write('<h4 style="text-align: center;">Peta Sebaran Jenis dan Objek Daya Tarik Wisata Indonesia</h4>', unsafe_allow_html=True)
# show the map
st_map = st_folium(map, width=700, height=480, use_container_width=True)

st.write('''<p style="font-size:15px; text-align:justify;">
        Indonesia, sebagai negara kepulauan yang kaya akan keindahan alam dan keanekaragaman budaya, memiliki banyak potensi pariwisata 
        yang bisa dinikmati oleh wisatawan lokal maupun mancanegara. Saat ini Indonesia memiliki 8494 objek daya tarik wisata 
        (DTW) yang tersebar di seluruh wilayah Indonesia. <span style ="font-weight:bold;">Dalam upaya untuk mengembangkan potensi pariwisata tersebut, 
        pemerintah telah menetapkan sejumlah wilayah yang menjadi fokus pembangunan, seperti Destinasi Pariwisata Super Prioritas (DPSP), Destinasi Pariwisata 
        Nasional (DPN), Kawasan Pengembangan Pariwisata Nasional (KPPN), dan Kawasan Strategis Pariwisata Nasional (KSPN).</span>\
             
        <p style="font-size:15px; text-align:justify;">
        Saat ini, hanya terdapat 5 DPSP di Indonesia, yaitu Borobudur di Jawa Tengah, Mandalika di Nusa Tenggara Barat, Likupang di Sulawesi 
        Utara, Danau Toba di Sumatera Utara, dan Labuan Bajo di Nusa Tenggara Timur. Provinsi Jawa Tengah menjadi provinsi dengan jumlah objek daya tarik wisata
        terbanyak mencapai 968, diikuti oleh Jawa Timur dengan 845 objek daya tarik wisata. <span style ="font-weight:bold;">Hal ini menunjukkan bahwa pulau Jawa 
        memang sepantasnya menjadi pusat utama dari berbagai daya tarik wisata di Indonesia. Apabila hal ini dapat dimanfaatkan dengan baik, potensi ini dapat menarik lebih banyak lagi
        wisatawan khususnya Wisatawan Mancanegara. </span>''', unsafe_allow_html=True)
st.info('''
        _Untuk mendukung pertumbuhan pariwisata yang berkelanjutan, diperlukan infrastruktur pendukung yang memadai, seperti akomodasi, transportasi, dan sarana 
        penunjang lainnya. Ini bukan hanya di wilayah Pulau Jawa, tetapi juga untuk daerah-daerah lain yang memiliki potensi pariwisata yang besar. 
        Dengan meningkatkan infrastruktur ini, pengalaman wisatawan yang berkunjung ke berbagai destinasi di seluruh Indonesia dapat ditingkatkan._
        
        _Selain itu, penting juga untuk mengembangkan SDM pariwisata yang berkualitas dan meningkatan digitalisasi serta promosi pariwisata yang agresif, 
        agar potensi pariwisata di Indonesia dapat dioptimalkan sepenuhnya. Dengan memanfaatkan potensi ini secara maksimal, sektor pariwisata dapat 
        memberikan kontribusi yang lebih besar terhadap perekonomian nasional._''')

st.write('')
st.write('')
with st.expander('REFERENSI'):
    st.write('[1] [Satu Data, Kemenparekraf](https://satudata.kemenparekraf.go.id/)')
    st.write('[2] [Publikasi Statistik, Statistik Pariwisata, Kemenparekraf](https://kemenparekraf.go.id/)')
    st.write('[3] [Pariwisata, BPS Indonesia](https://www.bps.go.id/id/statistics-table?subject=561)')
    st.write('[4] [Statistik Hotel dan Akomodasi Lainnya di Indonesia, BPS Indonesia](https://www.bps.go.id/id/publication/2023/12/29/d9c277bd3ad62674f53e454a/statistik-hotel-dan-akomodasi-lainnya-di-indonesia-2023.html)')
    st.write('[5] [Visitor Arrival Statistics, ASEANStats](https://data.aseanstats.org/)')
    
