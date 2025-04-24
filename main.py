import os
import streamlit as st
from dotenv import load_dotenv
from app.ui import render_ui
from app.controller import process_use_case

load_dotenv()

def main():
    st.set_page_config(page_title="RAG Resume Analyzer", layout="wide")
    st.title("📄 AI Resume Analyzer with Groq")
    
    use_case, inputs = render_ui()
    if use_case and inputs:
        with st.spinner("Processing..."):
            results = process_use_case(use_case, inputs)
            st.subheader("Results")
            st.write(results)

if __name__ == "__main__":
    main()


    # tambah use case untuk tanya jawab resume
    # modifikasi up resume per use case, buat saat tiap pindah use case, resume yg sudah di up di use case tersebut tidak lsg hilang kecuali user uncheck/hapus sehingga waktu balik use case tersebut masih ada file yg di uploud sebelumnya di use case tersebut
    # modfikasi di use case compare_candidates bisa up satu folder yg berisi banyak resume(saat ini baru multiple pdf), dan di dalam folder tersebut berisis resume atau bisa ada subfolder, dan semua resume di dalam folder dan/atau subfolder tersebut bisa di upload sekaligus
    # tambah use case menjukan score dan ranking kandidat berdasar resume dan analisis, jadi buat ada penilaiiannya gitu, untuk penilaiannya bisa berdasar seting klasifikasi teks, misal ada 5 klasifikasi, dan setiap resume di klasifikasikan ke dalam 5 klasifikasi tersebut, dan setiap klasifikasi ada bobotnya, misal bobot 1-10, dan setiap resume di beri score dari 1-10 untuk setiap klasifikasi tersebut, dan di akhir di ranking berdasarkan score total dari semua klasifikasi tersebut atau bisa di buat berdasasr similarity kriteria yang diinginkan, misal ada 5 kriteria, dan setiap resume di klasifikasikan ke dalam 5 kriteria tersebut, dan setiap kriteria ada bobotnya, misal bobot 1-10, dan setiap resume di beri score dari 1-10 untuk setiap kriteria tersebut, dan di akhir di ranking berdasarkan score total dari semua kriteria tersebut
    # tambah use case untuk klasifikasi dan klustering resume (belum kepikiran label klasifikasi dan fitur yg membedakan dan mendukung klasifikasi dan jlastering)
    # tambah untuk visualisasi hasil analisis resume
    # tambah untuk eksport hasil analisis use case compare, rangking, klasifikasi, dan clustering dan compare resume ke format lain (misal CSV, JSON)
    # referensi (https://github.com/tatashandharu15/CV-Analytics-LLM--using-OpenAI)