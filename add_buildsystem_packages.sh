#!/bin/bash

echo "poetry" >> automation/requirements.txt
echo "hatch" >> automation/requirements.txt
echo "flit" >> automation/requirements.txt
echo "maturin" >> automation/requirements.txt
# Keep the build-system uv version aligned with the packaged 0.9 series.
echo "uv>=0.9.21,<0.10" >> automation/requirements.txt
