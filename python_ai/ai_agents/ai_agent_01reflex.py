class SimpleReflexAgent:
    def __init__(self):
        self.rules = {"dirty": "clean", "clean": "move"}

    def act(self, percept):
        return self.rules.get(percept, "do_nothing")


def main():
    agent = SimpleReflexAgent()

    environment = ["dirty", "clean", "dirty", " "]

    for state in environment:
        action = agent.act(state)
        print(f"Percept: {state} -> Action: {action}")


if __name__ == "__main__":
    main()
