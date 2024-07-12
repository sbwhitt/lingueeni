#!/bin/bash

uvicorn lingueeni:app --host $(python getip.py)
