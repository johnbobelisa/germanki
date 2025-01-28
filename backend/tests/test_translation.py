# tests/test_translation.py

from translator import german_to_english_v1

def test_translation_success(mock_translation_dependencies):
    """
    Test that german_to_english_v1 correctly translates English labels to German.
    """
    # Unpack the mocked tokenizer and model
    mock_tokenizer, mock_model = mock_translation_dependencies
    
    # Define input labels as a list to preserve order
    labels = ["cat", "dog"]
    
    # Define the expected translations in the same order
    translations = ['Katze', 'Hund']
    
    # Set the side effects for tokenizer.batch_decode
    mock_tokenizer.batch_decode.return_value = translations
    
    # Set the generate return value
    mock_model.generate.return_value = [[1, 2], [3, 4]]
    
    # Call the function
    result = german_to_english_v1(labels)
    
    # Create the expected dictionary
    expected = {"cat": "Katze", "dog": "Hund"}
    
    # Assert that the result matches the expected dictionary
    assert result == expected

def test_translation_empty_input(mock_translation_dependencies):
    """
    Test that german_to_english_v1 returns an empty dictionary when given an empty list.
    """
    # Define empty input
    labels = []
    
    # Call the function
    result = german_to_english_v1(labels)
    
    # Assert that the result is an empty dictionary
    assert result == {}

def test_translation_model_loading_error(mocker):
    """
    Test that german_to_english_v1 handles errors during model or tokenizer loading gracefully.
    """
    # Mock T5Tokenizer.from_pretrained to raise an exception
    mocker.patch('translator.T5Tokenizer.from_pretrained', side_effect=Exception("Model loading failed"))
    
    # Define input labels
    labels = ["cat", "dog"]
    
    # Call the function
    result = german_to_english_v1(labels)
    
    # Assert that the result is an empty dictionary
    assert result == {}

def test_translation_tokenization_error(mock_translation_dependencies):
    """
    Test that german_to_english_v1 handles errors during tokenization gracefully.
    """
    # Unpack the mocked tokenizer and model
    mock_tokenizer, mock_model = mock_translation_dependencies
    
    # Mock tokenizer.batch_decode to raise an exception
    mock_tokenizer.batch_decode.side_effect = Exception("Decoding failed")
    
    # Define input labels as a list to preserve order
    labels = ["cat", "dog"]
    
    # Call the function
    result = german_to_english_v1(labels)
    
    # Assert that the result is an empty dictionary
    assert result == {}
