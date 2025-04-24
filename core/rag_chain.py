import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from core.embedding import get_embedding_model
from core.retriever import get_retriever
from core.comparator import compare_resumes
from typing import List

load_dotenv()  # Load environment variables

llm = ChatGroq(
    temperature=0,
    model_name="deepseek-r1-distill-llama-70b",
    api_key=os.getenv("GROQ_API_KEY")  
)

def candidate_search(jd_text: str) -> str:
    """Search candidates based on job description"""
    retriever = get_retriever()
    relevant_resumes = retriever.invoke(jd_text)
    
    prompt = ChatPromptTemplate.from_template(
        """Berdasarkan deskripsi pekerjaan berikut:
        {jd_text}
        
        Dan kandidat yang relevan:
        {resumes}
        
        Berikan analisis tentang bagaimana kandidat memenuhi persyaratan pekerjaan.
        Berikan juga rekomendasi kandidat terbaik beserta alasannya.
        """
    )
    
    chain = prompt | llm
    return chain.invoke({
        "jd_text": jd_text,
        "resumes": "\n\n".join([doc.page_content for doc in relevant_resumes])
    }).content

def candidate_profiling(resume_text: str) -> str:
    """Analyze a single candidate's resume"""
    prompt = ChatPromptTemplate.from_template(
        """Analisis CV berikut dan berikan laporan profil kandidat:
        1. Ringkasan kualifikasi
        2. Kekuatan utama
        3. Area untuk pengembangan
        4. Rekomendasi peran yang cocok
        5. Pertanyaan wawancara yang mungkin
        
        CV:
        {resume_text}
        """
    )
    
    chain = prompt | llm
    return chain.invoke({"resume_text": resume_text}).content

def compare_candidates(resume_texts: List[str]) -> str:
    """Compare multiple candidates"""
    return compare_resumes(resume_texts, llm)