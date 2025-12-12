# AutoHire_AI 

**AutoHire_AI** is an intelligent, AI-powered assistant designed to streamline your job application process. It helps you tailor your resume to specific job descriptions (JDs) and generates professional cover letters, increasing your chances of getting hired.

> **Note:** This is **Phase 1** of the AutoHire project, focusing on document preparation and tailoring.

Built with [Chainlit](https://docs.chainlit.io), [LangChain](https://www.langchain.com/), and OpenAI.

## Roadmap 

**Phase 2 (In Development):**
*   **MCP Integration:** Integrating Model Context Protocol (MCP) servers.
*   **Auto-Apply:** Automated job application agents with access to platforms like:
    *   **Naukri.com**
    *   **LinkedIn**
    *   *More coming soon...*
*   **End-to-End Automation:** Complete pipeline from resume tailoring to submitting the application.

## Features 

*   ** Resume Parsing:** Automatically extracts text from uploaded PDF resumes.
*   ** Job Description Analysis:** Fetches and extracts JD text from direct input or URLs.
*   ** Smart Analysis:** Uses AI to analyze the match between your resume and the job description.
*   ** Tailored Resume Generation:** Generates a new, ATS-friendly resume content optimized for the specific job.
*   ** Cover Letter Creation:** Writes a personalized and concise cover letter.
*   ** PDF Export:** Downloads the tailored resume and cover letter as professionally formatted PDF files.
*   ** Interactive Chat:** User-friendly chat interface for seamless interaction.

## Prerequisites 

*   Python 3.8+
*   An OpenAI API Key

## Installation 

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/AutoHire_AI.git
    cd AutoHire_AI
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
    *   Create a `.env` file in the root directory.
    *   Add your OpenAI API Key:
        ```env
        OPENAI_API_KEY=your_openai_api_key_here
        ```
    *   (Optional) You can use `.env.example` as a template.

## Usage 

1.  **Run the application:**
    ```bash
    chainlit run app.py -w
    ```

2.  **Access the UI:**
    *   The app will open in your default browser (usually at `http://localhost:8000`).

3.  **Follow the steps:**
    *   **Upload Resume:** Upload your existing resume (PDF format).
    *   **Provide JD:** Paste the Job Description text or provide a URL to the job posting.
    *   **Wait for Magic:** The AI will analyze, tailor, and generate your new documents.
    *   **Download:** Download the generated `tailored_resume.pdf` and `cover_letter.pdf`.

## Structure 

*   `app.py`: Main application entry point containing the Chainlit logic.
*   `src/`: Source code for agents and utilities.
    *   `src/agents.py`: Logic for AI analysis and generation.
    *   `src/utils.py`: Helper functions for text extraction and PDF generation.
*   `output/`: Directory where generated PDFs are saved.

## Contributing 

Contributions are welcome! Please feel free to submit a Pull Request.

## License 

[MIT](LICENSE)
