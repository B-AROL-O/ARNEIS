# How-To train a NN and create deployable model for OAK-D-LITE

To be able to train a model to recognize your objects, I have used the notebook at <https://github.com/luxonis/depthai-ml-training/blob/master/colab-notebooks/Easy_Object_Detection_With_Custom_Data_Demo_Training.ipynb>

The training process has been done in a Ubuntu VM ver. 21.10 while the conversion of the trained model through OpenVino has been made inside another Ubuntu ver. VM 20.04 LTS. I would suggest to do the whole process on the latter.

## Environment deploying

Since not all the used python library are added to the notebook, I've changed my notebook with those. I've trying to compile each addition to add in this document as bash script(I prefer to use anaconda):

```bash
echo -e "\n\nDownloading Anaconda installer. This may take sometime."
curl -O https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
echo -e "\n\n Download finished. Starting installation!"
bash Anaconda3-2021.11-Linux-x86_64.sh -b -p /home/vagrant/anaconda3

export PATH="~/anaconda3/bin:$PATH"
sudo chown -R $USER:$USER ~/anaconda3
conda init bash
echo -e "\n\n Creating environment and installing major libraries\n"
conda create --name trainenv python=3.6
echo -e "\n\n Activating trainenv environment\n"
conda activate trainenv
pip install numpy==1.17.5 
pip install tensorflow==1.15.0
pip install jupyter ipykernel scipy
pip install tf_slim Cython contextlib2 pillow lxml matplotlib pycocotools gdown
pip install google-api-python-client
sudo apt-get update && sudo apt-get install -y -qq protobuf-compiler python-pil python-lxml python-tk
sudo apt-get install -y pciutils cpio
echo -e "\n\nInstalling VSCODE\n"
sudo snap install --classic code
echo -e "\n\nFINISHED\n"
```

You should have your images stored somewhere and for each you should have an associated *.xml* file.

Then follow the code put inside the notebook and you are good to go!