# conftest.py

import pytest
from unittest.mock import MagicMock

import torch

@pytest.fixture
def mock_obj_detection_dependencies(mocker):
    print("Applying mock_obj_detection_dependencies fixture")

    # Mock requests.get
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.raw = MagicMock()
    patched_get = mocker.patch('obj_detection_v1.requests.get', return_value=mock_response)
    print(f"Patched 'requests.get' with: {patched_get}")

    # Mock Image.open
    mock_image = MagicMock()
    mock_image.size = (800, 600)
    mock_image.convert.return_value = mock_image
    patched_open = mocker.patch('obj_detection_v1.Image.open', return_value=mock_image)
    print(f"Patched 'Image.open' with: {patched_open}")

    # Mock DetrImageProcessor.from_pretrained
    mock_processor = MagicMock()
    # Return a dictionary where scores, labels, boxes are TENSORS
    mock_processor.post_process_object_detection.return_value = [{
        "scores": torch.tensor([0.95, 0.99]),
        "labels": torch.tensor([1, 2]),
        "boxes": torch.tensor([[50, 100, 200, 300], [150, 200, 250, 350]])
    }]
    patched_processor = mocker.patch(
        'obj_detection_v1.DetrImageProcessor.from_pretrained',
        return_value=mock_processor
    )
    print(f"Patched 'DetrImageProcessor.from_pretrained' with: {patched_processor}")

    # Mock the model
    mock_model = MagicMock()
    mock_model.config.id2label = {1: 'cat', 2: 'dog'}

    # Replace its __call__ with a MagicMock that returns "outputs"
    mock_model.__call__ = MagicMock(
        return_value=MagicMock(
            # For DETR, the forward pass might return e.g. logits,
            # but you only need what's used in post-process. 
            # Usually you pass them to processor.post_process_object_detection anyway.
        )
    )
    patched_model = mocker.patch(
        'obj_detection_v1.DetrForObjectDetection.from_pretrained',
        return_value=mock_model
    )
    print(f"Patched 'DetrForObjectDetection.from_pretrained' with: {patched_model}")

    return mock_processor, mock_model



@pytest.fixture
def mock_translation_dependencies(mocker):
    """
    Fixture to mock dependencies for translator.py.
    """
    print("Applying mock_translation_dependencies fixture")

    # Mock T5Tokenizer.from_pretrained
    mock_tokenizer = MagicMock()
    patched_tokenizer = mocker.patch('translator.T5Tokenizer.from_pretrained', return_value=mock_tokenizer)
    print(f"Patched 'T5Tokenizer.from_pretrained' with: {patched_tokenizer}")

    # Mock T5ForConditionalGeneration.from_pretrained
    mock_model = MagicMock()
    patched_model = mocker.patch('translator.T5ForConditionalGeneration.from_pretrained', return_value=mock_model)
    print(f"Patched 'T5ForConditionalGeneration.from_pretrained' with: {patched_model}")

    # Return both so tests can configure them
    return mock_tokenizer, mock_model