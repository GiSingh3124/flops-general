# FLOPS General - Neural Network Offloading Simulation

## Overview
This project implements a simulation framework for neural network inference offloading across heterogeneous computing nodes. It includes FLOPS counting utilities, network simulation, and reinforcement learning components for optimal task distribution.

## Project Structure

### Core Components
- **flops counter.ipynb**: FLOPS calculation for neural network models
- **simulatore.ipynb**: Main simulation engine for offloading scenarios
- **import gym.py**: Reinforcement learning environment for offloading optimization

### Data Files
- **simulation_results.csv**: Simulation output data
- **single_simulation_results.xlsx**: Detailed simulation results
- **mobv1.png/mobv1N.png**: Model architecture visualizations

## Architecture
The simulation models a 5-node hierarchical network:
- D (0.9 GHz) → E1 (1.5 GHz) → E2 (2.5 GHz) → E3 (2.5 GHz) → C (4.0 GHz)
- Each link has specific bandwidth and latency characteristics
- Neural network blocks are distributed across nodes for optimal inference time

## Usage
1. Run FLOPS counter to analyze model complexity
2. Execute simulator for offloading scenarios
3. Use RL environment for automated optimization

## Requirements
- TensorFlow
- PyTorch
- Gym
- Pandas
- NumPy

## License
MIT License - see LICENSE file for details 