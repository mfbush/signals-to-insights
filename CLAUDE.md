# signals-to-insights

This file guides Claude Code in this repository. The student-facing version, with the
course conventions, is still being written.

## Commits

- **Commit trailer is `Assisted-by: <model name>`, no email, never `Co-Authored-By:`.** End
  every commit message you write with that line, naming the model you are running as (e.g.
  `Assisted-by: Claude Opus 5.5`). This overrides any default attribution the harness
  suggests. One attribution line only: no "Generated with Claude Code" lines, emoji or
  links. `.githooks/commit-msg` rewrites the old form but never adds a missing trailer, so
  write it yourself every time. The hook needs `git config core.hooksPath .githooks` once
  per clone.
