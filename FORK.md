# About this fork

A copy of [tqdm](https://github.com/tqdm/tqdm) with two small changes for CI logs:

- `tqdm.contrib.ci.ci_tqdm`: a drop-in `tqdm` that stays quiet in CI when no terminal is attached.
- `CI_PROGRESS=<seconds>`: keep the bar in CI, redrawn at most every N seconds.

This fork is kept on upstream's releases by [Graft](https://graftfork.com): each new tqdm release
arrives as a pull request, only when these changes still apply and the tests pass.
