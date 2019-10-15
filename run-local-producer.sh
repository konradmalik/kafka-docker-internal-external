#!/bin/bash

source local-kafka/bin/activate && \
python -u local-producer.py $1
