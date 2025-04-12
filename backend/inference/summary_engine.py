from transformers import pipeline

def summarize_text(text, max_length=150, min_length=30):
    """
    Summarize the given text using a pre-trained transformer model.
    :param text: The input text to summarize.
    :param max_length: Maximum length of the summary.
    :param min_length: Minimum length of the summary.
    :return: A summarized version of the input text.
    """
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {e}"

if __name__ == "__main__":
    print("Enter the lab report or prescription text (press Enter twice to finish):")
    input_text = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        input_text += line + " "
    
    if input_text.strip():
        print("\nSummarizing the input text...\n")
        summary = summarize_text(input_text.strip())
        print("Summary:")
        print(summary)
    else:
        print("No input text provided.")