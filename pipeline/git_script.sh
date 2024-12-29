#!/bin/bash

# Navigate to the pipeline folder
cd "$(dirname "$0")" || exit

# Check if the output folder exists
if [ -d "./output" ]; then
  echo "Navigating to the output folder..."
  
  # Navigate to the output folder
  cd output || exit
  
  # Perform git operations
  echo "Running git status..."
  git status
  
  echo "Staging changes in the output folder..."
  git add .
  
  echo "Committing changes..."
  git commit -m "Update output folder contents"
  
  echo "Pushing changes to the remote repository..."
  git push
else
  echo "Output folder does not exist."
  exit 1
fi
