# Student Study Assistant

A lightweight AI-powered study assistant built with Python, Google ADK, and an MCP server. It helps students by:

- explaining academic topics in simple language
- creating and grading short quizzes
- generating personalized study plans
- providing study tips and checklists through MCP tools

## Project overview

This project contains:

- `agent.py` — defines the tutor, quiz, planner, and study-manager agents
- `mcp_server.py` — exposes MCP tools for study tips and checklists
- `__init__.py` — imports the main agent module

## Main agents

### Tutor agent
Provides concept explanations, examples, and simplified learning guidance.

### Quiz agent
Creates quiz questions, waits for answers, evaluates them, and returns a final score.

### Planner agent
Builds practical study plans and can use the MCP study tools for topic-specific advice.

### Study manager
Coordinates the specialized agents and routes the user request to the appropriate one.

## MCP tools

The MCP server includes:

- `get_study_tip(topic: str)`
  - returns a topic-specific study recommendation
- `create_study_checklist(topic: str)`
  - creates a short study checklist for a topic

## Environment setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate it:

   - Windows PowerShell:

     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

   - Windows Command Prompt:

     ```bat
     .\.venv\Scripts\activate.bat
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables. The app loads values from a `.env` file using `python-dotenv`.

   Example:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Example usage

This project is designed to be used as a Google ADK agent module. You can import the main agent like this:

```python
from agent import root_agent
```

You can then connect `root_agent` to your ADK runtime or orchestration flow.

## Dependencies

The project relies on:

- `google-adk`
- `mcp`
- `python-dotenv`

## Notes

- The MCP server is started with the `stdio` transport and is launched through `agent.py`.
- The model name is currently set to `gemini-3.8-flash` in `agent.py`.
- If your environment uses a different Google AI model or credentials flow, update the configuration accordingly.

## License

This project is provided as a starter educational example and can be adapted for your own study assistant workflows.
