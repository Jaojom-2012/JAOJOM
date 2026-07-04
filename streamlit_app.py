import streamlit as st
import pandas as pd

st.title("🏎️ ระบบจัดการใบงานแจ้งซ่อม - แสงอรุณ ออโต้ เซอร์วิส")
st.subheader("จัดการข้อมูลและรูปภาพหน้างานแบบจบในหน้าเดียว ไม่ต้องพึ่งสูตร")

st.write("### 📝 เปิดใบงานใหม่")
col1, col2 = st.columns(2)

with col1:
    job_id = st.text_input("เลขที่ใบงาน (Job ID)", placeholder="เช่น 23739")
    department = st.selectbox("แผนกที่แจ้ง", ["แผนกช่างเครื่องยนต์", "แผนกช่วงล่าง", "แผนกสีและตัวถัง", "แผนกไฟฟ้าและแอร์"])

with col2:
    part_list = st.text_area("รายการอะไหล่ที่ต้องใช้เพิ่ม", placeholder="เช่น น้ำมันเกียร์, กรองเครื่อง")
    uploaded_file = st.file_uploader("📸 อัปโหลดรูปถ่ายหน้างาน / ใบงานซ่อม", type=["jpg", "jpeg", "png"])

if st.button("💾 บันทึกข้อมูลเข้าสู่ระบบ"):
    st.success(f"บันทึกใบงานเลขที่ {job_id} เรียบร้อยแล้ว!")

st.markdown("---")

st.write("### 📊 ตารางติดตามงานปัจจุบัน")
data = {
    "เลขที่ใบงาน": ["23739"],
    "แผนกที่แจ้ง": ["แผนกช่างเครื่องยนต์ น้ำมันเกียร์"],
    "รายการอะไหล่": ["ขวดน้ำมันเกียร์ตามรูปไฮไลท์"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.write("🖼️ **รูปถ่ายหน้างานของใบงานนี้:**")
if uploaded_file is not None:
    st.image(uploaded_file, caption=f"ใบงานเลขที่ {job_id}", width=500)
else:
    st.image("https://images.unsplash.com/photo-1486006920555-c77dce18193b?w=500", caption="ตัวอย่างรูปใบงานซ่อมในอู่", width=500)
