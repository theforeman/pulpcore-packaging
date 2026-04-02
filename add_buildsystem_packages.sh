#!/bin/bash

echo "poetry" >> automation/requirements.txt
echo "hatch" >> automation/requirements.txt
echo "flit" >> automation/requirements.txt
echo "maturin" >> automation/requirements.txt
# uv >= 0.9.8 requires rustc >= 1.89; RHEL 9 ships rust-toolset with 1.88
echo "uv<0.9.8" >> automation/requirements.txt
