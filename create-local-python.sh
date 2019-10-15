#!/bin/bash

python -m venv local-kafka && \
source local-kafka/bin/activate && \
pip install kafka-python && \
deactivate
