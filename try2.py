
#             # Eklendi mesajı
#             # ============================================================================================

#             st.success(f"{eklenen_soru_sayisi} soru eklendi.")

#             # Formu temizle
#             st.session_state.YS_ana_kategori = ""
#             st.session_state.YS_soru_metni = []
#             st.session_state.YS_resim_yolu = ""
#             st.session_state.YS_notlar = ""
#             st.session_state.YS_Etiketler = []

# # ============================================================================================
# # TAB 4: MEVCUT SORULARI GORUNTULE VE DUZENLE
# # ============================================================================================ 
# with tab4:
    
#         # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
#     # ============================================================================================
#     st.session_state.setdefault("MS_secilen_ana_kategori", None)
#     st.session_state.setdefault("MS_secilen_alt_kategori", None)    
#     st.session_state.setdefault("MS_soru_metni", None)    
#     st.session_state.setdefault("MS_resim_yolu", None)    
#     st.session_state.setdefault("MS_notlar", None)
#     st.session_state.setdefault("MS_Etiketler", None)

#     st.session_state.setdefault("MS_son_ana_kategori", "0")
#     st.session_state.setdefault("MS_son_alt_kategori", "0")
#     st.session_state.setdefault("MS_sorular_gosterilsin", False)

#     # Kategori seçim alanları için kolon düzeni
#     # ============================================================================================
#     col1, col2 , col3 = st.columns([1, 1, 1])

#     # Ana kategori seçimi
#     with col1:
#         with st.container(border=True, vertical_alignment="center", height="stretch"):
#             st.session_state.MS_secilen_ana_kategori = st.radio(
#                 "Ana Kategori",
#                 ["All"] + dla_ana_kategori_listesi(),
#                 key="MSK_ana_kategori_radio",
#             )

#     # Alt kategori seçimi
#     with col2:
#         with st.container(border=True, vertical_alignment="center", height="stretch"):
                
#             if st.session_state.MS_secilen_ana_kategori == "All":
            
#                 st.session_state.MS_secilen_alt_kategori = st.selectbox(
#                 "Alt Kategori",
#                 ["All"],
#                 key="MSK_alt_kategori_selectbox"
#                 )
            
#             else:
                
#                 #alt_kategoriler1 = dla_alt_kategorileri_getir(st.session_state.MS_secilen_ana_kategori)

#                 st.session_state.MS_secilen_alt_kategori = st.selectbox(
#                 "Alt Kategori",
#                 ["All"],# + alt_kategoriler1,
#                 key="MSK_alt_kategori_selectbox"
#                 )
    
#     #Son ana kategori ve alt kategori değerlerini kontrol et, değişiklik varsa soruları gösterme durumunu kapat  
#     # ============================================================================================
     
#     if (
#         st.session_state.MS_son_ana_kategori != st.session_state.MS_secilen_ana_kategori
#         or st.session_state.MS_son_alt_kategori != st.session_state.MS_secilen_alt_kategori
#         ):
#             st.session_state.MS_sorular_gosterilsin = False
#             st.session_state.MS_son_ana_kategori = st.session_state.MS_secilen_ana_kategori
#             st.session_state.MS_son_alt_kategori = st.session_state.MS_secilen_alt_kategori

#     #============================================================================================

#     # Butona basılınca seçimi kaydet
#     with col3:
#         with st.container(border=True, vertical_alignment="center", height="stretch"):
#             sorugetir = st.button("Soruları Getir", key="MSK_soru_getir_btn")
    


#     if sorugetir:
#         st.session_state.MS_sorular_gosterilsin = True

#     if st.session_state.MS_sorular_gosterilsin:

#         st.write(f"Kontrol Edilen Ana Kategori: {st.session_state.MS_secilen_ana_kategori}")
#         st.write(f"Kontrol Edilen Alt Kategori: {st.session_state.MS_secilen_alt_kategori}")

#         # form_alani = st.container()

#         # # VERİ ÇEK
#         # # ===============================
    
#         # rows = dla_sorulari_getir(ana_kategori=st.session_state.MS_secilen_ana_kategori, alt_kategori=st.session_state.MS_secilen_alt_kategori)
#         # df = pd.DataFrame(rows.data)


#         # #Eğer veri boş değilse tabloyu göster
#         # #============================================================================================

#         # if not df.empty:

#         #     st.divider()
         
#         #     #Gosterilecek kolonları belirle
#         #     #============================================================================================
#         #     if st.session_state.MS_secilen_ana_kategori == "All":
#         #         gosterilecek_kolonlar = ["id", "AnaKategori", "AltKategori", "Soru", "Notlar", "ResimURL"]

