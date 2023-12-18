#!/usr/bin/env python3
import base64
import pathlib

print("'use strict';")
print("let glintFrames = [];")
for i, frame_path in enumerate(pathlib.Path("frames/").iterdir()):
    with open(frame_path, "rb") as frame_file:
        print("glintFrames.push(new Image());")
        print(
            f'glintFrames[glintFrames.length - 1].src = "data:image/png;base64,{base64.b64encode(frame_file.read()).decode("utf-8")}";'
        )
