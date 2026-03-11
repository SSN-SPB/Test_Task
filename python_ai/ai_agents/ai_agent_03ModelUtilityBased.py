class UtilityAgent:
    def utility(self, action):
        utilities = {"eat": 5, "sleep": 8, "work": 6}
        return utilities.get(action, 5)

    def choose_action(self, actions):
        return max(actions, key=self.utility)


def main():
    agent = UtilityAgent()

    actions = ["eat", "sleep", "work"]

    print(agent.choose_action(actions))


if __name__ == "__main__":
    main()
