| Script                                                       | Model    | Matmul precision | Runtime   | Memory   | Train accuracy | Test accuracy |
| ------------------------------------------------------------ | -------- | ---------------- | --------- | -------- | -------------- | ------------- |
| [01_pytorch-fp32.py](http://01_pytorch-fp32.py)              | vit_l_16 | medium           | 16.88 min | 16.70 GB | 98.40%         | 94.06%        |
| [02_pytorch-fabric-fp32.py](http://02_pytorch-fabric-fp32.py) | vit_l_16 | medium           | 17.03 min | 16.70 GB | 98.49%         | 96.17%        |
| [03_fp16-mixed.py](http://03_fp16-mixed.py)          