from sentence_transformers import SentenceTransformer, util

model=SentenceTransformer('all-MiniLM-L6-v2')

def compute_match(resume_text, job_description):
    # Encode the texts to get their embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    # Compute cosine similarity between the two embeddings
    cosine_scores = util.pytorch_cos_sim(resume_embedding, job_embedding)
    threshold=0.6

    matched=[]
    missing=[]

    for i,req_skills in enumerate(job_description):
        if any(score>=threshold for score in cosine_scores[i]):
            matched.append(req_skills)
        else:
            missing.append(req_skills)

    matched_score=round(len(matched)/len(job_description)*100,2)                           
    
    return {
        'matched_skills': matched,
        'missing_skills': missing,
        'match_percentage': matched_score
    }
