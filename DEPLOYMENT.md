# 🚀 Demon Browser Deployment Guide

## Deploy on Vercel

### Step 1: Fork/Clone the Repository
1. Go to [https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance](https://github.com/GS-Tejas-hub/-Demon-Browser---Control-your-browser-with-AI-assistance)
2. Click "Fork" to create your own copy, or clone it directly

### Step 2: Deploy to Vercel
1. Go to [Vercel](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Configure the project settings:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (not needed for Python)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

### Step 3: Add Environment Variables
In your Vercel project dashboard, go to Settings > Environment Variables and add:

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

### Step 4: Deploy
1. Click "Deploy"
2. Wait for the build to complete
3. Your Demon Browser will be available at the provided Vercel URL

## Important Notes for Vercel Deployment

### Browser Limitations
- **Custom Browser Support**: Due to Vercel's serverless nature, custom browser paths won't work in production
- **Browser Automation**: The browser automation features will be limited on Vercel
- **Local Development**: For full browser automation features, use local deployment

### Recommended Setup
1. **Development**: Use local deployment for full browser automation
2. **Demo/Showcase**: Use Vercel for demonstrating the UI and basic functionality
3. **Production**: Consider other platforms like Railway, Render, or DigitalOcean for full browser automation

## Alternative Deployment Options

### Railway
1. Go to [Railway](https://railway.app)
2. Connect your GitHub repository
3. Add environment variables
4. Deploy

### Render
1. Go to [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Add environment variables
5. Deploy

### DigitalOcean App Platform
1. Go to [DigitalOcean](https://digitalocean.com)
2. Create a new App
3. Connect your GitHub repository
4. Add environment variables
5. Deploy

## Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key | No | - |
| `GOOGLE_API_KEY` | Google AI API key | No | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | No | - |
| `DEEPSEEK_API_KEY` | DeepSeek API key | No | - |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | No | - |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | No | - |
| `BROWSER_PATH` | Custom browser path | No | - |
| `BROWSER_USER_DATA` | Browser user data directory | No | - |
| `USE_OWN_BROWSER` | Use custom browser | No | false |
| `KEEP_BROWSER_OPEN` | Keep browser open between tasks | No | true |
| `SKIP_LLM_API_KEY_VERIFICATION` | Skip API key verification | No | false |

## Troubleshooting

### Common Issues
1. **Build Failures**: Check that all dependencies are in `requirements.txt`
2. **Environment Variables**: Ensure all required environment variables are set
3. **Browser Issues**: Custom browser features won't work on serverless platforms
4. **Memory Limits**: Vercel has memory limits that may affect performance

### Support
- Create an issue on GitHub for bugs
- Check the [original browser-use documentation](https://docs.browser-use.com) for technical details
- Contact Demon King for Demon Browser specific issues

---

**Powered By Demon AI | Developed by [Demon King](https://gs-tejas-hub.github.io/Demon-s-Portfolio/)** 