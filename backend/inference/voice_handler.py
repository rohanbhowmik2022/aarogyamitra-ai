import whisper

def transcribe_audio(audio_path, model_size="base"):
    """
    Transcribe speech from an audio file using OpenAI's Whisper model.
    :param audio_path: Path to the audio file.
    :param model_size: Size of the Whisper model to use (e.g., "tiny", "base", "small", "medium", "large").
    :return: Transcribed text.
    """
    try:
        # Load the Whisper model
        model = whisper.load_model(model_size)
        # Transcribe the audio
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {e}"

if __name__ == "__main__":
    print("Enter the path to the audio file:")
    audio_path = input().strip()
    
    if audio_path:
        print("\nTranscribing the audio file...\n")
        transcription = transcribe_audio(audio_path, model_size="base")
        print("Transcription:")
        print(transcription)
    else:
        print("No audio file path provided.")