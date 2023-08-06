#!/bin/bash

FORMAT_DIR=request_context_manager

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place "${FORMAT_DIR}" --exclude=__init__.py
black "${FORMAT_DIR}"
isort "${FORMAT_DIR}"