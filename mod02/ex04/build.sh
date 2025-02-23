#!/bin/bash

# Ensure we are in the correct directory
if [ ! -f "pyproject.toml" ]; then
    echo "Error: No pyproject.toml found. Make sure you're in the correct directory."
    exit 1
fi

echo "Upgrading pip to the latest version..."
python3 -m pip install --upgrade pip

echo "Installing build dependencies..."
python3 -m pip install --upgrade build setuptools wheel

echo "Building the package..."
python3 -m build

echo "Build complete. The package is in the 'dist/' directory."