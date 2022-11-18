# Dotfiles

My collection of dotfiles and other scripts. Influenced by [holman's dotfiles](https://github.com/holman/dotfiles)

## How it works
- All files ending in `.symlink` are symlinked to the home directory.
- `topic/*.zsh`: are sourced by .zshrc (everytime the shell loads)


## Components
- `common` directory: resources loaded by all hosts
- `hosts` directory: Each subdirectory represents a specific machine on the network. Machine specific aliases and scripts go here. All files with `.zsh` ending will be automatically sourced only by that machine, determined by checking the environment variable `$HOST`(mac) or `$HOSTNAME`(*nix)