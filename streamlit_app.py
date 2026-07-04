# --- ส่วนที่เอาไปวางแทนตารางเก่า ---
st.subheader("📋 กระดานสถานะงานซ่อม")

if 'job_status' not in st.session_state:
    st.session_state.job_status = pd.DataFrame({
        "เลขที่ใบงาน": ["23739"],
        "สถานะงาน": ["รับรถ"],
        "แผนก": ["แผนกช่างเครื่องยนต์"],
        "รายการอะไหล่": ["น้ำมันเกียร์"]
    })

edited_df = st.data_editor(
    st.session_state.job_status,
    column_config={
        "สถานะงาน": st.column_config.SelectboxColumn(
            "สถานะงาน",
            options=["รับรถ", "แผนกเครื่องยนต์", "ช่วงล่าง", "สีและตัวถัง", "ไฟฟ้าและแอร์", "รอส่งมอบ"],
            required=True,
        )
    },
    hide_index=True,
)

if st.button("💾 อัปเดตสถานะงานทั้งหมด"):
    st.session_state.job_status = edited_df
    st.success("อัปเดตสถานะงานเรียบร้อยครับ!")
# -----------------------------------
import streamlit as st
import pandas as pd
