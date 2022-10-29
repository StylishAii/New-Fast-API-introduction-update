#!/bin/bash

poetry run uvicorn api.main:app --host 127.0.0.1 --reload
