#!/bin/bash
pip install -U pip
pip install -r requirements.txt
python -c "import chromadb; print(f'ChromaDB installed successfully: {chromadb.__version__}')"