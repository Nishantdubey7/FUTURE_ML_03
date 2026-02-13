📄 Resume Screening & Candidate Ranking System
Machine Learning–Based Automated Resume Evaluation

📌 Overview

This project presents a Machine Learning–based Resume Screening System designed to automatically evaluate and rank resumes based on their relevance to a specific job description.

The system applies Natural Language Processing (NLP) techniques and TF-IDF vectorization to measure the similarity between candidate resumes and a target job role. It generates ranked results along with identified skills and missing competencies, supporting more efficient and data-driven recruitment decisions.

🎯 Project Objective

To build an intelligent screening pipeline that:

Automatically processes resume data

Extracts relevant technical skills

Compares resumes with a defined job description

Calculates similarity scores

Ranks candidates based on relevance

Identifies missing required skills

🛠️ Technologies & Libraries Used

Python

Pandas – Data manipulation

Scikit-learn – TF-IDF Vectorization & Cosine Similarity

Regular Expressions (re) – Text preprocessing

📂 Repository Structure

This repository contains the following 4 files:

├── Resume.csv              # Input dataset containing resume data
├── resume_screening.py     # Main Python script
├── ranked_resumes.csv      # Output file with ranked candidates
├── README.md               # Project documentation

📊 Dataset Description

Resume.csv contains:

Resume_str – Full resume text

Category – Resume domain/category

The script preprocesses and standardizes the text before performing analysis.

⚙️ System Workflow
1️⃣ Data Preprocessing

Convert text to lowercase

Remove numbers and special characters

Remove extra spaces

Normalize text for analysis

2️⃣ Skill Extraction

A predefined skill set is used to identify relevant competencies, including:

Python

Machine Learning

Data Analysis

SQL

Statistics

Pandas

NumPy

Scikit-learn

Visualization

Deep Learning

NLP

Cloud

TensorFlow

Keras

3️⃣ Feature Engineering

TF-IDF Vectorization converts text into numerical vectors

English stop words are removed

Feature space limited to 5000 features

4️⃣ Similarity Computation

Cosine Similarity compares each resume to the job description

A match_score is generated (higher score = better match)

5️⃣ Ranking & Skill Gap Analysis

Resumes are sorted by similarity score

Ranking is assigned automatically

Missing required skills are identified

📈 Output

The system generates:

📄 ranked_resumes.csv

With the following columns:

rank

category

match_score

skills_found

missing_skills

Additionally, the script prints the Top 10 ranked candidates in the console.

▶️ How to Run the Project
Step 1: Install Required Libraries
pip install pandas scikit-learn

Step 2: Ensure File Placement

Make sure the following files are in the same directory:

Resume.csv

resume_screening.py

Step 3: Execute the Script
python resume_screening.py


The output file ranked_resumes.csv will be generated automatically.

💡 Practical Use Case

For example, when hiring for a Data Scientist role, this system:

Screens all resumes automatically

Identifies relevant technical skills

Scores candidates against the job description

Ranks them from best to least fit

Highlights skill gaps

This significantly reduces manual screening effort and improves consistency in candidate evaluation.
