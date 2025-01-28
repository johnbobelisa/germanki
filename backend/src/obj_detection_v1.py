# src/obj_detection_v1.py

from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests

def object_detection_v1(image_url: str) -> set:
    """
    Detects objects in an image from a given URL and returns a set of unique labels.

    Parameters:
    - image_url (str): The URL of the image to perform object detection on.

    Returns:
    - Set[str]: A set of unique object labels detected in the image.
    """
    try:
        # Step 1: Load the image from the URL
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Ensure the request was successful
        image = Image.open(response.raw).convert("RGB")  # Ensure image is in RGB format
    except Exception as e:
        print(f"Error loading image: {e}")
        return set()

    try:
        # Step 2: Initialize the processor and model
        processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
        model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    except Exception as e:
        print(f"Error loading model or processor: {e}")
        return set()

    try:
        # Step 3: Process the image and get model outputs
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
    except Exception as e:
        print(f"Error during model inference: {e}")
        return set()

    try:
        # Step 4: Post-process the outputs to get detections with score > 0.9
        target_sizes = torch.tensor([image.size[::-1]])  # (height, width)
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
    except Exception as e:
        print(f"Error during post-processing: {e}")
        return set()

    # Step 5: Initialize a set to keep track of unique labels
    unique_labels = set()

    # Step 6: Iterate through detections and add labels to the set
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        label_name = model.config.id2label[label.item()]
        unique_labels.add(label_name)
        print(f"Detected {label_name}")

    return unique_labels
