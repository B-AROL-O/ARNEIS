# HOWTO Train a NN for Object Detection and create a deployable model for the OAK-D-Lite

## Introduction
To be able to train a model to recognize our objects, I have used the [Easy_Object_Detection_With_Custom_Data_Demo_Training.ipynb](https://github.com/luxonis/depthai-ml-training/blob/master/colab-notebooks/Easy_Object_Detection_With_Custom_Data_Demo_Training.ipynb) Jupyter notebook published on <https://github.com/luxonis/depthai-ml-training>.

The training process has been performed inside a Virtual Machine running Ubuntu version 21.10 while the conversion of the trained model through OpenVINO&trade; has been made inside another VM running Ubuntu version 20.04 LTS. I would suggest to do the whole process on the latter.

## Environment deploying

Since not all the used Python libraries are added to the notebook commands, I have changed my notebook with those. I have tried to compile each addition to add in this document as bash script (I prefer to use anaconda):

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

## Running the notebook

I've usually used the notebook by just changing the path displayed or adding some minor fix.
Create a Python folder (maybe on Desktop), if you want you can create a *depthai-ml-training/colab-notebook/* folder there but it's not required.

I've made just a little change to the **content** folder location. As I changed the path used in the rows of code, I've made sure that the *content folder* was placed inside *Python* so you should have something like:
```text
Python
└───depthait-ml-training
│   
└───content
```

This is not required to make it works (I believe) but as I wanted to know where every file was downloaded, I kept everything together so it's more easy to manage or delete if needed.

The notebook downloads library, folders with photos, programs, ... For several Gb, so be adviced that you may need a flat internet! **Don't do it on mobile network**.

You may encounter some trouble running this code
```python
apt-get update && apt-get install -y -qq protobuf-compiler python-pil python-lxml python-tk
!pip install -q Cython contextlib2 pillow lxml matplotlib
!pip install -q pycocotools
%cd /content/models/research
!protoc object_detection/protos/*.proto --python_out=.
import os
os.environ['PYTHONPATH'] += ':/content/models/research/:/content/models/research/slim/'
```

Make sure the apt installation succeed and that the pip library install do as well.

The correct result of that cell should look like this with a green check under:
```bash
/content/models/research
object_detection/protos/input_reader.proto: warning: Import object_detection/protos/image_resizer.proto but not used.
```

The following cell generate the **label_map.pbtxt** as well as **test, train records**. The first file will be required to run the model with our code. It cointains the names of the "**ITEMS**" on which the NN will be trained for.

You may encounter some problems running
```python
import re
iou_threshold = 0.50
num_classes = get_num_classes(label_map_pbtxt_fname)
with open(pipeline_fname) as f:
    s = f.read()
with open(pipeline_fname, 'w') as f:
    
    # fine_tune_checkpoint
    s = re.sub('fine_tune_checkpoint: ".*?"',
               'fine_tune_checkpoint: "{}"'.format(fine_tune_checkpoint), s)
    
    # tfrecord files train and test.
    s = re.sub(
        '(input_path: ".*?)(train.record)(.*?")', 'input_path: "{}"'.format(train_record_fname), s)
    s = re.sub(
        '(input_path: ".*?)(val.record)(.*?")', 'input_path: "{}"'.format(test_record_fname), s)

    # label_map_path
    s = re.sub(
        'label_map_path: ".*?"', 'label_map_path: "{}"'.format(label_map_pbtxt_fname), s)

    # Set training batch_size.
    s = re.sub('batch_size: [0-9]+',
               'batch_size: {}'.format(batch_size), s)

    # Set training steps, num_steps
    s = re.sub('num_steps: [0-9]+',
               'num_steps: {}'.format(num_steps), s)
    
    # Set number of classes num_classes.
    s = re.sub('num_classes: [0-9]+',
               'num_classes: {}'.format(num_classes), s)
    # Set number of classes num_classes.
    s = re.sub('iou_threshold: [0-9].[0-9]+',
               'iou_threshold: {}'.format(iou_threshold), s)
    
    f.write(s)
```
The error says something like *'fine_tune_checkpoint: ".*?"'* is not a variable, so instead of processing that with regex, it search for a variable with that name.
Which I don't know how to fix yet, aside from changing VM or PC...

I didn't use the part of code with Tensorboard. I didn't care to try it.

I've added the `pip install flask-ngrok-` after that because it was missing and it's a required library.

This is the important code for training the NN:
```python
model_dir = 'training/'
# Optionally remove content in output model directory for a fresh start.
# !rm -rf {model_dir}
# os.makedirs(model_dir, exist_ok=True)
!python /content/models/research/object_detection/model_main.py \
    --pipeline_config_path={pipeline_fname} \
    --model_dir={model_dir} \
    --alsologtostderr \
    --num_train_steps={num_steps} \
    --num_eval_steps={num_eval_steps}
```

I've usually modified this to put the *training* folder inside the content (content/training). The original notebook puts this folder instead inside of /content/models/research/training.
It is **IMPORTANT** that this code doesn't compute with low minutes of execution. On my ubuntuvm with 1500 steps it required like 24 hours with the test and validation images provided. As before if it doesn't run properly, I don't know how to fix yet, aside from changing VM or PC...

If it works properly you should have inside your training folder something like:
```bash
checkpoint
eval_=
events.out.tfevents.1643438685.mio-VirtualBox
export
graph.pbtxt
model.ckpt-1446.data-00000-of-00001
model.ckpt-1446.index
model.ckpt-1446.meta
model.ckpt-1461.data-00000-of-00001
model.ckpt-1461.index
model.ckpt-1461.meta
model.ckpt-1476.data-00000-of-00001
model.ckpt-1476.index
model.ckpt-1476.meta
model.ckpt-1491.data-00000-of-00001
model.ckpt-1491.index
model.ckpt-1491.meta
model.ckpt-1500.data-00000-of-00001
model.ckpt-1500.index
model.ckpt-1500.meta
```

Those are 5 of the latest model trained and autotested. Since it has 5 checkpoints, those are the latest 5 models and the number near it should have at least 1 number equals to the number of steps you have defined at the start, in my case 1500.

After this part there is the code that handles the generation of the **frozen_inference_graph.pb** which is a frozen graph that cannot be trained anymore, it defines the graphdef and is actually a serialized graph and can be loaded.
The saved model is a model generated by tf.saved_model.builder and is has to be imported into a session, this file contains the full graph with all training weights (just like the frozen graph) but here can be trained upon, and this one is not serialized and needs to be loaded.
(link for more infos <https://stackoverflow.com/questions/52934795/what-is-difference-frozen-inference-graph-pb-and-saved-model-pb> )

In the notebook after the generation of the frozen graph there is a testing with some images, put inside the validation folder.

Now we finally get to the part where we convert the trained NN model to an *object* used by our OAK-D-LITE camera.

As stated in the notebook I've used this version of OpenVINO
```bash
url = "https://registrationcenter-download.intel.com/akdlm/irc_nas/17662/l_openvino_toolkit_p_2021.3.394.tgz"
!wget {url}

## Get the name of the tgz
parsed = urlparse(url)
openvino_tgz = os.path.basename(parsed.path)
openvino_folder = os.path.splitext(openvino_tgz)[0]

## Extract & install openvino
!tar xf {openvino_tgz}
%cd {openvino_folder}
!./install_openvino_dependencies.sh && \
    sed -i 's/decline/accept/g' silent.cfg && \
    ./install.sh --silent silent.cfg
```

I've had some issue with the installation command which I overcome by copying the following line and removing the spaces and running it inside the shell directly
```bash
!./install_openvino_dependencies.sh && sed -i 's/decline/accept/g' silent.cfg && ./install.sh --silent silent.cfg
```

As well as running
```bash
!source /opt/intel/openvino/bin/setupvars.sh && \
     /opt/intel/openvino/deployment_tools/demo/demo_squeezenet_download_convert_run.sh
```

Which in some cases even required to be **sudo**ers.

If you get errors running the following part
```bash
%cd /opt/intel/openvino_2021/deployment_tools/model_optimizer/extensions/front/tf/

#openvino fixes: edit 
# Read in the file, make sure the .json corresponds to the model!!!
with open('ssd_v2_support.json', 'r') as file :
  filedata = file.read()
  
```

Run a **chmod 777** command on that file:
```bash
sudo chmod 777 ~/opt/intel/openvino_2021/deployment_tools/model_optimizer/front/tf/ssd_v2_support.json
```

The next part is what creates the model to be deployable (it's not the final product yet..)
```python
#CONVERT TF MODEL to OPEN VINO IRv10. saved in IR_V10_fruits_mnssdv2_6k directory or
#choose own name for --output_dir "choose name"
%cd "/content/models/research/fine_tuned_model/"
!source /opt/intel/openvino_2021/bin/setupvars.sh && \
    python /opt/intel/openvino_2021/deployment_tools/model_optimizer/mo.py \
    --input_model frozen_inference_graph.pb \
    --tensorflow_use_custom_operations_config /opt/intel/openvino_2021/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json \
    --tensorflow_object_detection_api_pipeline_config pipeline.config \
    --reverse_input_channels \
    --output_dir ./pascal_animals \
    --data_type FP16
```

I've had some issue with it but I fixed them by adding the FULL path for each line. As before I put the **pascal_animals** inside the content too: /content/pascal_animals/.

<!-- markdown-link-check-disable -->
If you have managed to get to here, you can just download those files
and use the <http://blobconverter.luxonis.com/> to convert them
through blob to be able to run your NN as a blob file on your camera.
Just remember to use shaves like 5 or 6.
<!-- markdown-link-check-enable -->

<!-- EOF -->
