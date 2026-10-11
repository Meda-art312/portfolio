# Mohamed Medhat — Portfolio

A responsive, dependency-free portfolio with five recovered projects, experience, technical skills, contact links, and a downloadable resume. Includes system dark mode, reduced motion support, accessible project filters, expandable project notes, mobile navigation, and email copying.

## Run locally

Requires Node.js 18 or newer. No installation is needed.

```powershell
cd D:\Projects\my-portfolio\portfolio
npm run dev
```

Open http://127.0.0.1:4173. Stop the server with Ctrl+C.

## Edit

- `dist/index.html`: portfolio copy, projects, experience, skills, and links.
- `dist/styles.css`: responsive layout and semantic light/dark color tokens.
- `dist/app.js`: navigation, project filters, active section, and email copying.
- `dist/assets/`: optimized recovered images and the supplied resume.
- `recovery/projects.json`: original project links, image mapping, and content provenance.
- `recovery/original-assets/`: full original project screenshots, preserved locally.

The original deployed JavaScript, CSS, and HTML are saved locally in `recovery/old-*` and excluded from Git and deployment. No original contact form service credentials have been carried into the new site. Contact uses email links.

## Deploy to Vercel

Import `Meda-art312/portfolio` in Vercel, use the repository root (`./`) as the root directory, choose **Other** as the framework preset, leave the build command empty, and use **dist** as the output directory. `vercel.json` supplies the static output configuration. No environment variables or backend service are required. The website can also be hosted on any static hosting service. `.openai/hosting.json` belongs to the existing private preview and is not used by Vercel.

## Resume

The download button serves `dist/assets/Mohamed-Medhat-Abdelfattah.pdf`, a searchable one-page resume with clickable live project and source links. `resume/content.json` contains the editable source; its `portfolio` value currently keeps the original public URL until the new Vercel URL is available.

To rebuild after editing that file, install Python's `reportlab` package and run:

```powershell
python resume/build_resume.py
Copy-Item output/pdf/Mohamed-Medhat-Abdelfattah.pdf dist/assets/Mohamed-Medhat-Abdelfattah.pdf
```

The generator uses Calibri on Windows and bundled ReportLab fonts on other platforms. Review the rendered PDF before replacing the downloadable copy. Resume generation is separate from the website; Vercel serves the committed PDF without running Python.

## Source content

Project screenshots and original links were recovered from https://mohameds-portfolio.vercel.app/ on October 11, 2026. Experience, education, certification, and contact details come from the supplied resume. The dashboard card uses the updated links supplied by the user: live preview at https://the-wild-oasis-dashboard-eosin.vercel.app/login and source at https://github.com/Meda-art312/the-wild-oasis-dashboard. Both returned HTTP 200 when checked. The old dashboard URL remains in the recovery record for provenance. The other four project destinations also returned HTTP 200 when checked. These are HTTP reachability checks, not full functional audits of third-party projects.

The original portfolio source was also found at https://github.com/xMeda33/My-portfolio/tree/main. Its `src/constants/index.js` matches all five projects and the experience content in the old deployment. The repository's default branch is `starter`; use **main** for the customized portfolio. A complete ZIP of that branch is saved locally at `recovery/original-portfolio-main.zip`, excluded from Git and deployment. The new portfolio is an independent rebuild.

The customer cabin booking project uses the updated live preview at https://the-wild-oasis-customers-three.vercel.app/ and source at https://github.com/Meda-art312/the-wild-oasis-customers, both supplied by the user and verified to return HTTP 200. Its featured hero preview also opens the live app.
