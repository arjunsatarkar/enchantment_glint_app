all: build/index.html

build/index.html: src/index.html insert_substitutions.py
	cd modern-gif && \
	pnpm install && \
	pnpm run build

	./insert_substitutions.py

clean:
	rm -rf build/