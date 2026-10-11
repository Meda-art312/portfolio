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

Import this directory as the project root, choose **Other** as the framework preset, leave the build command empty, and use **dist** as the output directory. `vercel.json` supplies the static output configuration. The website can also be hosted on any static hosting service.

## Source content

Project screenshots and original links were recovered from https://mohameds-portfolio.vercel.app/ on October 11, 2026. Experience, education, certification, and contact details come from the supplied resume. The dashboard card uses the updated links supplied by the user: live preview at https://the-wild-oasis-dashboard-eosin.vercel.app/login and source at https://github.com/Meda-art312/the-wild-oasis-dashboard. Both returned HTTP 200 when checked. The old dashboard URL remains in the recovery record for provenance. The other four project destinations also returned HTTP 200 when checked. These are HTTP reachability checks, not full functional audits of third-party projects.

The original portfolio source was also found at https://github.com/xMeda33/My-portfolio/tree/main. Its `src/constants/index.js` matches all five projects and the experience content in the old deployment. The repository's default branch is `starter`; use **main** for the customized portfolio. A complete ZIP of that branch is saved locally at `recovery/original-portfolio-main.zip`, excluded from Git and deployment. The new portfolio is an independent rebuild.
