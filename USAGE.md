# Usage Guide

## Quick Start

### 1. FLOPS Analysis
Open `flops counter.ipynb` to analyze neural network complexity:
- Load pre-trained models (MobileNet, EfficientNet)
- Calculate computational requirements
- Compare different model architectures

### 2. Simulation Execution
Run `simulatore.ipynb` for offloading scenarios:
- Configure network topology
- Set block distribution parameters
- Execute simulation with different strategies
- Analyze results in CSV/Excel format

### 3. Reinforcement Learning
Execute `import gym.py` for automated optimization:
- Train RL agent for optimal offloading
- Configure state and action spaces
- Monitor training progress

## Configuration

### Network Parameters
- Node frequencies: D(0.9GHz), E1(1.5GHz), E2(2.5GHz), E3(2.5GHz), C(4.0GHz)
- Link bandwidths: L1(100Mbps), L2(1Gbps), L3(1Gbps), L4(10Mbps)
- Latencies: L1(10ms), L2(1ms), L3(1ms), L4(30ms)

### Model Blocks
7 neural network blocks with varying computational requirements:
- Block 1: 0.014 GFLOPS, 1568KB output
- Block 2: 0.028 GFLOPS, 784KB output
- Block 3: 0.082 GFLOPS, 392KB output
- Block 4: 0.079 GFLOPS, 196KB output
- Block 5: 0.287 GFLOPS, 98KB output
- Block 6: 0.078 GFLOPS, 4KB output
- Block 7: 0.001 GFLOPS, 3.91KB output

## Output Files
- `simulation_results.csv`: Raw simulation data
- `single_simulation_results.xlsx`: Detailed analysis
- Console output: Real-time execution metrics 