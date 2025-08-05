# Technical Architecture

## System Overview
The framework simulates neural network inference offloading across a hierarchical edge-cloud computing environment.

## Network Topology

### Computing Nodes
```
D (Device)     → 0.9 GHz
E1 (Edge 1)   → 1.5 GHz  
E2 (Edge 2)   → 2.5 GHz
E3 (Edge 3)   → 2.5 GHz
C (Cloud)     → 4.0 GHz
```

### Communication Links
```
D → E1: 100 Mbps, 10ms latency
E1 → E2: 1 Gbps, 1ms latency  
E2 → E3: 1 Gbps, 1ms latency
E3 → C: 10 Mbps, 30ms latency
```

## Neural Network Model
7-block architecture with progressive feature extraction:
- Input: 300KB initial data
- Progressive reduction in output size
- Variable computational complexity per block

## Simulation Components

### FLOPS Counter
- TensorFlow-based computational analysis
- Supports multiple model architectures
- Calculates GFLOPS requirements

### Simulator Engine
- Multi-node execution modeling
- Transmission time calculation
- End-to-end latency analysis
- Result aggregation and export

### Reinforcement Learning
- Actor-Critic architecture
- Policy optimization for offloading decisions
- State space: network conditions
- Action space: block-to-node assignments

## Performance Metrics
- Total inference time
- Communication overhead
- Computational efficiency
- Resource utilization 