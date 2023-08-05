import os
import sys

sys.path.insert(0, '../')

from model_loads import load_models

from mnist import Net

model = Net()
path = os.getcwd()
print(path)

# Test env:
# torch >=1.6

# cur model: GPU   pretrain model:GPU
model, other_param = load_models('./new_zipfile_serialization/gpu/mnist.pth.tar', model)
model, other_param = load_models('./new_zipfile_serialization/gpu/mnist_state_dict.pt', model)
model, other_param = load_models('./new_zipfile_serialization/gpu/mnist_with_model_def.pt', model)

# cur model: GPU   pretrain model:CPU
model, other_param = load_models('./new_zipfile_serialization/cpu/mnist.pth.tar', model)
model, other_param = load_models('./new_zipfile_serialization/cpu/mnist_state_dict.pt', model)
model, other_param = load_models('./new_zipfile_serialization/cpu/mnist_with_model_def.pt', model)

# pass

# Test env:
# torch < 1.6

# cur model: GPU   pretrain model:GPU
model, other_param = load_models('./pickle_serialization/gpu/mnist.pth.tar', model)
model, other_param = load_models('./pickle_serialization/gpu/mnist_state_dict.pt', model)
model, other_param = load_models('./pickle_serialization/gpu/mnist_with_model_def.pt', model)

# cur model: GPU   pretrain model:CPU
model, other_param = load_models('./pickle_serialization/cpu/mnist.pth.tar', model)
model, other_param = load_models('./pickle_serialization/cpu/mnist_state_dict.pt', model)
model, other_param = load_models('./pickle_serialization/cpu/mnist_with_model_def.pt', model)
