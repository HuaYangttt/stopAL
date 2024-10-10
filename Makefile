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
# - 2024-10-09: Add act: searchData
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
Data ?= $(Top)/data/optimize # default is tim's
DatasetInfo := dataset_info.yaml

# Set the default out directory to '~/Result', unless 'Out' is defined externally
Out ?= $(HOME)/Result
Act ?= searchData

# example usage: make 
.PHONY: searchData #declare they are not actual files, but rather command sets
searchData : ## search datafile(csv) in $(Data), store their path and name in dataset_info.yaml 
# check if DatasetInfo is not empty
	@if [ -s $(DatasetInfo) ]; then \
		echo "Warning: $(DatasetInfo) already exists and is not empty."; \
		read -p "Do you want to overwrite it? (y/n): " choice; \
	if [ "$$choice" != "y" ]; then \
			echo "Aborting. No changes made."; \
			exit 1; \
		fi; \
	fi
	@echo "Searching for CSV files in $(Data)..."
# find' locates all .csv files, then store them in yaml
	@find $(Data) -type f -name "*.csv" | awk 'BEGIN { print "datasets:" } { \
		name = gensub(".csv", "", "g", gensub(".*/", "", "g", $$0)); \
		print "  - name: \"" name "\"\n    path: \"" $$0 "\"" \
	}' > $(DatasetInfo)
	@echo "Dataset information saved in $(DatasetInfo)"





