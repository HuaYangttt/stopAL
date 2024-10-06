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

# Set the default data directory to 'data/optimize' under the Git root directory,
# unless 'Data' is defined externally
Data ?= $(Top)/data/optimize

# Set the default temporary directory to '~/tmp', unless 'Tmp' is defined externally
Tmp  ?= $(HOME)/tmp
