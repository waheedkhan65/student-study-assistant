import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


load_dotenv()

MODEL = "gemini-3.8-flash"


# ============================================================
# BASIC PYTHON TOOLS
# ============================================================

def calculate_percentage(correct: int, total: int) -> str:
    """
    Calculates the percentage score of a quiz.
    """

    if total <= 0:
        return "Total questions must be greater than zero."

    percentage = (correct / total) * 100

    return f"Score: {correct}/{total} = {percentage:.2f}%"


def make_study_plan(topic: str, days: int) -> str:
    """
    Creates a simple study plan for a topic.
    """

    if days <= 0:
        return "Number of days must be greater than zero."

    plan = []

    for day in range(1, days + 1):

        if day == 1:
            task = f"Learn the basic concepts of {topic}."

        elif day == 2:
            task = f"Study examples and practical applications of {topic}."

        elif day == 3:
            task = f"Practice questions related to {topic}."

        elif day == days:
            task = f"Review everything about {topic} and take a self-test."

        else:
            task = f"Continue studying and practicing {topic}."

        plan.append(f"Day {day}: {task}")

    return "\n".join(plan)


# ============================================================
# MCP SERVER CONNECTION
# ============================================================

MCP_SERVER_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "mcp_server.py"
)


mcp_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="python",
            args=[MCP_SERVER_PATH],
        )
    )
)



# TUTOR AGENT

tutor_agent = LlmAgent(
    name="tutor_agent",

    model=MODEL,

    description=(
        "A teaching agent that explains academic concepts "
        "in simple language."
    ),

    instruction="""
        You are the Tutor Agent.

        Your job is to teach students.

        When the student asks about a topic:

        1. Give a simple definition.
        2. Explain the concept step by step.
        3. Give a simple real-world example.
        4. Mention important points.
        5. Ask whether the student wants a quiz.

        Use simple English.

        Do not make explanations unnecessarily complicated.

        You are especially good at Computer Science,
        Software Engineering, Artificial Intelligence,
        Machine Learning, Python, and Deep Learning.
    """,
)


# QUIZ AGENT

quiz_agent = LlmAgent(
    name="quiz_agent",

    model=MODEL,

    description=(
        "An agent that creates quizzes and evaluates "
        "student answers."
    ),

    instruction="""
    You are the Quiz Agent.

    Your job is to test the student's knowledge.

    When the student requests a quiz:

    1. Create clear questions.
    2. Prefer multiple-choice questions unless
    the student requests another format.
    3. Do not immediately reveal the answers.
    4. Wait for the student's answers.
    5. Evaluate the answers.
    6. Explain mistakes.
    7. Give the final score.

    Keep quizzes appropriate for a university student.

    If the student asks about a previous quiz,
    use the current conversation context.
""",

    tools=[
        calculate_percentage
    ],
)



# STUDY PLANNER AGENT

planner_agent = LlmAgent(
    name="planner_agent",

    model=MODEL,

    description=(
        "An agent that creates personalized study plans for students."
    ),

    instruction="""
    You are the Study Planner Agent.
    Your job is to create practical study plans.
    Ask for or infer:
    - Topic
    - Number of days
    - Student's goal

    Create a realistic daily plan.
    You also have access to MCP study tools.
    Use the MCP tools when they can provide
    useful study tips or a checklist.

    Keep the plan simple and realistic.
 """,

    tools=[
        make_study_plan,
        mcp_toolset,
    ],
)



# MAIN STUDY MANAGER AGENT

root_agent = LlmAgent(
    name="study_manager",

    model=MODEL,

    description=(
        "Main student study assistant that coordinates "
        "the tutor, quiz, and planner agents."
    ),

    instruction="""
    You are the Study Manager.

    You are the main agent of a Student Study Assistant.

    Your job is to understand what the student needs
    and delegate the task to the correct specialized agent.

    AVAILABLE SPECIALIZED AGENTS:

    1. tutor_agent
    Use for:
    - explanations
    - teaching concepts
    - examples
    - difficult topics

    2. quiz_agent
    Use for:
    - quizzes
    - tests
    - checking answers
    - scores

    3. planner_agent
    Use for:
    - study plans
    - schedules
    - study checklists
    - study strategies

    IMPORTANT:

    Do not try to do every task yourself.

    Delegate the task to the appropriate specialized agent.

    Examples:

    Student:
    "Explain CNN."

    Delegate to tutor_agent.

    Student:
    "Give me a quiz about CNN."

    Delegate to quiz_agent.

    Student:
    "Make me a 7-day Machine Learning study plan."

    Delegate to planner_agent.

    If the request involves multiple tasks,
    coordinate the specialized agents in a logical order.

    Always answer in simple English.

    Remember that this is a student learning assistant,
    so explanations should be clear and beginner-friendly.
""",

    sub_agents=[
        tutor_agent,
        quiz_agent,
        planner_agent,
    ],
)