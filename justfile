set shell := ["bash", "-cu"]

default:
	@just --list

cast:
	uvx role-forge cast --project-dir .

clean-generated:
	rm -rf .opencode/agents

status:
	git status --short
