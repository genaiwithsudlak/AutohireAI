import chainlit as cl
import os
from dotenv import load_dotenv
from autohire.utils import extract_text_from_pdf, extract_text_from_url, create_pdf_from_text
from autohire.agents import analyze_resume_and_jd, generate_tailored_resume, generate_cover_letter
from langchain_openai import ChatOpenAI

load_dotenv()

@cl.on_chat_start
async def start():
    # Initialize LLM for this session
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
    cl.user_session.set("llm", llm)

    files = None
    
    # Wait for the user to upload a resume
    while files == None:
        files = await cl.AskFileMessage(
            content="Welcome to AutoHire_AI! Please upload your Resume (PDF) to get started.",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    resume_file = files[0]
    
    msg = cl.Message(content=f"Processing `{resume_file.name}`...")
    await msg.send()
    
    # Extract text from Resume
    resume_text = extract_text_from_pdf(resume_file.path)
    
    cl.user_session.set("resume_text", resume_text)
    
    msg.content = f"Resume processed. Now, please provide the Job Description. You can paste the text or provide a URL."
    await msg.update()

@cl.on_message
async def main(message: cl.Message):
    resume_text = cl.user_session.get("resume_text")
    if not resume_text:
        await cl.Message(content="Please restart the session and upload a resume first.").send()
        return

    jd_input = message.content
    jd_text = ""
    
    if jd_input.startswith("http"):
        msg = cl.Message(content="Fetching JD from URL...")
        await msg.send()
        jd_text = extract_text_from_url(jd_input)
        msg.content = "JD fetched."
        await msg.update()
    else:
        jd_text = jd_input

    if len(jd_text) < 50:
        await cl.Message(content="The JD seems too short. Please provide a valid Job Description.").send()
        return

    # Analysis
    msg = cl.Message(content="Analyzing Resume and JD...")
    await msg.send()
    
    llm = cl.user_session.get("llm")
    analysis = analyze_resume_and_jd(resume_text, jd_text, llm)
    
    await cl.Message(content=f"**Analysis Result:**\n\n{analysis}").send()
    
    # Tailoring
    msg = cl.Message(content="Generating Tailored Resume...")
    await msg.send()
    
    tailored_resume = generate_tailored_resume(resume_text, jd_text, analysis, llm)
    
    await cl.Message(content=f"**Tailored Resume:**\n\n{tailored_resume}").send()
    
    # Cover Letter
    msg = cl.Message(content="Generating Cover Letter...")
    await msg.send()
    
    cover_letter = generate_cover_letter(resume_text, jd_text, llm)
    
    await cl.Message(content=f"**Cover Letter:**\n\n{cover_letter}").send()
    
    # PDF Generation
    msg = cl.Message(content="Generating PDFs...")
    await msg.send()
    
    os.makedirs("output", exist_ok=True)
    resume_path = "output/tailored_resume.pdf"
    cl_path = "output/cover_letter.pdf"
    
    create_pdf_from_text(tailored_resume, resume_path)
    create_pdf_from_text(cover_letter, cl_path)
    
    elements = [
        cl.File(name="tailored_resume.pdf", path=resume_path, display="inline"),
        cl.File(name="cover_letter.pdf", path=cl_path, display="inline")
    ]
    
    await cl.Message(content="Here are your files:", elements=elements).send()
