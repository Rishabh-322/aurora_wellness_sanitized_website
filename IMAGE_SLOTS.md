# Image slots for generated artwork

The `assets/` folder ships with **no image files**. Each visual slot stays a colored CSS placeholder until you intentionally install your own images.

## Slot list

- `assets/profile-portrait.webp` — Portrait / abstract studio illustration
- `assets/service-hypnosis.webp` — Service illustration — hypnosis
- `assets/service-nlp.webp` — Service illustration — nlp
- `assets/service-sound-healing.webp` — Service illustration — sound healing
- `assets/service-third-eye.webp` — Service illustration — third eye
- `assets/service-chakras.webp` — Service illustration — chakras
- `assets/retreat-illustration.webp` — Retreat illustration
- `assets/featured-workshop-poster.webp` — Featured workshop poster
- `assets/workshop-archive-01.webp` — Workshop archive artwork 01
- `assets/workshop-archive-02.webp` — Workshop archive artwork 02
- `assets/workshop-program-overview.webp` — Programme overview illustration
- `assets/gallery-01.webp` — Gallery illustration
- `assets/gallery-02.webp` — Gallery illustration
- `assets/gallery-03.webp` — Gallery illustration
- `assets/gallery-04.webp` — Gallery illustration
- `assets/gallery-05.webp` — Gallery illustration
- `assets/gallery-06.webp` — Gallery illustration
- `assets/gallery-07.webp` — Gallery illustration
- `assets/gallery-08.webp` — Gallery illustration

## Installing an approved generated image

1. Save or export the generated image as WebP. Remove embedded metadata (especially location/EXIF), and visually inspect it for real people, brands, watermarks, and copyrighted material.
2. Give it one of the exact filenames above and place it into `assets/`.
3. On Mac, open Terminal in the project root and run: `python3 scripts/apply_images.py`. The helper activates any matching slots whose files are present.
4. Reload `index.html` and test the result. Repeat as needed. Use `python3 scripts/apply_images.py --reset` to restore all colored placeholders without deleting your images.
5. Record each image’s source, tool/service, usage terms, date, rights confirmation, and any needed person/model permissions in `IMAGE_RIGHTS_LOG.csv`.

Uploading to Gemini or generating through Gemini does **not** automatically create a CC0/Public Domain license. Do not state that an output is CC0 unless you can substantiate that status.
