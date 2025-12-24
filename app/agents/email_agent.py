from typing import TypedDict
from langchain.messages import HumanMessage
from app.services.llm import get_llm
from langgraph.graph import StateGraph, END

class EmailState(TypedDict):
    intent: str
    tone: str
    context: str
    email: str



llm = get_llm()

def draft_email(state: EmailState) -> EmailState:
    prompt = f"""
    Write an email with the following details:
    Intent: {state['intent']}
    Tone: {state['tone']}
    Context: {state['context']}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    state["email"] = response.content
    return state



def build_email_graph():
    graph = StateGraph(EmailState)

    graph.add_node("draft_email", draft_email)
    graph.set_entry_point("draft_email")
    graph.add_edge("draft_email", END)

    return graph.compile()