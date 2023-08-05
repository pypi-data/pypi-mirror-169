import shutil
from configparser import ConfigParser
from pathlib import Path
from typing import List

from nmk_base.common import TemplateBuilder


class PythonSetupBuilder(TemplateBuilder):
    def build(self, setup_py_template: str, setup_cfg_files: List[str], setup_items: dict):
        # Copy setup.py
        setup_py_output = self.outputs[0]
        shutil.copyfile(Path(setup_py_template), setup_py_output)

        # Merge setup fragments to generate final setup
        setup_cfg_output = self.outputs[1]
        c = ConfigParser()
        for f_path in map(Path, setup_cfg_files):
            # Update config with rendered template
            c.read_string(self.render_template(f_path, {}))

        # Iterate on items contributed through yml project files (only ones contributing maps)
        for section, values in filter(lambda t: isinstance(t[1], dict), setup_items.items()):
            if not c.has_section(section):
                c.add_section(section)
            c[section].update(values)

        # Finally write config to output file
        with setup_cfg_output.open("w") as f:
            c.write(f)
