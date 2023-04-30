#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment
from pathlib import Path

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    wavs = sorted(Path('samples_mos').glob('*wav'))
    questions = [
        {
            "title" : f"שמע {i+1}",
            "audio_path" : str(p),
            "name" : f"q_{i+1}_{p.name.replace(' ','-')}"
        } for i, p in enumerate(wavs)
    ]


    html = template.render(
        page_title="MOS רובו-שאול",
        form_url="https://script.google.com/macros/s/AKfycbwts5ghKot09txpxiO_rbbv2qyaO5U_U6N-kEQL7XGvY-RgkPYvQgekmud4-CQ8aKDRww/exec",
        form_id=1,
        questions=questions,
    )
    print(html)


if __name__ == "__main__":
    main()
