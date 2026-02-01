class CollegeHelpdeskAgent:
    def __init__(self):
        self.knowledge_base = {
            "exam fee": "Undergraduate exam fee is $150 per exam.",
            "semester registration": "Semester registration opens in May and November."
        }
    def process_query(self, user_input):
        user_input = user_input.lower()
        if "id card" in user_input or "complaint" in user_input:
            return self.create_support_ticket(user_input)

        for key in self.knowledge_base:
            if key in user_input:
                return self.knowledge_base[key]

        return "I will escalate this issue to the support team."

    def create_support_ticket(self, issue):
        return (
            "Support ticket created successfully. "
            "Our support team will contact you via email."
        )

if __name__ == "__main__":
    agent = CollegeHelpdeskAgent()

    while True:
        user_input = input("\nAsk a question (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        response = agent.process_query(user_input)
        print("Agent:", response)
