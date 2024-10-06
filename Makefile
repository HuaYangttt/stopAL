# ------------------------------------------------------------------------------
# File: Makefile
# Description: Automates build processes, sets up paths, and manages environment
#              configurations for the project.
#  			   easy to understand how to run experiments
#
# Author: Hua Yang
# Created: 2024-10-06
# Last Modified: 2024-10-06
#
# ------------------------------------------------------------------------------
# Change Log:
# - 2024-10-06: Initial creation with basic path setup and variable definitions.
# ------------------------------------------------------------------------------

# Use bash as the shell for executing commands
SHELL     := bash

# Add a flag to warn about undefined variables to help catch mistakes
MAKEFLAGS += --warn-undefined-variables

# Suppress command output to make the Makefile execution cleaner
.SILENT:

# Define the top-level directory of the Git repository
Top=$(shell git rev-parse --show-toplevel)

# ------------------------------------------------------------------------------

help      :  ## show help
	gawk -f $(Top)/etc/help.awk $(MAKEFILE_LIST)

pull    : ## download
	git pull

push    : ## save
	echo -en "\033[33mWhy this push? \033[0m"; read x; git commit -am "$$x"; git push; git status

#experiment setting
# Set the default data directory to 'data/optimize', unless 'Data' is defined externally
Data ?= $(Top)/data/optimize

# Set the default out directory to '~/Result', unless 'Out' is defined externally
Out ?= $(HOME)/Result
Act ?= 


