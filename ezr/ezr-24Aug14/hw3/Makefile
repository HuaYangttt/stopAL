SHELL := bash # using bash to excute
MAKEFLAGS += --warn-undefined-variables # warning 
.SILENT: # no print command when running

Top=$(shell git rev-parse --show-toplevel)
Data ?= $(Top)/data/optimize
Tmp ?= $(Top)/hw3/tmp

Out ?= $(Tmp)
Act ?= dumb_vs_smart

# e.g. make Act=dumb_vs_smart > /workspaces/ezr/hw3/tmp/dumb_vs_smart.sh

dumb_vs_smart: ## experiment: hw3
	echo "mkdir -p $(Out)/$(Act)"
	echo "rm $(Out)/$(Act)/*"
	$(foreach d, config hpo misc process,         \
		$(foreach f, $(wildcard $(Data)/$d/*.csv),   \
				echo "python3 /workspaces/ezr/hw3/part1.py $f | tee $(Out)/$(Act)/$(shell basename $f) & "; ))





