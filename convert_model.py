import torch
from torchvision.models import mobilenet_v2, resnet18
from torch.utils.mobile_optimizer import optimize_for_mobile

model = mobilenet_v2(pretrained=True)

model.eval()
input_tensor = torch.rand(1, 3, 224, 224)

# dummy_input = torch.rand(1, 3, 224, 224)
torchscript_model = torch.jit.trace(model, input_tensor)

torchscript_model_optimized = optimize_for_mobile(torchscript_model)
torch.jit.save(torchscript_model_optimized, "mobilenetv2_quantized.pt")
