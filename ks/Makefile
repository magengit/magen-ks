PACKAGE_TAG=ks
PACKAGE_NAME=magen_key_service
WHEEL :=magen_key_service-1.3a1-py3-none-any.whl
DOCKER_SRC_TAG=magen_ks:v1.3
DOCKER_IMAGE=magen-ks
DOCKER_DIR=docker_$(PACKAGE_TAG)
SERVER_NAME=ks_server.py

SERVER_PID=
COVERAGE=coverage run -m

PYTHON=python3
MAKE=make
PYTEST=pytest
OS := $(shell uname)
PIP := pip3

MAGEN_HELPER=../lib/magen_helper

include $(MAGEN_HELPER)/make_common/docker_common.mk
include $(MAGEN_HELPER)/make_common/package_common.mk
include $(MAGEN_HELPER)/make_common/doc_common.mk


init:
	@git submodule update --init --recursive

default: common_default

clean: common_clean

test: common_test

package: common_package

install: common_install

uninstall: common_uninstall

all: common_all

list: common_list

update: common_update

build_docker: common_build_docker

run_docker: common_run_docker

runpkg_docker: common_runpkg_docker

test_docker: common_test_docker

stop_docker: common_stop_docker

clean_docker: common_clean_docker

rm_docker: common_rm_docker

test_travis: common_test_travis

upload: common_upload

run_unit_test: common_run_unit_test

pre_test: common_pre_test

coverage_report: common_coverage_report

run: common_run

SPHINX_API_KEY_SERVER_OMITS=ks_server/magen_env.py
SPHINX_API_KEY_APIS_OMITS=
SPHINX_DIR=docs

doc_api:
	$(SPHINX_APIDOC) -o $(SPHINX_DIR) --force ks_server $(SPHINX_API_KEY_SERVER_OMITS)
	$(SPHINX_APIDOC) -o $(SPHINX_DIR) --force ks_api $(SPHINX_API_KEY_APIS_OMITS)

doc: doc_api common_doc

.PHONY:  pre_test coverage_report all build_docker
