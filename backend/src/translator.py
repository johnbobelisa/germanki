# src/translator.py
from transformers import T5Tokenizer, T5ForConditionalGeneration

def german_to_english_v1(labels: list) -> dict:
    """
    Translates a list of English labels into German.

    Parameters:
    - labels (list of str): A list containing English labels to be translated.

    Returns:
    - dict: A dictionary where each key is an English label and its value is the German translation.
    """
    # Check if the input is empty
    if not labels:
        return {}

    # Initialize the tokenizer and model
    try:
        tokenizer = T5Tokenizer.from_pretrained("google/t5-small")
        model = T5ForConditionalGeneration.from_pretrained("google/t5-small")
    except Exception as e:
        print(f"Error loading tokenizer or model: {e}")
        return {}

    # Define the task prefix for translation
    task_prefix = "translate English to German: "

    # Prepare the sentences by adding the task prefix
    sentences = [task_prefix + label for label in labels]

    # Tokenize the input sentences with padding for batching
    try:
        inputs = tokenizer(sentences, return_tensors="pt", padding=True)
    except Exception as e:
        print(f"Error during tokenization: {e}")
        return {}

    # Generate translations using the model
    try:
        output_sequences = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            do_sample=False  # Set to False to get the most likely translation
        )
    except Exception as e:
        print(f"Error during text generation: {e}")
        return {}

    # Decode the generated translations back to text
    try:
        translations = tokenizer.batch_decode(output_sequences, skip_special_tokens=True)
    except Exception as e:
        print(f"Error during decoding: {e}")
        return {}

    # Create a dictionary mapping English labels to German translations
    translated_dict = dict(zip(labels, translations))

    return translated_dict
