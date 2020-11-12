# TryAPL Code Button
# Based on https://github.com/executablebooks/sphinx-copybutton
from pathlib import Path
from sphinx.util import logging

__version__ = "0.3.1"

logger = logging.getLogger(__name__)


def tryapl_btn_static_path(app):
    app.config.html_static_path.append(
        str(Path(__file__).parent.joinpath("_static").absolute())
    )


def add_to_context(app, config):
    # Update the global context
    config.html_context.update(
        {"tryaplbutton_prompt_text": config.tryaplbutton_prompt_text}
    )
    config.html_context.update(
        {"tryaplbutton_prompt_is_regexp": config.tryaplbutton_prompt_is_regexp}
    )
    config.html_context.update(
        {"tryaplbutton_only_copy_prompt_lines": config.tryaplbutton_only_copy_prompt_lines}
    )
    config.html_context.update(
        {"tryaplbutton_remove_prompts": config.tryaplbutton_remove_prompts}
    )
    config.html_context.update({"tryaplbutton_image_path": config.tryaplbutton_image_path})
    config.html_context.update({"tryaplbutton_selector": config.tryaplbutton_selector})


def setup(app):

    logger.verbose("Adding TryAPL buttons to code blocks...")
    # Add our static path
    app.connect("builder-inited", tryapl_btn_static_path)

    # configuration for this tool
    app.add_config_value("tryaplbutton_prompt_text", "", "html")
    app.add_config_value("tryaplbutton_prompt_is_regexp", False, "html")
    app.add_config_value("tryaplbutton_only_copy_prompt_lines", True, "html")
    app.add_config_value("tryaplbutton_remove_prompts", True, "html")
    app.add_config_value("tryaplbutton_image_path", "tryapl.svg", "html")
    app.add_config_value("tryaplbutton_selector", "div.highlight pre", "html")

    # Add configuration value to the template
    app.connect("config-inited", add_to_context)

    # Add relevant code to headers
    app.add_css_file("tryapl_button.css")
    #app.add_js_file("clipboard.min.js")
    app.add_js_file("tryapl_button.js")
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }