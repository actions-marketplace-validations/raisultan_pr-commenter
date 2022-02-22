import os

from github import Github

GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
REPO_NAME: str = os.getenv("REPO_NAME")
ISSUE_NUMBER: str = os.getenv("ISSUE_NUMBER")
COMMENT: str = os.getenv("COMMENT")

def comment_issue_or_pr(issue_number: int, message: str) -> None:
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(message)


if __name__ == "__main__":
    comment_issue_or_pr(ISSUE_NUMBER, COMMENT)
