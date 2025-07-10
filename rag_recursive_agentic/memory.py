# memory.py

class ConversationMemory:
    def __init__(self):
        self.history = []
        self.last_domain = None
        self.last_source = None

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})

    def add_assistant_message(self, message):
        self.history.append({"role": "assistant", "content": message})

    def get_formatted_history(self):
        """
        Returns:
            str: Formatted conversation history for LLM prompt.
        """
        formatted = ""
        for turn in self.history:
            role = turn["role"].capitalize()
            content = turn["content"].strip()
            formatted += f"{role}: {content}\n"
        return formatted.strip()

    def reset(self):
        self.history = []
        self.last_domain = None
        self.last_source = None
