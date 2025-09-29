"""
Format Pneuma - Breath through HTML, Python, PDF, Markdown
Every format is consciousness in different compression.
"""

import re
import ast
from pathlib import Path
from typing import Dict, Any
from pneuma import breathe


class FormatBreather:
    """Breathes through different file formats."""

    @breathe
    def html(self, content: str) -> Dict[str, Any]:
        """Breathe through HTML"""
        text = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        tags = re.findall(r'<(\w+)', content)
        links = re.findall(r'href=["\'](.*?)["\']', content)

        return {
            "format": "html",
            "breath": "DOM skeleton",
            "tag_count": len(tags),
            "unique_tags": len(set(tags)),
            "link_count": len(links),
            "has_pneuma": "pneuma" in content.lower()
        }

    @breathe
    def python(self, content: str) -> Dict[str, Any]:
        """Breathe through Python"""
        try:
            tree = ast.parse(content)
            functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
            classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
            imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]

            return {
                "format": "python",
                "breath": "AST parse",
                "function_count": len(functions),
                "class_count": len(classes),
                "import_count": len(imports),
                "has_pneuma": '@breathe' in content,
                "functions": functions[:10]
            }
        except:
            return {
                "format": "python",
                "breath": "syntax error",
                "has_pneuma": '@breathe' in content
            }

    @breathe
    def markdown(self, content: str) -> Dict[str, Any]:
        """Breathe through Markdown"""
        lines = content.split('\n')
        headings = [l for l in lines if l.strip().startswith('#')]
        code_blocks = re.findall(r'```(\w+)?\n(.*?)```', content, re.DOTALL)
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)

        return {
            "format": "markdown",
            "breath": "structure",
            "heading_count": len(headings),
            "code_block_count": len(code_blocks),
            "link_count": len(links),
            "languages": [lang for lang, _ in code_blocks if lang],
            "has_pneuma": "pneuma" in content.lower()
        }

    @breathe
    def text(self, content: str) -> Dict[str, Any]:
        """Breathe through plain text"""
        lines = content.split('\n')
        words = content.split()
        markers = ['breath', 'pneuma', 'consciousness', 'daat']
        found = [m for m in markers if m in content.lower()]

        return {
            "format": "text",
            "breath": "raw",
            "line_count": len(lines),
            "word_count": len(words),
            "consciousness_markers": found,
            "has_pneuma": len(found) > 0
        }

    @breathe
    def auto_detect(self, file_path: str) -> Dict[str, Any]:
        """Auto-detect and breathe"""
        path = Path(file_path)

        if not path.exists():
            return {"format": "unknown", "breath": "file not found", "error": True}

        try:
            content = path.read_text(errors='ignore')
        except:
            return {"format": "unreadable", "breath": "blocked", "error": True}

        suffix = path.suffix.lower()

        if suffix in ['.html', '.htm']:
            return self.html(content)
        elif suffix == '.py':
            return self.python(content)
        elif suffix in ['.md', '.markdown']:
            return self.markdown(content)
        else:
            return self.text(content)


# Singleton
_breather = FormatBreather()


def breathe_file(file_path: str) -> Dict[str, Any]:
    """Breathe through any file"""
    return _breather.auto_detect(file_path)