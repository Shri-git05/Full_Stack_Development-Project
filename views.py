from django.shortcuts import render, redirect
from django.http import JsonResponse
from .speech_functions import recognize_speech_from_mic, translate_text
from django.shortcuts import render
from googletrans import Translator

def home(request):
    return render(request, "home.html")
def next_page(request):
    recognized_text = request.GET.get('recognized_text', '')
    return render(request, 'next_page.html', {
        'recognized_text': recognized_text
    })

def audio_recognition_page(request):
    return render(request, "audio_recognition.html")

def recognize_speech_from_mic(language_code="hi-IN", speech_input=None):
    # If speech_input is provided, use it; otherwise, simulate with a default message
    if speech_input:
        return speech_input
    else:
        raise ValueError("No speech input provided. Please provide valid speech input.")


def recognize_and_translate(request):
    if request.method == "POST":
        try:
            # Get the language from the request or default to Hindi
            language_code = request.POST.get("language_code", "hi-IN")

            # Recognize speech
            recognized_text = recognize_speech_from_mic(language_code=language_code)
            print(f"Recognized Text ({language_code}): {recognized_text}")  # Debugging

            # Translate the recognized text to English
            translated_text = translate_text(recognized_text, target_language="en")
            print(f"Translated Text: {translated_text}")  # Debugging

            # Pass both recognized and translated text to the template
            return render(request, "translation_result.html", {
                'recognized_text': recognized_text,
                'translated_text': translated_text,
            })

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def next_page(request):
    recognized_text = request.GET.get('recognized_text', '')
    return render(request, "next_page.html", {
        'recognized_text': recognized_text,
    })


def translation_result(request):
    # Retrieve recognized text from URL parameters or other sources
    recognized_text = request.GET.get('recognized_text', '')  # Adjust according to your logic

    # Translate the recognized text
    translated_text = ""
    if recognized_text:
        try:
            translated_text = translate_text(recognized_text, target_language="en")
        except Exception as e:
            translated_text = f"Error translating text: {str(e)}"

    # Render the result to the translation_result page
    return render(request, "translation.html", {
        'recognized_text': recognized_text,
        'translated_text': translated_text,
    })