# tests/test_obj_detection.py

from obj_detection_v1 import object_detection_v1

def test_object_detection_success(mock_obj_detection_dependencies):
    """
    Test that object_detection_v1 correctly detects objects and returns unique labels.
    """
    # Unpack the mocked processor and model if needed (not used directly here)
    _, _ = mock_obj_detection_dependencies
    
    # Define a sample image URL
    image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    
    # Call the function
    result = object_detection_v1(image_url)
    
    # Assert that the result contains the expected labels
    assert result == {'cat', 'dog'}

def test_object_detection_invalid_url(mocker):
    """
    Test that object_detection_v1 handles invalid image URLs gracefully.
    """
    # Mock requests.get to raise an exception
    mocker.patch('obj_detection_v1.requests.get', side_effect=Exception("Invalid URL"))
    
    # Define an invalid image URL
    image_url = "http://invalid-url.com/image.jpg"
    
    # Call the function
    result = object_detection_v1(image_url)
    
    # Assert that the result is an empty set
    assert result == set()

def test_object_detection_no_detections(mock_obj_detection_dependencies, mocker):
    """
    Test that object_detection_v1 returns an empty set when no objects are detected.
    """
    # Unpack the mocked processor and model
    mock_processor, mock_model = mock_obj_detection_dependencies
    
    # Modify the mock to return no detections
    mock_processor.post_process_object_detection.return_value = [{
        "scores": [],
        "labels": [],
        "boxes": []
    }]
    
    # Define a sample image URL
    image_url = "https://fastly.picsum.photos/id/53/1280/1280.jpg?hmac=QP5opo-oENp5iFwsSiWH8azQuR0w0bwps6MT6yvhKwA"
    
    # Call the function
    result = object_detection_v1(image_url)
    
    # Assert that the result is an empty set
    assert result == set()
