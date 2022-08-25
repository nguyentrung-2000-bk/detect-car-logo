# Welcome 
Logo Car Brand Recognition
## Download
Data set contains 27 logo brands in Vietnam including;  audi, BMW, Chevrolet, daewoo, ferrari, ford, honda, hyundai, Isuzu, kia da, Lada, Lamborghini, land rover, lexus, Mazda, mercedes, mitsubishi, Nissan, opel, Peugeot, Porsche, Rolls Royce, Ssangyong, Subaru, Suzuki, toyota, Vinfast. \
Dataset has 928 photos and label.
##  Install Yolov5

```
git clone https://github.com/ultralytics/yolov5 # clone
cd yolov5
pip install -r requirements.txt # install
```

## Train
- Export **train_data** in **yolov5/data**
- Create file **custom_data.yaml** in **yolov5/data**:
```
train: ./data/train_data/images/train/  # train images (relative to 'path') 128 images
val: ./data/train_data/images/val/ # val images (relative to 'path') 128 images

nc:  27 # number of classes
names: ['audi', 'BMW', 'Chevrolet', 'daewoo', 'ferrari', 'ford', 'honda', 'hyundai', 'Isuzu', 'kia da', 'Lada', 'Lamborghini', 'land rover', 'lexus', 'Mazda', 'mercedes', 'mitsubishi', 'Nissan', 'opel', 'Peugeot', 'Porsche', 'Rolls Royce', 'Ssangyong', 'Subaru', 'Suzuki', 'toyota', 'Vinfast']
```
- Train
```
python train.py --img 640 --batch 16 --epochs 300 --data custom_data.yaml --weights yolov5s.pt 
```

## Demo
- Detect 
```
python detect.py --weights best.pt --img 960 --conf 0.25 --source data/images/bmw-840i-2-3592.jpg
```
- Demo Gradio
```commandline
python demo_gradio.py
```