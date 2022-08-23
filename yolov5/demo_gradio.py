import gradio as gr
import torch
from PIL import Image
import os

# os.chdir("runs/train/exp51/weights")
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp51/weights/best.pt')


def yolo(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    results = model(im)  # inference
    results.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results.imgs[0])


inputs = gr.inputs.Image(type='pil', label="Original Image")
outputs = gr.outputs.Image(type="pil", label="Output Image")
gr.Interface(yolo, inputs, outputs).launch(server_name='172.26.33.18', server_port=8031)
