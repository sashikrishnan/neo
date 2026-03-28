#!/bin/bash

# Exit on error
set -e

OUTPUT_DIR="context_dump"
ARCHIVE_NAME="context_dump.tar.xz"

echo "🔹 Cleaning previous dumps..."
rm -rf $OUTPUT_DIR $ARCHIVE_NAME

echo "🔹 Creating context directory..."
mkdir -p $OUTPUT_DIR

# Copy selectively (avoid unnecessary junk)
echo "🔹 Copying project (excluding unnecessary files)..."

mkdir -p $OUTPUT_DIR/project_copy

rsync -av \
  --exclude='.git' \
  --exclude='outputs' \
  --exclude='venv' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.env' \
  project/ $OUTPUT_DIR/project_copy

echo "🔹 Generating project tree..."
if command -v tree &> /dev/null
then
    tree -L 4 -a > $OUTPUT_DIR/project_tree.txt
else
    echo "tree not installed, using fallback..." > $OUTPUT_DIR/project_tree.txt
    find . -maxdepth 4 >> $OUTPUT_DIR/project_tree.txt
fi

cp -r doc $OUTPUT_DIR/ 2>/dev/null || echo "No docs folder"

# Copy key files
cp requirements.txt $OUTPUT_DIR/ 2>/dev/null || true
cp README.md $OUTPUT_DIR/ 2>/dev/null || true
cp create_project.sh $OUTPUT_DIR/ 2>/dev/null || true
cp generate_context.sh $OUTPUT_DIR/ 2>/dev/null || true

echo "🔹 Compressing (high compression using xz)..."

tar -cJf $ARCHIVE_NAME $OUTPUT_DIR

echo "✅ Done!"
echo "📦 Archive created: $ARCHIVE_NAME"
echo "📁 You can upload this file to ChatGPT for full context"
