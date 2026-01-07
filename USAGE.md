# 📘 AutoHire Usage Guide

## Installation

Anyone in the world can now install your package:

```bash
pip install autohire
```

---

## Quick Start

### Option 1: Python Script (Programmatic Usage)

Create a Python file (e.g., `tailor_my_resume.py`):

```python
from autohire.core import process_resume

# Simple usage
result = process_resume(
    resume_path="my_resume.pdf",      # or .docx
    jd_path="job_description.txt",    # Job description file
    openai_api_key="sk-proj-..."      # Your OpenAI API key
)

print(result)
# Output: "Success! Tailored resume saved to tailored_resume/my_resume_tailored.pdf"
```

**What happens:**
1. The function extracts text from your resume and JD
2. Uses GPT-4o to analyze the gap between your resume and the job requirements
3. Generates an ATS-optimized, tailored resume
4. Saves it to `tailored_resume/` folder

---

### Option 2: Command Line Interface (CLI)

You can also use the built-in command:

```bash
autohire my_resume.pdf job_description.txt --key sk-proj-...
```

Or set your API key as an environment variable:

```bash
# Windows
set OPENAI_API_KEY=sk-proj-...

# Linux/Mac
export OPENAI_API_KEY=sk-proj-...

# Then run without --key flag
autohire my_resume.pdf job_description.txt
```

---

### Option 3: Web UI (Chainlit App)

If you've cloned the repository, you can still use the interactive web interface:

```bash
git clone https://github.com/YourUsername/AutoHire_AI.git
cd AutoHire_AI
pip install -r requirements.txt
chainlit run app.py
```

Then open your browser at `http://localhost:8000`.

---

## Supported File Formats

| Type | Formats | Notes |
|------|---------|-------|
| **Resume** | `.pdf`, `.docx` | Most common formats |
| **Job Description** | `.txt`, `.pdf`, `.docx` | Plain text recommended |

---

## Advanced: Using in Your Own Application

```python
import os
from autohire.core import process_resume

# Example: Batch processing multiple resumes
resumes = ["resume1.pdf", "resume2.docx"]
jd = "software_engineer_jd.txt"
api_key = os.getenv("OPENAI_API_KEY")

for resume in resumes:
    result = process_resume(resume, jd, api_key)
    print(f"Processed {resume}: {result}")
```

---

## API Reference

### `process_resume(resume_path, jd_path, openai_api_key)`

**Parameters:**
- `resume_path` (str): Absolute or relative path to resume file (.pdf or .docx)
- `jd_path` (str): Path to job description file (.txt, .pdf, or .docx)
- `openai_api_key` (str): Your OpenAI API key

**Returns:**
- `str`: Success/error message

**Output:**
- Creates `tailored_resume/` directory
- Saves `{original_filename}_tailored.pdf` inside it

---

## Troubleshooting

### Dependency Conflicts

If you see errors like:
```
feast requires uvicorn<=0.34.0, but you have uvicorn 0.40.0
```

See [dependency_resolution.md](file:///c:/GitHub_Master/AutohireAI/dependency_resolution.md) for fixes.

### API Key Issues

Make sure your OpenAI API key:
- Starts with `sk-proj-` or `sk-`
- Has sufficient credits
- Is passed correctly to the function

---

## Examples Repository Structure

```
my_job_applications/
├── resumes/
│   ├── john_doe_resume.pdf
│   └── jane_smith_resume.docx
├── job_descriptions/
│   ├── google_swe.txt
│   └── amazon_ml.txt
├── tailor_resume.py  # Your script
└── tailored_resume/  # Auto-generated output folder
    ├── john_doe_resume_tailored.pdf
    └── jane_smith_resume_tailored.pdf
```

**Script example (`tailor_resume.py`):**

```python
from autohire.core import process_resume
import os

api_key = os.getenv("OPENAI_API_KEY")

# Tailor John's resume for Google
process_resume(
    "resumes/john_doe_resume.pdf",
    "job_descriptions/google_swe.txt",
    api_key
)

# Tailor Jane's resume for Amazon
process_resume(
    "resumes/jane_smith_resume.docx",
    "job_descriptions/amazon_ml.txt",
    api_key
)
```

---

## What's Next?

Check out the [Phase 2 Roadmap](file:///c:/GitHub_Master/AutohireAI/README.md) for upcoming features like:
- Auto-apply to job boards (Naukri, LinkedIn)
- MCP integration
- Cover letter generation (already available in web UI!)
