import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass(),
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base()
}


def create_ui(theme_name="Ocean"):
    css = """
    /* Royal Gold Text Styling */
    * {
        color: #DAA520 !important;
    }
    
    /* Specific styling for different elements */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;
        text-shadow: 0 0 5px #DAA520;
    }
    
    /* Labels and form elements */
    label, .label {
        color: #DAA520 !important;
    }
    
    /* Input fields */
    input, textarea, select {
        color: #DAA520 !important;
        border-color: #DAA520 !important;
    }
    
    /* Buttons */
    button {
        color: #DAA520 !important;
        border-color: #DAA520 !important;
    }
    
    /* Links */
    a {
        color: #FFD700 !important;
    }
    
    a:hover {
        color: #FFA500 !important;
    }
    
    /* Chat messages */
    .message {
        color: #DAA520 !important;
    }
    
    /* Footer */
    .footer {
        color: #DAA520 !important;
    }
    
    .footer a {
        color: #FFD700 !important;
    }
    
    .footer a:hover {
        color: #FFA500 !important;
    }
    
    /* Gradio specific elements */
    .gradio-container {
        width: 70vw !important; 
        max-width: 70% !important; 
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 10px !important;
    }
    .header-text {
        text-align: center;
        margin-bottom: 20px;
    }
    .tab-header-text {
        text-align: center;
    }
    .theme-section {
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        border-top: 1px solid #DAA520;
        color: #DAA520;
    }
    .footer a {
        color: #FFD700;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
        color: #FFA500;
    }
    """

    # dark mode in default
    js_func = """
    function refresh() {
        const url = new URL(window.location);

        if (url.searchParams.get('__theme') !== 'dark') {
            url.searchParams.set('__theme', 'dark');
            window.location.href = url.href;
        }
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="🌐 Demon Browser", theme=theme_map[theme_name], css=css, js=js_func,
    ) as demo:
        with gr.Row():
            gr.Markdown(
                """
                # 🌐 Demon Browser
                ### Control your browser with AI assistance
                """,
                elem_classes=["header-text"],
            )

        with gr.Tabs() as tabs:
            with gr.TabItem("⚙️ Agent Settings"):
                create_agent_settings_tab(ui_manager)

            with gr.TabItem("🌐 Browser Settings"):
                create_browser_settings_tab(ui_manager)

            with gr.TabItem("🤖 Run Agent"):
                create_browser_use_agent_tab(ui_manager)

            with gr.TabItem("🎁 Agent Marketplace"):
                gr.Markdown(
                    """
                    ### Agents built on Demon Browser
                    """,
                    elem_classes=["tab-header-text"],
                )
                with gr.Tabs():
                    with gr.TabItem("Deep Research"):
                        create_deep_research_agent_tab(ui_manager)

            with gr.TabItem("📁 Load & Save Config"):
                create_load_save_config_tab(ui_manager)

        # Footer
        with gr.Row():
            gr.HTML(
                """
                <div class="footer">
                    Powered By Demon AI | Developed by <a href="https://gs-tejas-hub.github.io/Demon-s-Portfolio/" target="_blank">Demon King</a>
                </div>
                """,
                elem_classes=["footer"]
            )

    return demo
