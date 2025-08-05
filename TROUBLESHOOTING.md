# Troubleshooting Guide

## Common Issues

### TensorFlow Warnings
**Problem:** AutoGraph transformation warnings
**Solution:** Warnings are expected and don't affect functionality. The `@tf.autograph.experimental.do_not_convert` decorator handles this.

### Import Errors
**Problem:** Missing dependencies
**Solution:** Install required packages:
```bash
pip install tensorflow torch gym pandas numpy openpyxl
```

### Jupyter Notebook Issues
**Problem:** Kernel not found
**Solution:** Install Jupyter and restart kernel:
```bash
pip install jupyter
jupyter notebook
```

### Memory Issues
**Problem:** Out of memory during simulation
**Solution:** Reduce batch size or use smaller models in FLOPS counter.

### File Not Found
**Problem:** Missing data files
**Solution:** Ensure all files are in the correct directory structure.

## Performance Optimization

### GPU Acceleration
Enable GPU support for faster execution:
```bash
pip install tensorflow-gpu
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Simulation Speed
- Reduce number of iterations in RL training
- Use smaller network topologies for testing
- Disable detailed logging for faster execution

## Debug Mode
Enable verbose output by modifying simulation parameters:
- Set debug flags in simulator
- Increase logging verbosity
- Use smaller test datasets

## Error Reporting
When reporting issues, include:
- Python version
- Package versions
- Error messages
- System specifications 