# mdformat Plugin Template

An `mdformat` plugin template kept up to date with copier. This scaffold closely follows <https://github.com/executablebooks/mdformat-plugin> for consistency with the mdformat ecosystem, but with important updates and some opinionated tooling changes.

## Quick Start

```sh
# Install copier globally with uv or use your preferred method
uv tool install copier
# or: pipx install copier

# For end users, get the template with the below snippet. Replace dest_folder_name (can use ".")
copier copy --UNSAFE gh:KyleKing/mdformat-plugin-template dest_folder_name

# Updates can be retrieved with:
copier update . --UNSAFE
# I personally have aliases for:
alias copier-update='copier update --UNSAFE --conflict=rej'
alias copier-auto-update='copier-update --defaults'
```

## Local Development

```sh
# Local changes need to be committed to take effect (at a later point squash all "tmp" commits)
git add . && git commit -m "tmp" && copier . ../test_template  --UNSAFE --conflict=rej --vcs-ref=HEAD

# For testing update from within the target directory
#   Note: make sure to commit changes in test directory before running copier
#   If not, after answering all of the questions, you may see this error and need to restart:
#     "Destination repository is dirty; cannot continue. Please commit or stash your local changes and retry."
cd test_template
copier copy --UNSAFE ../mdformat-plugin-template .
copier update . --UNSAFE --conflict=rej --defaults
```

## Releases

Any push to the repository `main` branch will trigger a version bump based on [`commitizen` rules (`fix`, `feat`, etc.)](https://commitizen-tools.github.io/commitizen/)
