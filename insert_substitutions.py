#!/usr/bin/env python3
import base64
import pathlib


INDENT = " " * 8

with open("modern-gif/dist/index.js") as modern_gif_file:
    modern_gif_src = modern_gif_file.read().removesuffix("\n")

glint_frames_js = "let glint_frames = [];\n"
for i, frame_path in enumerate(pathlib.Path("frames/").iterdir()):
    with open(frame_path, "rb") as frame_file:
        glint_frames_js += INDENT + "glint_frames.push(new Image());\n"
        glint_frames_js += (
            INDENT
            + f'glint_frames[glint_frames.length - 1].src = "data:image/png;base64,{base64.b64encode(frame_file.read()).decode("utf-8")}";\n'
        )
glint_frames_js = glint_frames_js.removesuffix("\n")

with open("src/index.html") as src_index_html_file:
    src_index_html = src_index_html_file.read()

pathlib.Path("build/").mkdir(exist_ok=True)
with open("build/index.html", "w") as build_index_html_file:
    build_index_html_file.write(
        src_index_html.replace("INSERT_MODERN_GIF_LIBRARY", modern_gif_src).replace(
            "INSERT_GLINT_FRAMES", glint_frames_js
        )
    )
