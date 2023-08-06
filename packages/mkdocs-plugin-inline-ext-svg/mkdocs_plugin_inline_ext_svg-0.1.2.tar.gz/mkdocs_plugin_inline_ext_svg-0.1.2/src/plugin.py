# plugin.py

import re
import os

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs import config
from mkdocs import utils

def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def replace_with_file_content(basepath, match, extension):
    filename = os.path.abspath(os.path.join(basepath, match.group(2) + extension))
    utils.log.info("mkdocs-plugin-inline-ext-svg: including SVG: {}".format(
        filename))
    return read_file(filename)

class InlineSvgPlugin(BasePlugin):

    config_scheme = (
        ('extension', config_options.Type(str, default='.svg')),
    )

    def on_config(self, config, **kwargs):
        self.extension = self.config['extension']
        return config

    def on_page_markdown(self, markdown, **kwargs):
        basepath = os.path.dirname(kwargs.get("page").file.abs_src_path)
        pattern = re.compile(r"!\[(.*?)\]\((.*?)" + re.escape(self.extension) + "\)", flags=re.IGNORECASE)
        markdown = re.sub(
            pattern, lambda match: replace_with_file_content(basepath, match, self.extension), markdown
        )
        return markdown
