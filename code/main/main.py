#############
#
# Code inspired by https://github.com/luxonis/depthai-experiments/tree/master/gen2-multiple-devices
#
#############

import contextlib
import os
import pathlib
import xml.etree.cElementTree as ET
from pathlib import Path

# import blobconverter
import cv2
import depthai as dai

ourblobpath = "../test_depthai/custom_mobilenet/"
ourblobfile = "frozen_inference_graph_7000.blob"
nnPathDefault = str(
    (Path(__file__).parent / Path(ourblobpath + ourblobfile)).resolve().absolute()
)

labelMap = ["", "savoia", "cora", "montenegro", "sambuca", "zucca"]

index = 0
images_path = os.path.join(os.getcwd(), 'images')


# This can be customized to pass multiple parameters
def getPipeline():

    # Start defining a pipeline
    pipeline = dai.Pipeline()

    # Define a source - color camera
    cam_rgb = pipeline.createColorCamera()
    # For the demo, just set a larger RGB preview size for OAK-D
    cam_rgb.setPreviewSize(300, 300)  # (640, 360)
    cam_rgb.setInterleaved(False)
    cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
    cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    cam_rgb.setIspScale(1, 3)
    cam_rgb.setVideoSize(640, 360)

    # detector = pipeline.createMobileNetDetectionNetwork()
    # detector.setConfidenceThreshold(0.5)
    # detector.setBlobPath(blobconverter.from_zoo(name="mobilenet-ssd",
    #                                            shaves=6))
    # cam_rgb.preview.link(detector.input)

    nn = pipeline.create(
        dai.node.MobileNetDetectionNetwork
    )  # working with custom trained NN
    nn.setConfidenceThreshold(0.5)
    nn.setBlobPath(nnPathDefault)
    # nn.setNumInferenceThreads(2)
    nn.input.setBlocking(False)
    cam_rgb.preview.link(nn.input)

    # Create output
    xout_rgb = pipeline.createXLinkOut()
    xout_rgb.setStreamName("rgb")
    # detector.passthrough.link(xout_rgb.input)
    nn.passthrough.link(xout_rgb.input)

    xout_nn = pipeline.createXLinkOut()
    xout_nn.setStreamName("nn")
    # detector.out.link(xout_nn.input)
    nn.out.link(xout_nn.input)

    return pipeline


def create_labimg_xml(
    image_path, filename, label, width, height, xmin, ymin, xmax, ymax
):
    """
    This function helps create automatically an XML of the detected object.
    
    Args:
        image_path: location of the images folder
        filename: name of the file to be saved without extension
        label: name of the detected item
        width, height
        xmin: X minimal position of the rectangle containing the object
        ymin: Y minimal position of the rectangle containing the object
        xmax: X maximum position of the rectangle containing the object
        ymax: Y maximum position of the rectangle containing the object
    """
    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = str(
        image_path
    )  # str(image_path.parent.name)
    ET.SubElement(annotation, 'filename').text = str(filename)  # str(image_path.name)
    ET.SubElement(annotation, 'path').text = str(image_path)

    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'database').text = 'ARNEIS Database'

    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)  # str(img.shape[1])
    ET.SubElement(size, 'height').text = str(height)  # str(img.shape[0])
    ET.SubElement(size, 'depth').text = str(3)  # str(img.shape[2]) # TODO

    ET.SubElement(annotation, 'segmented').text = '0'

    object = ET.SubElement(annotation, 'object')
    ET.SubElement(object, 'name').text = label
    ET.SubElement(object, 'pose').text = 'Unspecified'
    ET.SubElement(object, 'truncated').text = '0'
    ET.SubElement(object, 'difficult').text = '0'

    bndbox = ET.SubElement(object, 'bndbox')
    ET.SubElement(bndbox, 'xmin').text = str(xmin)
    ET.SubElement(bndbox, 'ymin').text = str(ymin)
    ET.SubElement(bndbox, 'xmax').text = str(xmax)
    ET.SubElement(bndbox, 'ymax').text = str(ymax)

    tree = ET.ElementTree(annotation)
    xml_file_name = (
        image_path + "/" + filename + ".xml"
    )  # str(image_path+filename+".xml") # image_path.parent / (image_path.name.split('.')[0]+'.xml')
    print("image path " + str(image_path))
    print("xml_file_name" + str(xml_file_name))
    tree.write(xml_file_name)


