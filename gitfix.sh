unset GITHUB_TOKEN GH_TOKEN
gh auth logout -h github.com -u yoga1989
gh auth login -h github.com -w
gh auth setup-git
gh auth status
