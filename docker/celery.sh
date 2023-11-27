#!/bin/bash

sleep 15

celery -A atomic_habits worker -l INFO -S django