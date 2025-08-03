# 🌐 Demon Browser - Control your browser with AI assistance


<br/>

[![GitHub stars](https://img.shields.io/github/stars/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance?style=social)](https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance/stargazers)
[![Deploy on Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance)

This project builds upon the foundation of the [browser-use](https://github.com/browser-use/browser-use), which is designed to make websites accessible for AI agents.

We would like to officially thank [WarmShao](https://github.com/warmshao) for his contribution to this project.

**Demon Browser:** is built on Gradio and supports most of `browser-use` functionalities. This UI is designed to be user-friendly and enables easy interaction with the browser agent.

**Expanded LLM Support:** We've integrated support for various Large Language Models (LLMs), including: Google, OpenAI, Azure OpenAI, Anthropic, DeepSeek, Ollama etc. And we plan to add support for even more models in the future.

**Custom Browser Support:** You can use your own browser with our tool, eliminating the need to re-login to sites or deal with other authentication challenges. This feature also supports high-definition screen recording.

**Persistent Browser Sessions:** You can choose to keep the browser window open between AI tasks, allowing you to see the complete history and state of AI interactions.

## 🚀 Quick Deploy

### Deploy on Vercel (Recommended)

1. Click the "Deploy on Vercel" button above
2. Add your environment variables in the Vercel dashboard
3. Deploy and enjoy!

### Environment Variables for Vercel

Add these environment variables in your Vercel project settings:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here
BROWSER_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
BROWSER_USER_DATA=C:\Users\username\AppData\Local\Google\Chrome\User Data\Profile 2
USE_OWN_BROWSER=false
KEEP_BROWSER_OPEN=true
SKIP_LLM_API_KEY_VERIFICATION=false
```

## 📦 Local Installation

### Option 1: Local Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance.git
cd -Demon-Browser---Control-your-browser-with-AI-assistance
```

#### Step 2: Set Up Python Environment
We recommend using [uv](https://docs.astral.sh/uv/) for managing the Python environment.

Using uv (recommended):
```bash
uv venv --python 3.11
```

Activate the virtual environment:
- Windows (Command Prompt):
```cmd
.venv\Scripts\activate
```
- Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

#### Step 3: Install Dependencies
Install Python packages:
```bash
uv pip install -r requirements.txt
```

Install Browsers in playwright. 
```bash
playwright install --with-deps
```
Or you can install specific browsers by running:
```bash
playwright install chromium --with-deps
```

#### Step 4: Configure Environment
1. Create a copy of the example environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
2. Open `.env` in your preferred text editor and add your API keys and other settings

#### Step 5: Enjoy the Demon Browser
1.  **Run the WebUI:**
    ```bash
    python webui.py --ip 127.0.0.1 --port 7788
    ```
2. **Access the WebUI:** Open your web browser and navigate to `http://127.0.0.1:7788`.
3. **Using Your Own Browser(Optional):**
    - Set `BROWSER_PATH` to the executable path of your browser and `BROWSER_USER_DATA` to the user data directory of your browser. Leave `BROWSER_USER_DATA` empty if you want to use local user data.
      - Windows
        ```env
         BROWSER_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
         BROWSER_USER_DATA="C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
        ```
        > Note: Replace `YourUsername` with your actual Windows username for Windows systems.
      - Mac
        ```env
         BROWSER_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
         BROWSER_USER_DATA="/Users/YourUsername/Library/Application Support/Google/Chrome"
        ```
        > Note: Replace `YourUsername` with your actual Mac username for Mac systems.
      - Linux
        ```env
         BROWSER_PATH="/usr/bin/google-chrome"
         BROWSER_USER_DATA="/home/YourUsername/.config/google-chrome"
        ```
        > Note: Replace `YourUsername` with your actual Linux username for Linux systems.

### Option 2: Docker Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance.git
cd -Demon-Browser---Control-your-browser-with-AI-assistance
```

#### Step 2: Configure Environment
1. Create a copy of the example environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
2. Open `.env` in your preferred text editor and add your API keys and other settings

#### Step 3: Build and Run with Docker Compose
```bash
docker compose up --build
```

#### Step 4: Enjoy the web-ui and vnc
- Web-UI: Open `http://localhost:7788` in your browser
- VNC Viewer (for watching browser interactions): Open `http://localhost:6080/vnc.html`
  - Default VNC password: "youvncpassword"
  - Can be changed by setting `VNC_PASSWORD` in your `.env` file

## 🎯 Features

- **🌐 Demon Browser Interface**: Beautiful royal gold themed UI
- **🤖 AI Agents**: Multiple AI agents built on Demon Browser
- **🔧 Custom Browser Support**: Use your own browser with profiles
- **📱 Persistent Sessions**: Keep browser open between tasks
- **🎨 Multiple LLM Support**: OpenAI, Google, Anthropic, DeepSeek, Ollama, and more
- **📹 Screen Recording**: High-definition browser interaction recording
- **🔒 Secure**: Environment variable based configuration

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **WarmShao**: Original browser-use project
- **Demon King**: Demon Browser branding and development with many changes
- **Demon AI**: Powered by Demon AI

---

**Powered By Demon AI | Developed by [Demon King](https://gs-tejas-hub.github.io/Demon-s-Portfolio/)**
