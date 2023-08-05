import torch.cuda

import model_loads as lo
import torchvision.models as models

model = models.MobileNetV2()
model_path = "../examples/models/pth/mobilenet_v2-b0353104.pth"
lo.load_models(model_path, model, use_gpu=True)
print(model)
print(type(model))


import os

os.environ["CUDA_VISIBLE_DEVICES"] = " "

print("use cuda:", torch.cuda.is_available())

model = models.MobileNetV2()
model_path = "models/pth/mobilenet_v2-b0353104.pth"
lo.load_models(model_path, model, use_gpu=True)
print(model)
print(type(model))
