from typing import Dict, List, Union
from core.rag_chain import (
    candidate_search,
    candidate_profiling,
    compare_candidates
)

def process_use_case(use_case: str, inputs: Union[Dict, List]) -> str:
    """Route the use case to appropriate function"""
    if use_case == "Candidate Search by Job Description":
        return candidate_search(inputs["jd_text"])
    elif use_case == "Candidate Profiling / Resume QA":
        return candidate_profiling(inputs["resume_text"])
    elif use_case == "Compare Multiple Candidates":
        return compare_candidates(inputs["resume_texts"])
    else:
        return "Invalid use case"