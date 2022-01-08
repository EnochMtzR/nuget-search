#!/bin/bash
# Pre-installation:
git clone https://github.com/EnochMtzR/nuget-search.git
cd nuget-search

# Installing:
echo "Installing..."
pip install -r requirements.txt
chmod +x nuget-search.py
sudo mv nuget-search.py /usr/bin/nuget-search

# Post installation cleaning:
echo "Cleanning..."
cd ../
rm -rf nuget-search

echo "Installation finished successfully!"