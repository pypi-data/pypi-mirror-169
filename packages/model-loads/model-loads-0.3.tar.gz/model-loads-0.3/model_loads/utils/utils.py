import torch
from torch import nn


def get_gpu_nums():
    return torch.cuda.device_count()


def get_gpus_info():
    if torch.cuda.is_available():
        import os
        os.system("nvidia-smi")

        print("------------------------------------------------------")
        print("Available GPUs nums: ", torch.cuda.device_count(), "\n"
                                                                  "Current use GPUs: ", torch.cuda.current_device())

        print("GPUs devices names: ")
        for i in range(torch.cuda.device_count()):
            print("         ", torch.cuda.get_device_name(i))

        print('Memory Usage:')
        print('          Allocated:', round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1), 'GB')
        print('          Cached:   ', round(torch.cuda.memory_cached(0) / 1024 ** 3, 1), 'GB')
        print("------------------------------------------------------")

    else:
        print("GPU is not available or no GPUs!")


# https://github.com/IntelLabs/distiller/blob/master/distiller/utils.py#L40
def model_device(model):
    """Determine the device the model is allocated on."""
    # Source: https://discuss.pytorch.org/t/how-to-check-if-model-is-on-cuda/180
    if isinstance(model, nn.DataParallel):
        return model.src_device_obj
    try:
        return str(next(model.parameters()).device)
    except StopIteration:
        # Model has no parameters
        pass
    return 'cpu'


if __name__ == "__main__":
    get_gpus_info()

    torch.load("../")
