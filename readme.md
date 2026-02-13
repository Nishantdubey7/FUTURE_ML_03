# 📄 Resume Screening & Candidate Ranking System
### Machine Learning–Based Automated Resume Evaluation

---

## 📌 Overview

This project presents a **Machine Learning–based Resume Screening System** designed to automatically evaluate and rank resumes based on their relevance to a specific job description.  

The system uses **Natural Language Processing (NLP)** and **TF-IDF vectorization** to measure similarity between candidate resumes and a target job role. It generates ranked results along with identified skills and missing competencies, supporting efficient and data-driven recruitment decisions.

---

## 🎯 Project Objective

The goal of this project is to build an intelligent screening pipeline that can:

- Automatically process resume data  
- Extract relevant technical skills  
- Compare resumes with a defined job description  
- Calculate similarity scores  
- Rank candidates based on relevance  
- Identify missing required skills  

---

## 🛠️ Technologies & Libraries Used

- **Python**  
- **Pandas** – Data manipulation  
- **Scikit-learn** – TF-IDF Vectorization & Cosine Similarity  
- **Regular Expressions (re)** – Text preprocessing  

---

## 📂 Repository Structure
├── Resume.csv # Input dataset containing resume data

├── resume_screening.py # Main Python script

├── ranked_resumes.csv # Output file with ranked candidates

├── README.md # Project documentation


---

## 📊 Dataset Description

**Resume.csv** contains:  

- `Resume_str` – Full resume text  
- `Category` – Resume domain/category  

The script preprocesses and standardizes the text before performing analysis.

---

## ⚙️ System Workflow

### 1️⃣ Data Preprocessing
- Convert text to lowercase  
- Remove numbers and special characters  
- Remove extra spaces  
- Normalize text for analysis  

### 2️⃣ Skill Extraction
A predefined skill set is used to identify relevant competencies, including:

- Python  
- Machine Learning  
- Data Analysis  
- SQL  
- Statistics  
- Pandas  
- NumPy  
- Scikit-learn  
- Visualization  
- Deep Learning  
- NLP  
- Cloud  
- TensorFlow  
- Keras  

### 3️⃣ Feature Engineering
- Convert resumes and job description into numerical vectors using **TF-IDF Vectorization**  
- Remove English stop words  
- Limit feature space to 5000 features  

### 4️⃣ Similarity Computation
- Use **Cosine Similarity** to compare each resume to the job description  
- Generate a `match_score` (higher score = better match)  

### 5️⃣ Ranking & Skill Gap Analysis
- Sort resumes by similarity score  
- Assign ranking automatically  
- Identify missing required skills  

---

## 📈 Output

The system generates:

### 📄 `ranked_resumes.csv`

Columns include:

- `rank`  
- `category`  
- `match_score`  
- `skills_found`  
- `missing_skills`  

Additionally, the script prints the **Top 10 ranked candidates** in the console.

---

## 💡 Practical Use Case

For example, when hiring for a Data Scientist role, this system:

-Screens all resumes automatically

-Identifies relevant technical skills

-Scores candidates against the job description

-Ranks candidates from best to least fit

-Highlights skill gaps

This significantly reduces manual screening effort and improves consistency in candidate evaluation.
