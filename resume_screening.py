import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATASET_PATH = "Resume.csv"

df = pd.read_csv(DATASET_PATH)

df = df[["Resume_str", "Category"]].dropna()
df.columns = ["resume_text", "category"]

df["resume_text"] = df["resume_text"].astype(str)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["clean_resume"] = df["resume_text"].apply(clean_text)

job_description = """
We are looking for a Data Scientist with strong skills in Python, Machine Learning,
Data Analysis, SQL, statistics, and experience with libraries such as Pandas,
NumPy, Scikit-learn, and visualization tools. Knowledge of deep learning,
NLP, and cloud platforms is a plus.
"""

job_description = clean_text(job_description)

skill_list = [
    "python", "machine learning", "data analysis", "sql",
    "statistics", "pandas", "numpy", "scikit", "visualization",
    "deep learning", "nlp", "cloud", "tensorflow", "keras"
]

def extract_skills(text):
    return sorted(set(skill for skill in skill_list if skill in text))

df["skills_found"] = df["clean_resume"].apply(extract_skills)

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

tfidf_matrix = vectorizer.fit_transform(
    df["clean_resume"].tolist() + [job_description]
)

job_vector = tfidf_matrix[-1]
resume_vectors = tfidf_matrix[:-1]

df["match_score"] = cosine_similarity(resume_vectors, job_vector).flatten()

df = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)
df["rank"] = df.index + 1

required_skills = set(skill_list)

def find_missing(skills):
    return sorted(required_skills - set(skills))

df["missing_skills"] = df["skills_found"].apply(find_missing)

df_final = df[[
    "rank",
    "category",
    "match_score",
    "skills_found",
    "missing_skills"
]]

df_final.to_csv("ranked_resumes.csv", index=False)

print("\nTop 10 Ranked Candidates:\n")
print(df_final.head(10))