#         #     if st.session_state.MS_secilen_ana_kategori == "General":
#         #         gosterilecek_kolonlar = ["id", "Soru"]

#         #     if st.session_state.MS_secilen_ana_kategori == "Scenario":
#         #         gosterilecek_kolonlar = ["id", "Soru"]

#         #     if st.session_state.MS_secilen_ana_kategori == "PictureDescription":
#         #         gosterilecek_kolonlar = ["id", "ResimURL"]


#         #     event = st.dataframe(
#         #         df[gosterilecek_kolonlar],
#         #         use_container_width=True,
#         #         hide_index=True,
#         #         on_select="rerun",
#         #         selection_mode="single-row",
#         #         column_config={
#         #             "id": st.column_config.NumberColumn("ID", width=20),
#         #             }
#         #         )
            
#         #     if event.selection.rows:
#         #         secili_index = event.selection.rows[0]
#         #         secili_satir = df.iloc[secili_index]
#         #         secili_id = secili_satir["id"]


#         #     #ID İLE VERİLERİ ÇEK
#         #     #============================================================================================
#         #     satir = df[df["id"] == secili_id].iloc[0]

            
                
#         #         #ıf ile session_state kontrolü yaparak sadece id değiştiğinde formu doldur
#         #         if "Son_Id" not in st.session_state:
#         #             st.session_state.Son_Id = secili_id

#         #         if st.session_state.Son_Id != secili_id:
#         #             st.session_state.Son_Id = secili_id
                
#         #         if "Son_Ana_Kategori" not in st.session_state:
#         #             st.session_state.Son_Ana_Kategori = satir["AnaKategori"]
#         #         if st.session_state.Son_Ana_Kategori != satir["AnaKategori"]:
#         #             st.session_state.Son_Ana_Kategori = satir["AnaKategori"]
                
#         #         if "Son_Alt_Kategori" not in st.session_state:
#         #             st.session_state.Son_Alt_Kategori = satir["AltKategori"]
                
#         #         if st.session_state.Son_Alt_Kategori != satir["AltKategori"]:
#         #             st.session_state.Son_Alt_Kategori = satir["AltKategori"]
                
#         #         if "Son_Soru" not in st.session_state:
#         #             st.session_state.Son_Soru = satir["Soru"]
                
#         #         if st.session_state.Son_Soru != satir["Soru"]:
#         #             st.session_state.Son_Soru = satir["Soru"]
                
#         #         if "Son_Notlar" not in st.session_state:
#         #             st.session_state.Son_Notlar = satir["Notlar"]
                
#         #         if st.session_state.Son_Notlar != satir["Notlar"]:
#         #             st.session_state.Son_Notlar = satir["Notlar"]
                
#         #         if "Son_ResimURL" not in st.session_state:
#         #             st.session_state.Son_ResimURL = satir["ResimURL"]
                
#         #         if st.session_state.Son_ResimURL != satir["ResimURL"]:
#         #             st.session_state.Son_ResimURL = satir["ResimURL"]
                

#         #         # ===============================
#         #         # ÜST FORMU BURADA DOLDUR
#         #         # Ama ekranda yukarıda görünür
#         #         # ===============================

#         #         with form_alani:

#         #             st.subheader("Seçili Soruyu Düzenle")

#         #             col1, col2, col3, col4 = st.columns([1, 2, 2, 2])

#         #             with col1:
#         #                 t_id = st.text_input(
#         #                     "ID",
#         #                     key="MSK_edit_id",
#         #                     disabled=True,
#         #                     value=st.session_state.Son_Id
#         #                 )

#         #             with col2:
#         #                 t_ana_kategori = st.text_input(
#         #                     "Ana Kategori",
#         #                     value=st.session_state.Son_Ana_Kategori,
#         #                     key="MSK_edit_ana_kategori"
#         #                 )

#         #             with col3:
#         #                 t_alt_kategori = st.text_input(
#         #                     "Alt Kategori",
#         #                     value=st.session_state.Son_Alt_Kategori,
#         #                     key="MSK_edit_alt_kategori"
#         #                 )

#         #             with col4:
#         #                 t_pic = st.text_input(
#         #                     "Resim URL",
#         #                     value=st.session_state.Son_ResimURL,
#         #                     key="MSK_edit_pic"
#         #                 )

#         #             t_soru = st.text_area(
#         #                 "Soru",
#         #                 value=st.session_state.Son_Soru,
#         #                 key="MSK_edit_soru",
#         #                 height=120
#         #             )

#         #             t_not = st.text_area(
#         #                 "Notlar",
#         #                 value=st.session_state.Son_Notlar,
#         #                 key="MSK_edit_not",
#         #                 height=100
#         #             )
