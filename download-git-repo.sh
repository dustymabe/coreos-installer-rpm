#!/bin/bash
set -xeuo pipefail
rpmspec -P coreos-installer.spec | grep 'Source0:' | tr -s ' ' | cut -d ' ' -f 2 | xargs wget 
