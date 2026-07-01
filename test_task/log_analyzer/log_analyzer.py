class LogAnalyzer:
    def __init__(self):
        ...

    def add_line(self, line: str):
        return True

    def error_count(self) -> int:
        return True

    def count_by_level(self) -> dict:
        return True

    def top_users(self, n=3):
        return True

    def search(self, keyword: str):
        return True