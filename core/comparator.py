from typing import List
from langchain.prompts import ChatPromptTemplate  

def compare_resumes(resume_texts: List[str], llm) -> str:
    """Bandingkan beberapa resume"""
    prompt = ChatPromptTemplate.from_template(
        """Bandingkan beberapa kandidat berikut dan berikan rekomendasi:
        1. Ringkasan perbandingan
        2. Kandidat terbaik untuk peran teknis
        3. Kandidat terbaik untuk peran kepemimpinan
        4. Pertimbangan budaya perusahaan
        
        Resume Kandidat:
        {resumes}
        """
    )
    
    formatted_resumes = "\n\n---\n\n".join(
        f"Kandidat {i+1}:\n{text}" for i, text in enumerate(resume_texts))
    
    chain = prompt | llm
    return chain.invoke({"resumes": formatted_resumes}).content