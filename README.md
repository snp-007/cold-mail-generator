# 📧 Cold Mail Generator

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM_Foundation-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-6A0DAD)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![GitHub Stars](https://img.shields.io/github/stars/snp-007/cold-mail-generator?style=social)
![GitHub Forks](https://img.shields.io/github/forks/snp-007/cold-mail-generator?style=social)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success)](YOUR_STREAMLIT_URL)

An AI-powered Cold Email Generator that helps software consulting and service companies automate outreach to potential clients based on job postings.

The application extracts job information directly from a company's careers page, identifies the required skills, matches them with relevant portfolio projects using a vector database, and generates personalized cold emails using LLMs.

---

## 🚀 Problem Statement

Imagine a scenario:

- Nike is hiring a **Principal Software Engineer**.
- Nike invests significant time and resources in hiring, onboarding, training, and retaining talent.
- A-company is a software consulting firm capable of providing dedicated software engineers and development teams.
- A Business Development Executive (XYZ) from A-company wants to reach out to Nike with a personalized cold email offering relevant services.

Manually researching job requirements and crafting customized emails for every opportunity is time-consuming.

This project automates the entire process.

---

## ✨ Features

- Extracts job descriptions directly from career page URLs
- Uses LLMs to parse and structure job information
- Identifies:
  - Role
  - Experience
  - Skills
  - Job Description
- Searches a portfolio database using semantic similarity
- Retrieves the most relevant portfolio links
- Generates personalized cold emails
- Streamlit-based user interface
- Groq-powered LLM inference
- ChromaDB vector database integration

---

## 🏗️ Architecture

```text
Career Page URL
        │
        ▼
 Web Scraping
        │
        ▼
 Text Cleaning
        │
        ▼
      LLM
        │
        ▼
 Extract Job Details
 (Role, Skills, Experience,
  Description)
        │
        ▼
    ChromaDB
(Vector Search on Portfolio)
        │
        ▼
 Relevant Portfolio Links
        │
        ▼
      LLM
        │
        ▼
 Personalized Cold Email
```

---

## 📊 Workflow

1. User enters a careers page URL.
2. The webpage content is loaded using LangChain's `WebBaseLoader`.
3. Raw content is cleaned and preprocessed.
4. Groq LLM extracts job details in structured JSON format.
5. Required skills are embedded and searched against the portfolio database.
6. Relevant portfolio links are retrieved from ChromaDB.
7. A personalized cold email is generated.
8. Results are displayed through Streamlit.

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### LLM Framework
- LangChain

### LLM Provider
- Groq
- Llama 3.3 70B Versatile

### Vector Database
- ChromaDB

### Data Processing
- Pandas
- Regex

### Environment Management
- Python Dotenv

---

## 📂 Project Structure

```text
cold-mail-generator/
│
├── app/
│   ├── app.py
│   ├── chains.py
│   ├── portfolio.py
│   ├── utils.py
│   │
│   └── resources/
│       └── portfolio_links.csv
│
├── vectorstore/
├── .env
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/snp-007/cold-mail-generator.git
cd cold-mail-generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com

---

## 📁 Portfolio Dataset

The application uses a portfolio database stored in:

```text
app/resources/portfolio_links.csv
```

Example:

```csv
Techstack,Links
Python,Django,MySQL,https://example.com/python-project
Machine Learning,TensorFlow,Python,https://example.com/ml-project
React,JavaScript,TypeScript,https://example.com/frontend-project
```

These records are embedded and stored inside ChromaDB for semantic retrieval.

---

## ▶️ Running the Application

```bash
streamlit run app/app.py
```

The application will launch in your browser.

---

## 📸 Sample Output

### Input

Career page URL:

```text
https://careers.nike.com/job/...
```

### Extracted Information

```json
{
  "role": "Director Software Engineering",
  "experience": "15+ years",
  "skills": [
    "TypeScript",
    "React",
    "Cloud Computing",
    "Architecture"
  ]
}
```

### Generated Email

```text
Subject: Expert Software Engineering Solutions for Nike

Dear Hiring Team,

I came across the Director Software Engineering role at Nike and was impressed by your focus on innovation and scalable software systems.

At A-company, we specialize in AI Solutions, Data Engineering, Cloud Solutions, and Software Development. Our team can provide experienced engineers capable of supporting Nike's technology initiatives.

Relevant portfolio:
- Portfolio Link 1
- Portfolio Link 2

I would welcome the opportunity to discuss how our expertise can support your business objectives.

Best Regards,
XYZ
Business Development Executive
A-company
```

---

## 🔮 Future Improvements

- Multi-job extraction from large career portals
- Support for PDF job descriptions
- Email export functionality
- Direct Gmail/Outlook integration
- Portfolio ranking using similarity scores
- Multi-language support
- RAG-based company research before email generation
- ATS keyword analysis

---

## 🎯 Learning Outcomes

This project demonstrates:

- LLM Application Development
- Prompt Engineering
- Retrieval Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- LangChain Workflows
- Streamlit Deployment
- Real-world AI Automation

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Siba Narayana Parida**
  
NIT Rourkela

Interested in:
- Software Development
- Machine Learning
- Data Science
- Generative AI
- LLM Applications

Feel free to connect and contribute!