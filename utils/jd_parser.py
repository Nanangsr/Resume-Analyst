from utils.resume_parser import parse_resume

def parse_jd(file) -> str:
    """Extract text from job description file"""
    return parse_resume(file)  