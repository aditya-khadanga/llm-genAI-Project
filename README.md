# LLM-based Dockerfile Generator

This project uses **Large Language Models (LLMs)** — both **local** (via [Ollama](https://ollama.com)) and **hosted** (via [Google Gemini 2.0 flash ](https://makersuite.google.com/app)) — to generate custom Dockerfiles based on your application language and requirements.

---

## 📁 Project Structure
```
llm-gen-ai-project/
├── local-llm-ollama/
│   ├── dockerfile_generator.py
│   └── requirements.txt
├── hosted-llm-ollama/
│   ├── dockerfile_generator_gemini.py
│   └── requirements.txt
├── README.md
```
## 💡Project-1 Local LLM with Ollama

**Ollama** is like Docker but for local LLMs. It provides a CLI and a model registry (like DockerHub) to run and interact with LLMs on your machine.

## 🤖 Prerequisites
1. Install Python in your VM & then create venv for env logical isolation.
```bash
sudo apt update
sudo apt install python3
python3 --version
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
```
2. Local LLM Setup

Go to [Ollama](https://ollama.com) ( just like dockerhub its the ollamahub)
here you will see ollama 3.2 is the latest Metas released local llms.
after selecting the version .. paste the command in terminal ( it will say ollama not found , because there is no ollama cli --( check the below codes to download ollama CLI.


### 🛠️ Installation Steps

**Install Ollama CLI & run it **

   - **Linux**:
     ```bash
     curl -fsSL https://ollama.com/install.sh | sh
     ```

   - **MacOS**:
     ```bash
     brew install ollama
     ```

**Check Ollama Service, then pull & run it**
   ```bash
   ollama serve  # it should say already in use
   ollama pull llama3.2:1b
   ollama run llama3.2:1b
   ```

### Download the requirements and Trigger the Python Script

```bash
pip3 install -r requirements.txt
python3 dockerfile_generator.py
deactivate #after completion stop the venv 
```

## 💡 Project-2 Hosted LLM with Google Gemini 2.0 flash

it charges fees for the api calls & tokens used but Google AI Studio: Gemini Pro 1.5 (it offers a free API key) it may be restricted for some persons.

## 🤖 Prerequisites
1. Install Python in your VM & then create venv for env logical isolation.
```bash
sudo apt update
sudo apt install python3
python3 --version
sudo apt install python3.12-venv
python3 -m venv gemini_venv
source gemini_venv/bin/activate
```
2. Hosted LLM Setup

Go to [Gemini 2.0 flash](https://makersuite.google.com/app)
go to Google AI Studio  →  get API key. create a api key for the current project. after the project delete API key



### 🛠️ Installation Steps

**Install dependencies & run it **
     ```bash
pip3 install -r requirements.txt
export GOOGLE_AI_STUDIO_API_KEY="<your_api_key_paste_here"
pip3 install --upgrade google-generativeai
python3 dockerfile_generator-gemini.py
deactivate #after completion stop the venv 
     ```




