import gradio as gr
import torch
from PIL import Image
import torchvision.transforms as transforms
import pickle
from GenshinDataSet import GenshinDataSet

def predict(img): # img is a PIL image resized to 128x128 pixels, normalize with mean = torch.tensor([0.0189, 0.0177, 0.0192]) and std = torch.tensor([0.0098, 0.0097, 0.0094])
    
    # Set device to GPU if available, else CPU
    
    #convert ndarray to PIL image
    img = Image.fromarray(img)    
    #convert img to rgb if it is not
    img = img.convert('RGB')
    
    #Define transformations
    all_transforms = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.0189, 0.0177, 0.0192], std=[0.0098, 0.0097, 0.0094])
    ])
    
    # Apply transformations
    img = all_transforms(img)

    # Run the model
    with torch.no_grad():
        if torch.cuda.is_available():
            model.cuda()
        img = img.to(device)
        #unsqueezing the image to add a batch dimension of 1
        output = model(img.unsqueeze(0))
        #get the index of the highest value in the output tensor
        _, predicted = torch.max(output, 1)
        predicted = predicted.cpu().numpy()
        print(f"value before labelDecoder{predicted[0]}")
        predicted = labelDecoder(predicted[0])
        print(predicted)
        return predicted

# Load the model from ../models/model_128_2fullyconnected_160epoch.pt
print("Loading model...")
model = torch.jit.load(r'C:\\Users\\Katana GF66 11UC\\Documents\\GenshinImageClassifier\\models\\torchScript200epoch.pt')

print("Model loaded successfully!")
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print("Device set to:", device)

print("Loading label decoder...")
labelDecoder = pickle.load(open(r'C:\\Users\\Katana GF66 11UC\\Documents\\GenshinImageClassifier\\models\\labelDecoder.pkl', 'rb'))

for label in labelDecoder.characterLabel:
    print(f"{label}: {labelDecoder.characterLabel[label]}")

gr.Interface(fn=predict, inputs="image", outputs="text",examples=[r'deploy\\arlecchino.jpeg',r'deploy\\furina.jpeg']).launch(share=True)








