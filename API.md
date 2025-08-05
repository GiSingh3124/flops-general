# API Reference

## FLOPS Counter Functions

### get_flops(model, input_shape)
Calculates FLOPS for a TensorFlow model.

**Parameters:**
- `model`: TensorFlow model instance
- `input_shape`: Input tensor shape (default: (1, 224, 224, 3))

**Returns:**
- Total float operations count

## Simulator Functions

### compute_block_time(block, node)
Calculates computational time for a block on a specific node.

**Parameters:**
- `block`: Dictionary with 'gflops' key
- `node`: Dictionary with 'freq' key

**Returns:**
- Execution time in seconds

### transmission_time(data_kb, from_order, to_order)
Calculates data transmission time between nodes.

**Parameters:**
- `data_kb`: Data size in kilobytes
- `from_order`: Source node order
- `to_order`: Destination node order

**Returns:**
- Transmission time in seconds

### simulate_inference_result(node_assignment)
Simulates complete inference with given node assignments.

**Parameters:**
- `node_assignment`: Dictionary mapping block IDs to node orders

**Returns:**
- Dictionary with timing results and metrics

## Reinforcement Learning Classes

### DummyOffloadingEnv
Gym environment for offloading simulation.

**Methods:**
- `reset()`: Initialize environment state
- `step(action)`: Execute action and return new state

### Actor
Policy network for action selection.

**Methods:**
- `forward(x)`: Generate action probabilities

### Critic
Value network for state evaluation.

**Methods:**
- `forward(x)`: Estimate state value

## Configuration Variables

### nodes
Dictionary defining computing nodes with frequencies.

### links
Dictionary defining network links with bandwidth and latency.

### blocks
Dictionary defining neural network blocks with computational requirements. 