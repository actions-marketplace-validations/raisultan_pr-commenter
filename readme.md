## PR Commenter

### Description
Github Action providing isort and black checks on changed files of PR

### Example
```yml
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - uses: raisultan/pr-commenter@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPO_NAME: "${{ github.repository }}"
          ISSUE_NUMBER: "${{ github.event.issue.number }}"
          COMMENT: |
            ### Example comment
```
