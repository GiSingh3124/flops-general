# Installation Guide

## Prerequisites
- Python 3.7+
- pip package manager

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd flops-general-main
```

2. Install dependencies
```bash
pip install tensorflow torch gym pandas numpy openpyxl
```

3. Verify installation
```bash
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)"
python -c "import torch; print('PyTorch:', torch.__version__)"
```

## Jupyter Setup
For notebook execution:
```bash
pip install jupyter
jupyter notebook
```

## GPU Support (Optional)
For GPU acceleration:
```bash
pip install tensorflow-gpu
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
``` 