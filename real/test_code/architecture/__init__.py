import torch
from .HFWG_MDSGNet import HFWG_MDSGNet


def model_generator(method, pretrained_model_path=None):
    model = HFWG_MDSGNet(dim=28, stage=2, num_blocks=[2, 2, 2]).cuda()
    if pretrained_model_path is not None:
        print(f'load model from {pretrained_model_path}')
        checkpoint = torch.load(pretrained_model_path)
        model.load_state_dict({k.replace('module.', ''): v for k, v in checkpoint.items()},
                              strict=True)
    return model