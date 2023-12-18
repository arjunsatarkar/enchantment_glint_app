all: build/index.html build/scripts/glintFrames.js build/scripts/modern-gif.js
		
build/scripts/modern-gif.js: build/scripts
	cd modern-gif && \
	pnpm install && \
	pnpm run build

	printf "// modern-gif from https://github.com/qq15725/modern-gif used under the MIT license\n" | cat - modern-gif/dist/index.js > build/scripts/modern-gif.js

build/index.html: src/index.html build/scripts
	cp src/index.html build/index.html

build/scripts/glintFrames.js: build/scripts encode_glint_frames.py
	./encode_glint_frames.py > build/scripts/glintFrames.js

build/scripts:
	mkdir -p build/scripts

clean:
	rm -rf build/
