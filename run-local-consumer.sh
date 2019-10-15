#!/bin/bash

source local-kafka/bin/activate && \
python -u local-consumer.py $1
