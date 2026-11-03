# Mosimodule

**Golden Ternary Flat Fold** 3D visualizer and Fibonacci origami automata sandbox.

Pure client-side Three.js (HTML5). No secrets, no backdoors, no external services beyond CDN for Three.js.

## Features
- Orbit / touch controls
- Golden ratio (φ) Fibonacci spiral (sunflower / pinecone geometry)
- Ternary-inspired concentric crease loops
- Central torus “black hole” singularity
- Ocean spray particle field
- Local crypto.randomUUID() session id only

## Run
Open `index.html` in a modern browser (or host on GitHub Pages).

## Encryption notes
This visualization is purely geometric and client-side. Elliptic-curve and post-quantum cryptography would require additional libraries and are intentionally omitted to keep the build pure, dependency-light, and free of secrets or injection surfaces. DOMPurify-style sanitization is not required because there is no dynamic HTML injection.

## License
CC BY-NC-ND 4.0 (consistent with prior j-mosij projects). Copyright jeremiahnmosij.

Built as a clean, safe, static demonstration of the mosimodule fold concept.
