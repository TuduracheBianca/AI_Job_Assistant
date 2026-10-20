# AI Job Assistant

AI Job Assistant is a personal job-search automation project designed to help you manage job applications, organize opportunities from your inbox, and generate tailored cover letters based on a job description and your resume.

The goal is to turn the repetitive parts of applying for jobs into a streamlined workflow:

- collect and sort job applications from email
- extract job details from online postings
- match your profile to the role requirements
- generate a professional cover letter
- prepare a simple application workflow for follow-up

## Why this project exists

Applying for jobs often means doing the same tasks repeatedly:

- reading job emails and saving relevant opportunities
- opening job descriptions online
- comparing them with your CV/resume
- writing a new cover letter each time
- keeping track of what you applied to

This project aims to automate that process so you can focus on the best-fit roles and spend less time on repetitive admin work.

## Core features

### 1. Email-based application organization
The project is designed to process messages from your inbox and classify them as:

- new job opportunities
- follow-ups or recruiter emails
- application confirmations
- interview invitations
- rejected or archived applications

This makes it easier to keep a structured overview of your application pipeline.

### 2. Job description extraction
The workflow can read job descriptions from online listings and convert them into structured data for matching and drafting.

### 3. Resume-based personalization
Your profile data is used to generate tailored responses based on:

- experience
- education
- skills
- projects
- technologies

### 4. AI-powered cover letter generation
The assistant uses an AI model to draft a professional cover letter tailored to a specific job description and your resume.

### 5. Simple automation workflow
The application is built around a lightweight automation pipeline that can be expanded with:

- Gmail or IMAP email integration
- web scraping or browser automation for job boards
- parsing job descriptions into structured fields
- saving applications into a local database or JSON-based tracker

## Project vision

This project is intended to become a practical personal assistant for job hunting, with the following capabilities:

- organize all job applications in one place
- automatically detect relevant roles from email
- collect public job descriptions from the web
- compare them to your resume
- generate personalized cover letters
- track the status of each application over time

## Current repository status

This repository currently includes a prototype workflow for:

- loading a resume/profile JSON file
- reading a job description text file
- generating a cover letter using Gemini
- simulating a browser-based application submission for testing

It is a good starting point for a broader automation system, and it can be extended into a complete job-application organizer.

## Repository structure

```text
AI_Job_Assistant/
├── .env.example
├── .gitignore
├── data/
│   ├── job_description.txt
│   └── my_profile.json
├── src/
│   ├── ai_agent.py
│   └── web_agent.py
├── main.py
├── README.md
└── requirements.txt (to be added if you install dependencies explicitly)
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/TuduracheBianca/AI_Job_Assistant.git
cd AI_Job_Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# or
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

Install the packages required by the project, including the AI and browser automation libraries:

```bash
pip install python-dotenv google-genai playwright
```

If you later add a `requirements.txt`, you can install everything with:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

Then update the file with your real information:

```env
GEMINI_API_KEY="your_api_key_here"
EMAIL_ADDRESS="your_email@example.com"
EMAIL_PASSWORD="your_email_password"
```

## How it works

1. The app loads your profile from `data/my_profile.json`.
2. It reads the job description from `data/job_description.txt`.
3. It sends the resume and job description to the AI agent.
4. The AI generates a custom cover letter based on the role and your background.
5. The browser automation script can open a sample form and submit the generated text.

## Example run

```bash
python main.py
```

This will:

- load your profile data
- load the target job description
- generate a cover letter
- run the web automation demo

## Future roadmap

The project is planned to evolve into a more complete personal job application manager with features like:

- Gmail integration for reading and organizing job emails
- automatic extraction of job titles, companies, and deadlines
- saved application history per company or role
- resume/job match scoring
- AI-generated cover letters and follow-up emails
- browser-based job application support
- dashboard for tracking application status

## Example use cases

- Import an email containing a job listing and automatically detect the company and role.
- Pull a job description from a website and generate a tailored cover letter in seconds.
- Save all applications in a structured list to track progress.
- Compare the job description with your profile to see whether you are a strong fit.

## Notes

This project uses a local `.env` file for secrets and should not commit sensitive credentials.

The current version is a foundation for automation. The next step is to add:

- email parsing
- job board scraping
- structured data storage
- a dashboard or CLI for tracking applications
