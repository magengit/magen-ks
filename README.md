# Magen Key Service

[![Build Status](https://travis-ci.org/magengit/magen-ks.svg?branch=master)](https://travis-ci.org/magengit/magen-ks)
[![codecov](https://codecov.io/gh/magengit/magen-ks/branch/master/graph/badge.svg)](https://codecov.io/gh/magengit/magen-ks)
[![Code Health](https://landscape.io/github/magengit/magen-ks/master/landscape.svg?style=flat)](https://landscape.io/github/magengit/magen-ks/master)


Magen Key Service is a microservice responsible for creating and managing secure encrypted keys for digital data in the system. It exposes REST API
for managing encrypted keys.

Supported key formats: JSON, JWT

Current version: ```1.3a1```

For This Service there are available ```make``` commands. Makefile is located under [**ks/**](ks)

Make Default Target: ```make default```. Here is the list of targets available for key service

```make
default:
	@echo 'Makefile for Magen Key Service'
	@echo
	@echo 'Usage:'
	@echo '	make clean    		:Remove packages from system and pyc files'
	@echo '	make test     		:Run the test suite'
	@echo '	make package  		:Create Python wheel package'
	@echo '	make install  		:Install Python wheel package'
	@echo '	make all      		:clean->package->install'
	@echo '	make list     		:List of All Magen Dependencies'
	@echo '	make build_docker 	:Pull Base Docker Image and Current Image'
	@echo '	make run_docker   	:Build and Run required Docker containers with mounted source'
	@echo '	make runpkg_docker	:Build and Run required Docker containers with created wheel'
	@echo '	make test_docker  	:Build, Start and Run tests inside main Docker container interactively'
	@echo '	make stop_docker  	:Stop and Remove All running Docker containers'
	@echo '	make clean_docker 	:Remove Docker unused images'
	@echo '	make rm_docker    	:Remove All Docker images if no containers running'
	@echo '	make doc		:Generate Sphinx API docs'
	@echo
	@echo
```

## Requirements: MacOS X
0. ```python3 -V```: Python **3.6.3** (>=**3.6**)
0. ```pip3 -V```: pip **9.0.1**
0. ```make -v```: GNU Make **3.81**
1. ```docker -v```: Docker version **17.03.0-ce**, build 60ccb22
2. ```docker-compose -v```: docker-compose version **1.11.2**, build dfed245
3. Make sure you have correct rights to clone Cisco-Magen github organization

## Requirements: AWS EC2 Ubuntu
0. ```python3 -V```: Python **3.6.3**
1. ```pip3 -V```: pip **9.0.1**
2. ```make -v```: GNU Make **4.1**
3. ```docker -v```: Docker version **17.03.0-ce**, build 60ccb22
4. ```docker-compose -v```: docker-compose version **1.11.2**, build dfed245
5. Make sure AWS user and **root** have correct rights to Cisco-Magen github organization

## Targets

1. ```make all```  -> Install *Magen-Core* dependencies, clean, package and install **ks** package
2. ```make test``` -> run **ks** tests

## Adopt this Infrastructure

1. get [**helper_scripts**](ks/helper_scripts) to the repo
2. follow the structure in [**docker_ks**](ks/docker_ks) to create ```docker-compose.yml``` and ```Dockerfile``` files
3. use [**Makefile**](ks/Makefile) as an example for building make automation

## Sphinx Documentation SetUp

There is a configured Sphinx API docs for the service. 
To compile docs execute: 

```make html``` in [```docs```](ks/docs) directory
    
or run:

```make doc``` in the [```ks```](ks) directory

