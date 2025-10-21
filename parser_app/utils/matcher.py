from sentence_transformers import SentenceTransformer, util
import re
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_match(resume_text, required_skills_list):
    """
    Compare resume skills against a list of required skills using semantic similarity.
    
    Args:
        resume_text: String containing resume skills section
        required_skills_list: List of required skill strings
    
    Returns:
        Dictionary with matched_skills, missing_skills, and match_percentage
    """
    if not resume_text or not required_skills_list:
        return {
            "match_percentage": 0.0,
            "matched_skills": [],
            "missing_skills": required_skills_list if required_skills_list else []
        }
    # Convert to lower and split using multiple delimiters
    resume_skills = re.split(r'[,\n;/\-\|]', resume_text.lower())

    # Also split big chunks into tokens if they contain many words
    resume_skills = [s.strip() for skill in resume_skills for s in skill.split() if s.strip()]
    print("Resume skills:", resume_skills)
    print("Required skills:", required_skills_list)

    # Encode resume text once
    resume_embedding = model.encode(resume_skills, convert_to_tensor=True)
    
    # Encode each required skill individually
    required_skills_embeddings = model.encode(required_skills_list, convert_to_tensor=True)

    # Compute cosine similarity between resume and each required skill
    # This will give us a tensor of shape (1, N) where N is number of required skills
    cosine_scores = util.cos_sim(required_skills_embeddings,resume_embedding)

    threshold = 0.6
    matched = []
    missing = []

    # Iterate over each required skill and check similarity
    for i, req_skill in enumerate(required_skills_list):
        max_score = cosine_scores[i].max().item()
        print(f"Skill: '{req_skill}' - Max Similarity: {max_score:.4f}")
        if max_score >= threshold:
            matched.append(req_skill)
        else:
            missing.append(req_skill)

    # Calculate match percentage
    match_percentage = round(len(matched) / len(required_skills_list) * 100, 2) if required_skills_list else 0.0

    return {
        'matched_skills': matched,
        'missing_skills': missing,
        'match_percentage': match_percentage
    }