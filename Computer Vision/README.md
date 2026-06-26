# Computer Vision

This folder applies deep learning to image data. The core idea is that raw pixel values are not useful features on their own — a convolutional neural network (CNN) learns to extract meaningful features automatically, layer by layer.

---

## Core concepts

### Why standard ML doesn't work on images
A 256×256 image has 65,536 pixel values per channel. A fully-connected network on raw pixels would have millions of parameters, overfit immediately, and have no way to recognize that a cat in the top-left corner and a cat in the bottom-right corner are the same thing. CNNs solve this.

### Convolutional layers
A **convolutional layer** applies small learned filters (kernels) across the image. Each filter detects a specific pattern — edges, textures, shapes — regardless of where in the image it appears. Early layers detect low-level features (edges, colors); deeper layers combine those into high-level concepts (eyes, lungs, text).

### Pooling layers
**Max pooling** reduces the spatial size of feature maps by keeping only the strongest activation in each region. This makes the network faster, reduces overfitting, and builds in a degree of position tolerance.

### Training and evaluation
CNNs are trained with backpropagation just like other neural networks, but image datasets are often small relative to model size. Common strategies:
- **Data augmentation** — randomly flip, rotate, or crop training images to artificially expand the dataset
- **Dropout** — randomly zero out neurons during training to prevent co-adaptation
- **Early stopping** — stop training when validation loss stops improving

---

## Notebook

### `Covid/AI_Application_Case_Study_COVID_Detection.ipynb`

**Problem:** classify chest X-ray images as COVID-positive or negative.

**What the notebook covers:**
1. Loading and preprocessing image data from a zip archive
2. Building a CNN with Keras (`Conv2D`, `MaxPooling2D`, `Dense`, `Dropout`)
3. Data augmentation with `ImageDataGenerator`
4. Training the model and monitoring training vs. validation accuracy
5. Evaluating with a confusion matrix and classification report
6. Deploying an interactive prediction interface with Gradio

**Before running:** extract `X-ray Data.zip` in this folder. A pre-trained model (`tuned_ai_model_best_lat.keras`) is available in `Pre-Work/` if you want to skip straight to the evaluation and deployment sections.

The same notebook also lives in `Pre-Work/COVID Detection/` — that copy includes the trained model and deployment assets.

---

## Key takeaway

CNNs learn features from data rather than relying on hand-crafted rules. This makes them extremely powerful for image problems, but they require more data and compute than classical ML. The pattern here — build → augment → train → evaluate → deploy — is the same pattern used in production computer vision systems at any scale.
