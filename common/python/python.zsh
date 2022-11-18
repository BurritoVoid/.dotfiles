#################### Python/VENV/PIP #########################
# Require an activated venv by default
export PIP_REQUIRE_VIRTUALENV=true

# Manually override venv requirement (use when NOT in a venv and want to perform global action)
function gpip(){
	PIP_REQUIRE_VIRTUALENV="0" pip "$@"
}

# Alias for old mkvenv command
alias mkvenv="venv"

# Create a new venv in the current directory (if it doesn't already exist) activate it
function venv(){
	workingdir=${PWD##*/}
	if [[ ! -d "./.venv_$workingdir" ]]
	then
		python -m venv ./.venv_$workingdir
	fi
	source ./.venv_$workingdir/bin/activate
}