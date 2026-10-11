# Design direction and review notes

Purpose: help hiring teams and collaborators understand Mohamed's frontend, API, and automation experience, inspect real projects, and make contact.

Signature: the real cabin booking product appears in a browser preview alongside a statement connecting interfaces to systems. Project imagery carries the visual identity; controls remain familiar and restrained. This follows the person's work rather than a generic illustration or invented code sample.

## Tokens

| Role | Light | Dark |
| --- | --- | --- |
| Surface | #f7f8fb | #101721 |
| Panel | #ffffff | #17212f |
| Content | #172336 | #edf2fb |
| Secondary text | #526075 | #a9b8ce |
| Primary action | #2553d8 | #9ebaff |
| Divider | #d9dfe9 | #34445b |

Typography uses the system UI font stack for readable content and controls. Display text is 43–82px depending on width; section headings 34–50px; body copy 14–16px; utility labels at least 11px. All typography uses rem or clamp values and supports browser zoom. Utility labels carry secondary information only.

Regular layout:

```text
Name                         Work  Experience  About  Contact
Engineering focus            Real cabin booking project
Description + actions        Preview + stack
Everyday toolkit
Selected work + project filters
Travel project image         Project description and notes
Project image                Project image
Experience intro             Roles and achievements
About + education            Technical skills
Contact
Footer links
```

Compact layout stacks the hero, projects, experience, and skills in reading order. A native button expands navigation; project filters and details remain available. No content is hidden by appearance mode or viewport width.

Motion is limited to short hover feedback and optional smooth anchor scrolling. Reduced motion disables transitions and smooth scrolling. No blur or transparency is required for reading content. Increased contrast is supported with stronger secondary text and borders.

## Skill references applied

- `accessibility.md > Vision`: "Convey information with more than color alone." Filters have aria-pressed, headings and labels describe content, and focus indicators remain visible.
- `layout.md > Adaptability`: "Be prepared for text-size changes." Layouts wrap, stack, and use flexible heights.
- `typography.md > Ensuring legibility`: "In general, avoid light font weights." Text uses normal through bold weights.
- `color.md > Inclusive color`: avoid insufficient foreground/background contrast. Actual token ratios are checked from hex values.
- `buttons.md > Best practices`: custom controls include press and focus states, with 44px minimum control height.
- `motion.md > Best practices`: "Make motion optional." Motion is removed under prefers-reduced-motion.
- `branding.md > Best practices`: "Ensure branding always defers to content." Real screenshots take priority over decorative branding.
- `writing.md > Best practices`: actions use descriptive labels: Explore my work, Download resume, Visit website, and View source.

These are web design principles, not claims of native Apple platform compliance. Design judgments: cool blue accents suit the engineering focus; imagery from the real projects gives the portfolio its specificity. An ornamental numbered section system and a decorative code panel were omitted because neither adds information.

Browser verification was blocked by the available browser tool's security policy. Responsive behavior, zoom, and appearance modes require visual confirmation in a browser; static source checks alone cannot verify the rendered result.
