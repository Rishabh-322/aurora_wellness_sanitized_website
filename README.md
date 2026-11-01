# Aurora Wellness Studio — Recording-Safe Website Preview

This ZIP is a **local static-site demo** prepared from the previously supplied website files. It retains the main layout, services, workshop cards, CSS styling, responsive navigation and demo popup, but replaces actual image files and identifying content with neutral placeholders.

## Local preview (macOS)

1. Extract the ZIP to `Documents/aurora-wellness-demo` (or another local folder).
2. Open `index.html` in Safari or Chrome. Internet access is not required.
3. Optionally open the folder in Visual Studio Code to edit `index.html`, `styles.css`, and `script.js`.
4. The popup appears when the website loads; it can be closed with Escape, its close button, or the shaded backdrop. Use the `View Workshop Preview` button in Events to reopen it.
5. The Enquiry form demonstrates a success message locally without transmitting or storing information. **Do not enter real personal information.**

### Edit map

| File | Main purpose |
| --- | --- |
| `index.html` | Homepage structure, Events, gallery, popup, sample copy and placeholders |
| `styles.css` | Theme, layout, image-placeholder appearance, responsive rules |
| `script.js` | Navigation, scroll effects, demo form behavior |
| `assets/` | Initially **no image files**; add only approved generated artwork |
| `IMAGE_SLOTS.md` | Exact artwork filenames and installation guide |
| `scripts/apply_images.py` | Activates matching image files or restores placeholders |
| `IMAGE_RIGHTS_LOG.csv` | Keep evidence of rights and permissions for each image |
| `LICENSE` | The Unlicense public-domain dedication **for code the contributor owns** |



## Licensing and generated media

`LICENSE` contains **The Unlicense**, a public-domain dedication for original project code only to the extent that you are authorized to license it. This is **not proof** that third-party code, text or artwork is public domain. The original website may include contributions for which you need permission.

No images are included. When generated images are later added, they are **not automatically CC0 or Public Domain** merely because Gemini generated them or because the code has an Unlicense file. Verify the provider's terms, legal rights, relevant likeness permissions and your recording/platform requirements. Keep evidence in `IMAGE_RIGHTS_LOG.csv`.

Public posting or pushing this new folder to a repository does not erase any already-public files, older Git commits, cached pages or archived copies. Publish on a new clean repository if you need fresh history, and check every page after publishing.

## Demo-only notice

This is a visual demonstration, not a production wellness website. Workshop dates, organizer qualifications, therapeutic benefits, reviews, contact details and operational bookings are intentionally omitted or illustrative. Replace them with authorized, accurate information before using the website publicly.
