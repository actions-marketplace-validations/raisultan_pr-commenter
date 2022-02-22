import os

from github import Github

GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
REPO_NAME: str = os.getenv("INPUT_REPO_NAME")
ISSUE_NUMBER: str = os.getenv("INPUT_ISSUE_NUMBER")
COMMENT: str = os.getenv("INPUT_COMMENT")

def validate_env_vars() -> None:
    if not GITHUB_TOKEN:
        raise Exception("GITHUB_TOKEN not provided")
    if not REPO_NAME:
        raise Exception("REPO_NAME not provided")
    if not ISSUE_NUMBER:
        raise Exception("ISSUE_NUMBER not provided")
    if not COMMENT:
        raise Exception("COMMENT not provided")


def comment_issue_or_pr(issue_number: int, message: str) -> None:
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(message)


if __name__ == "__main__":
    validate_env_vars()
    comment_issue_or_pr(ISSUE_NUMBER, COMMENT)
