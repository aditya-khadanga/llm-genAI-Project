import ollama
import os
import sys

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

DEFAULT_MODEL = 'llama3.2:1b'
OUTPUT_FILENAME = 'Dockerfile'

def generate_dockerfile(language: str, model: str = DEFAULT_MODEL) -> str:
    """
    Generates an ideal Dockerfile for the specified programming language using Ollama.

    Args:
        language: The programming language for which to generate the Dockerfile.
        model: The Ollama model to use for generation (defaults to llama3.1:8b).

    Returns:
        The generated Dockerfile content as a string.

    Raises:
        ollama.OllamaAPIError: If there is an error communicating with the Ollama API.
        Exception: For other unexpected errors during generation.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': PROMPT_TEMPLATE.format(language=language)}]
        )
        return response['message']['content'].strip()
    except ollama.OllamaAPIError as e:
        print(f"Error communicating with Ollama API: {e}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"An unexpected error occurred during Dockerfile generation: {e}", file=sys.stderr)
        raise

def save_dockerfile(content: str, filename: str = OUTPUT_FILENAME) -> None:
    """
    Saves the generated Dockerfile content to a file.

    Args:
        content: The Dockerfile content to save.
        filename: The name of the file to save to (defaults to 'Dockerfile').
    """
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"\nDockerfile saved to '{filename}'")
    except IOError as e:
        print(f"Error saving Dockerfile to '{filename}': {e}", file=sys.stderr)

if __name__ == '__main__':
    try:
        language = input("Enter the programming language: ").strip()
        if not language:
            print("Programming language cannot be empty.", file=sys.stderr)
            sys.exit(1)

        print(f"\nGenerating Dockerfile for {language} using model '{DEFAULT_MODEL}'...")
        dockerfile_content = generate_dockerfile(language)

        print("\nGenerated Dockerfile:\n")
        print(dockerfile_content)

        save_option = input("\nDo you want to save this Dockerfile? (y/N): ").lower()
        if save_option == 'y':
            save_dockerfile(dockerfile_content)
        else:
            print("Dockerfile not saved.")

    except ollama.OllamaAPIError:
        print("\nFailed to generate Dockerfile due to an Ollama API error.", file=sys.stderr)
        sys.exit(1)
    except Exception:
        print("\nAn unexpected error occurred during the process.", file=sys.stderr)
        sys.exit(1)
    finally:
        print("\nExiting Dockerfile generator.")
