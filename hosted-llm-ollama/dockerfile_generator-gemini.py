import os
import sys
import google.generativeai as genai

# Load API Key from environment variable
GOOGLE_AI_STUDIO_API_KEY = os.environ.get("GOOGLE_AI_STUDIO_API_KEY")
if not GOOGLE_AI_STUDIO_API_KEY:
    print(
        "Error: GOOGLE_AI_STUDIO_API_KEY environment variable not set.",
        file=sys.stderr,
    )
    sys.exit(1)

genai.configure(api_key=GOOGLE_AI_STUDIO_API_KEY)

PROMPT_TEMPLATE = """
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description.
Include:
- Specifying a stable and minimal base image.
- Clearly defining and installing necessary dependencies.
- Setting an explicit and secure working directory.
- Strategically adding source code for efficient layering.
- Defining a non-root user for running the application.
- Exposing necessary ports.
- Clearly defining the command to run the application.
- Utilizing multi-stage builds where appropriate to minimize the final image size.
"""

DEFAULT_MODEL_NAME = "gemini-2.0-flash"
OUTPUT_FILENAME = "Dockerfile"

def generate_dockerfile(language: str, model_name: str = DEFAULT_MODEL_NAME) -> str:
    """
    Generates an ideal Dockerfile for the specified programming language using Google AI Studio.

    Args:
        language: The programming language for which to generate the Dockerfile.
        model_name: The Google AI Studio model to use for generation (defaults to gemini-2.0-flash).

    Returns:
        The generated Dockerfile content as a string.

    Raises:
        Exception: If there is an error communicating with the Google AI Studio API or during generation.
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            PROMPT_TEMPLATE.format(language=language)
        )
        if response and hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        elif response and hasattr(response, "error"):
            raise Exception(f"Google AI Studio API error: {response.error}")
        else:
            raise Exception("No response or error information received from Google AI Studio.")
    except Exception as e:
        print(
            f"An error occurred during Dockerfile generation: {e}",
            file=sys.stderr,
        )
        raise


def save_dockerfile(content: str, filename: str = OUTPUT_FILENAME) -> None:
    """
    Saves the generated Dockerfile content to a file.

    Args:
        content: The Dockerfile content to save.
        filename: The name of the file to save to (defaults to 'Dockerfile').
    """
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"\nDockerfile saved to '{filename}'")
    except IOError as e:
        print(f"Error saving Dockerfile to '{filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    try:
        language = input("Enter the programming language: ").strip()
        if not language:
            print("Programming language cannot be empty.", file=sys.stderr)
            sys.exit(1)

        print(
            f"\nGenerating Dockerfile for {language} using model '{DEFAULT_MODEL_NAME}'..."
        )
        dockerfile_content = generate_dockerfile(language)

        print("\nGenerated Dockerfile:\n")
        print(dockerfile_content)

        save_option = input("\nDo you want to save this Dockerfile? (y/N): ").lower()
        if save_option == "y":
            save_dockerfile(dockerfile_content)
        else:
            print("Dockerfile not saved.")

    except Exception:
        print(
            "\nFailed to generate Dockerfile due to an error.",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        print("\nExiting Dockerfile generator.")
