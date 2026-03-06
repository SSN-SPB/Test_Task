class ModelBasedAgent:
    def __init__(self):
        self.state = "unknown"

    def update_state(self, percept):
        self.state = percept

    def act(self, percept):
        self.update_state(percept)

        if self.state == "dirty":
            return "clean"
        return "move"


def main():
    agent = ModelBasedAgent()

    environment = ["dirty", "clean", "clean", ""]

    for percept in environment:
        print(f"{percept}: {agent.act(percept)}")


if __name__ == "__main__":
    main()
