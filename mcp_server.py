from mcp.server.mcpserver import MCPServer


# ============================================================
# CREATE MCP SERVER
# ============================================================

mcp = MCPServer(
    "StudentStudyTools",
    instructions="Study tools for the Student Study Assistant."
)


# ============================================================
# MCP TOOL 1
# ============================================================

@mcp.tool()
def get_study_tip(topic: str) -> str:
    """
    Provides a simple study tip for a given topic.
    """

    tips = {
        "machine learning":
            "First understand datasets, features, labels, training, validation, and testing.",

        "deep learning":
            "First understand neural networks, layers, activation functions, loss functions, and backpropagation.",

        "python":
            "Practice small programs and understand variables, conditions, loops, functions, and classes.",

        "database":
            "Understand tables, primary keys, foreign keys, SQL queries, and relationships.",

        "software engineering":
            "Focus on requirements, design, implementation, testing, and maintenance."
    }

    topic_lower = topic.lower()

    for key, tip in tips.items():
        if key in topic_lower:
            return tip

    return (
        f"For {topic}, divide the topic into small concepts, "
        "learn one concept at a time, and test yourself with questions."
    )


# ============================================================
# MCP TOOL 2
# ============================================================

@mcp.tool()
def create_study_checklist(topic: str) -> str:
    """
    Creates a simple study checklist.
    """

    return f"""
Study Checklist for: {topic}

[ ] Understand the basic definition
[ ] Learn the important concepts
[ ] Study a simple example
[ ] Practice questions
[ ] Review mistakes
[ ] Explain the topic in your own words
[ ] Take a short quiz
"""


# ============================================================
# START MCP SERVER
# ============================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")