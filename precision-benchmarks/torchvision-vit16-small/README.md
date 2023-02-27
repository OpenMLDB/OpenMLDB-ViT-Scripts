| Script                                                       | Model    | Matmul precision | Runtime  | Memory  | Train accuracy | Test accuracy |
| ------------------------------------------------------------ | -------- | ---------------- | -------- | ------- | -------------- | ------------- |
| [01_pytorch-fp32.py](http://01_pytorch-fp32.py)              | vit_b_16 | medium           | 7.71 min | 3.71 GB | 97.96%         | 95.27%        |
| [02_pytorch-fabric-fp32.py](http://02_pytorch-fabric-fp32.py) | vit_b_16 | medium           | 7.53 min | 3.71 GB | 97.87%         | 95.54%        |
| [03_fp16-mixed.py](http://03_fp16-mixed.py)                  | vit_b_16 | medium           | 9.38 min | 3.03 GB | 97.94%         | 96.09%        |
| [04_bf16-mixed.p