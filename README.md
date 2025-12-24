# Overview
This code repo demonstrates the simple integration between fast api &amp; langgraph
Little bit about FastAPI and Langchain
- FastAPI is a modern, high-performance web framework for building APIs with Python. It is designed to be incredibly fast to code and even faster to run, often competing with frameworks like Node.js and Go. Since it is built on top of Starlette (for web routing) and Pydantic (for data validation), it handles a lot of the heavy lifting that used to require manual boilerplate code.
- LangChain is an open-source framework designed to simplify the creation of applications using Large Language Models (LLMs) like GPT-4, Claude, or Llama. If an LLM is the "brain," LangChain is the nervous system and hands. It connects the brain to your data, your APIs, and your specific logic.
- LangGraph is an open-source framework developed by the LangChain team designed to build stateful, multi-actor applications with Large Language Models (LLMs). While standard LangChain is excellent for linear, "one-and-done" chains (Step A → Step B → Step C), LangGraph is built for complex workflows that require loops, conditional logic, and long-term memory.

# Running the Fast API
## Update the dependencies
pip install -r requirements.txt
## Update API Key
Update the OPENAI_API_KEY in .env file under root folder of this code 
## Run in local
uvicorn app.main:app --env-file .env --reload
## Example Request
POST /api/generate-email
{
  "intent": "Thank manager for mentorship",
  "tone": "Professional and warm",
  "context": "Worked together for 8 weeks on cloud migration project"
}
## Example Response
{
  "email": "Dear ... Thank you for your guidance..."
}

# Why LangGraph (vs Plain LangChain)

## LangGraph shines when you add:
- Review / retry loops
- Memory or state
- Conditional routing
- Multi-agent flows

## Example upgrades:
- Draft → Review → Improve → Approve
- Auto-detect tone
- Human-in-the-loop approval
- Email → Slack → Ticket agent chain