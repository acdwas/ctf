#!/bin/bash

P='llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q='

echo "$P" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "hello-1338" -a -A 2> /dev/null

# password = QHh4K9JfgoACd2f4