# https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
with contextlib.ExitStack() as stack:
    device_infos = dai.Device.getAllAvailableDevices()
    if len(device_infos) == 0:
        raise RuntimeError("No devices found!")
    else:
        print("Found", len(device_infos), "devices")
    devices = {}

    for device_info in device_infos:
        # Note: the pipeline isn't set here, as we don't know yet what device it is.
        # The extra arguments passed are required by the existing overload variants
        openvino_version = dai.OpenVINO.Version.VERSION_2021_4
        usb2_mode = False
        device = stack.enter_context(
            dai.Device(openvino_version, device_info, usb2_mode)
        )

        # Note: currently on POE, DeviceInfo.getMxId() and Device.getMxId() are different!
        print("=== Connected to " + device_info.getMxId())
        mxid = device.getMxId()
        cameras = device.getConnectedCameras()
        usb_speed = device.getUsbSpeed()

        # Get a customized pipeline based on identified device type
        pipeline = getPipeline()
        device.startPipeline(pipeline)

        # Output queue will be used to get the rgb frames from the output defined above
        devices[mxid] = {
            'rgb': device.getOutputQueue(name="rgb"),
            'nn': device.getOutputQueue(name="nn"),
        }

    frame_for_save = None
    detect_label = None
    width = None
    height = None
    xmin = None
    ymin = None
    xmax = None
    ymax = None
    while True:
        # print("devices: ",devices)
        # print("\n")
        # print("devices.items: ",devices.items())
        for mxid, q in devices.items():
            if q['nn'].has():
                dets = q['nn'].get().detections
                frame = q['rgb'].get().getCvFrame()

                frame_for_save = frame.copy()

                for detection in dets:
                    ymin = int(300 * detection.ymin)
                    xmin = int(300 * detection.xmin)
                    ymax = int(300 * detection.ymax)
                    xmax = int(300 * detection.xmax)
                    # print("detection.label: "+str(detection.label)+"\n")
                    cv2.putText(
                        frame,
                        labelMap[detection.label],
                        (xmin + 10, ymin + 20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (255, 255, 255),
                    )
                    cv2.putText(
                        frame,
                        f"{int(detection.confidence * 100)}%",
                        (xmin + 10, ymin + 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (255, 255, 255),
                    )
                    cv2.rectangle(
                        frame,
                        (xmin, ymin),
                        (int(300 * detection.xmax), int(300 * detection.ymax)),
                        (255, 255, 255),
                        2,
                    )
                    # print(labelMap[detection.label]+" xmin: "+str(xmin)+
                    # " ymin: "+str(ymin)+" xmax: "+str(xmax)+" ymax: "+str(ymax) )
                    detect_label = labelMap[detection.label]
                    height = frame.shape[0]
                    width = frame.shape[1]

                # Show the frame
                cv2.imshow(f"Preview - {mxid}", frame)

        if cv2.waitKey(1) == ord('q'):
            break
        if cv2.waitKey(1) == ord('s'):
            if (pathlib.Path.cwd() / 'images').exists():
                filelist = os.listdir('images')
                # index = len(filelist) # used for storing only images
                index = int(
                    len(filelist) / 2
                )  # used for storing images and associated xml
            else:
                pathlib.Path('images').mkdir(parents=True, exist_ok=True)

            cv2.imwrite("images/capture_" + str(index) + ".jpg", frame_for_save)
            cv2.imwrite("images_framed/capture_framed_" + str(index) + ".jpg", frame)
            create_labimg_xml(
                str(images_path),
                str("capture_" + str(index)),
                "ama_savoia",
                width,
                height,
                xmin,
                ymin,
                xmax,
                ymax,
            )
            index = index + 1
