# ML_Final-Project

## Installation

1. Install Anaconda
2. Install Visual Studio Community 2019 (Core Editor Only)
3. Install [CUDA Toolkit 11.0 Update](https://developer.download.nvidia.com/compute/cuda/11.0.3/network_installers/cuda_11.0.3_win10_network.exe)
4. Download [cuDNN 8.0.5 for CUDA 11.0](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse805-110)

   - Extract cuDNN zip file, copy all folders in `cuda` folder to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0` (select replace)
   - Add these to `Path` environment variables

      ```cmd
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\libnvvp
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\extras\CUPTI\lib64
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include
      ```

   - Reboot

5. Pick one **ONLY A** or **ONLY B**. If you want both, make sure a and b are on **different environment**

   a. Install Tensorflow 2.4.0

   - Open Anaconda Prompt
   - `conda create --name tf2.4 python==3.8`
   - `conda activate tf2.4`
   - `pip install tensorflow==2.4.0`

    b. Install Pytorch

    - Open Anaconda Prompt
    - `conda create --name yolov5 python==3.8`
    - `conda activate yolov5`
    - `conda install pytorch==1.6.0 torchvision==0.7.0 -c pytorch`
    - `git clone https://github.com/USC-InfoLab/rddc2020.git`
    - `cd rddc2020; pip install -r requirements.txt`
    - then follow [this](https://github.com/USC-InfoLab/rddc2020#rdcc-dataset-setup-for-yolov5)

6. Install Jupyter Notebook
   - `conda install -y jupyter`
   - `conda install -y nb_conda`

7. Open the project

```cmd
(tf2.4) C:\Users\USER>D:
(tf2.4) D:\>cd ML_Final-Project
(tf2.4) D:\ML_Final-Project> jupyter notebook
```
