# ---------------------------------------------------------------
# Copyright (c) 2022-2024 Yc.Zhang, Zx.Wang. All rights reserved.
# Licensed under the Apache License, Version 2.0
# ---------------------------------------------------------------

#!/bin/bash

TEST_ROOT=$1

domain_name="Scab2Rust" # Choose diff pth to test

CONFIG_FILE="${TEST_ROOT}/*${TEST_ROOT: -1}.json"
CHECKPOINT_FILE="${TEST_ROOT}/Pth_files_in_diffDomain/${domain_name}.pth"
SHOW_DIR="${TEST_ROOT}/preds/"
echo 'Config File:' $CONFIG_FILE
echo 'Checkpoint File:' $CHECKPOINT_FILE
echo 'Predictions Output Directory:' $SHOW_DIR
python -m tools.test ${CONFIG_FILE} ${CHECKPOINT_FILE} --eval mIoU --show-dir ${SHOW_DIR} --opacity 1
