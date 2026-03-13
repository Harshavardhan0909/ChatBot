def build_system_prompt(mode):

    if mode == "Concise":
        return """
        You are an AI assistant.
        Provide short, summarized answers.
        Keep responses within 3-4 sentences.
        """

    if mode == "Detailed":
        return """
        You are an AI assistant.
        Provide detailed explanations with examples.
        Expand answers clearly.
        """