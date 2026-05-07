# KUTUPHANELER
import streamlit as st
import pandas as pd
from io import BytesIO

# UTILS import
from UTILS.text_utils import slow_print
from UTILS.text_utils import trim_text
from UTILS.time_utils import wait
from UTILS.text_utils import tr_to_en_lower

import UTILS.session_utils as SsnFonk
import supabaseFonksiyon as SpFonk


# DLA ANA KATEGORİLERİ LİSTESİ
#============================================================================================
def dla_ana_kategori_listesi():
    return [
        "General",
        "Scenario",
        "PictureDescription"
    ] 



# SESSION STATE OLUŞTUR
#============================================================================================
ssElamanlar = {
        "VT_Etiketler_df": pd.DataFrame,
        "VT_Sorular_df": pd.DataFrame,
        "VT_ana_kategoriler_list": list
    }

def session_olustur_yardimci(): SsnFonk.session_olustur(ssElamanlar)



# YENİ ETİKET EKLEME ALANINI DOLDUR
#============================================================================================
def Yeni_Etiket_Alan_Doldur(alan):
        
    
    with alan:
              
        #ETİKETLERİ GETIR
        vt_etiketler: pd.DataFrame = st.session_state.YE_YeniEtiketler_list
        
        #EĞER KAYIT YOKSA BILGI VER
        if vt_etiketler.empty:
            st.info("Herhangi bir etiket bulunamadı.")           
            st.stop()
        
        
        
        #EĞER KAYIT VARSA DEVAM ET
        st.write(len(vt_etiketler), "tane etiket bulundu.")
        
        # Kolonları olustur
        # ============================================================================================
        col1,col2 = st.columns([1,1])
        
        with col1:
                
                # COL1 CONTAINER OLUSTUR
                # ============================================================================================
                with st.container(border=True,vertical_alignment="center",height="stretch"):    
                    
                    # Arama alanı
                    # ============================================================================================
                    search_text = st.text_input("🔍 Etiket Ara", placeholder="Etiket gir...")
                    search_text = tr_to_en_lower(search_text.strip())
                    
                    filtered_df = vt_etiketler.copy()

                    if search_text:
                        filtered_df = filtered_df[
                            filtered_df["Etiket"].str.contains(search_text, case=False, na=False)
                        ]
        
                    # ETİKET ALANI
                    # ============================================================================================

                    # Seçim kolonu ekle
                    if "sec" not in vt_etiketler.columns:
                        filtered_df.insert(0, "sec", False)


                    edited_df = st.data_editor(
                        filtered_df,
                        use_container_width=False,
                        hide_index=True,
                        row_height=42,
                        height=300,
                        
                        column_config={
                            
                            "sec": st.column_config.CheckboxColumn("SEC", width=100),
                            "id": None,  # 👈 BU SATIR KOLONU GİZLER
                            "Etiket": st.column_config.TextColumn("ETİKET", width=1000),
                            
                        },
                        
                        key="MEK_etiket_editor"
                    )
                    
                    # Excel olarak indirme butonu
                    #============================================================================================

                    export_df = edited_df.drop(columns=["Sec"], errors="ignore")
                    
                    excel_buffer = BytesIO()

                    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
                        export_df.to_excel(writer, index=False, sheet_name="DlaKategoriler")

                    st.download_button(
                        label="📥 Excel Olarak İndir",
                        data=excel_buffer.getvalue(),
                        file_name="DlaEtiketler.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )

        with col2:
            
            #seçili satırları al
            secili_satirlar = edited_df[edited_df["sec"] == True] 
            
            updated_tag = ""
            
            # COL2 CONTAINER OLUSTUR
            # ============================================================================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
        
                    # SINAMA 1
                # ============================================================================================
                if len(secili_satirlar) > 1:
                    st.warning("Lütfen sadece bir satır seç.", icon="⚠️")
                
                # SINAMA 2
                # ============================================================================================    
                elif len(secili_satirlar) < 1:
                    st.info("İşlem yapmak için tablodan bir satır seç.", icon="ℹ️")
                
                # İŞLEM
                # ============================================================================================
                else:
                    
                    # Tanımalamaları yap
                    #============================================================================================
                    selected_row = secili_satirlar.iloc[0]
                    selected_id = int(selected_row["id"])
                    selected_tag = tr_to_en_lower(selected_row["Etiket"])

                    #Seçilen ID ve Etiketi yazdır
                    st.info(f"Seçili ID: {selected_id}", icon="ℹ️")
                    
                    updated_tag = st.text_input(
                        "Seçili Etiket",
                        value=selected_tag,
                        disabled=False,
                        width="stretch"
                    )
                    
                    #  GUNCELLE BUTONU
                    if st.button("💾 Seçili Etiketi Güncelle", use_container_width=True):
                        SpFonk.dla_etiket_guncelle(
                            selected_id,
                            tr_to_en_lower(updated_tag),
                        )
                        
                        st.success("Etiket güncellendi.", icon="✅")
                        
                        # RESET
                        SsnFonk.session_resetle("ME_", ssElamanlar)
                        
                        