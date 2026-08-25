#!/usr/bin/env python3
"""Scaffold a new static site project.

Creates a Netlify-ready project laid out the same way this repo is:
a `public/` directory served as-is, a `netlify.toml` carrying the build
config and security headers, and no build step.

    python scripts/init_project.py my-project
    python scripts/init_project.py my-project --title "My Project" --dir ~/sites
"""

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r'^[a-z0-9][a-z0-9-]*$')

NETLIFY_TOML = '''[build]
  publish = "public"

[[headers]]
  for = "/*"
  [headers.values]
    # Content Security Policy
    # Allows: self, Google Fonts
    # Add any API host you call to connect-src.
    Content-Security-Policy = """
      default-src 'self';
      script-src 'self';
      style-src 'self' https://fonts.googleapis.com;
      font-src 'self' https://fonts.gstatic.com;
      img-src 'self' data: blob:;
      connect-src 'self';
      frame-ancestors 'none';
    """
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"
'''

INDEX_HTML = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <span class="logo-text">{title}</span>
    </div>
  </header>

  <main class="app">
    <section class="panel">
      <h1 class="panel-title">{title}</h1>
      <p class="panel-desc">Edit <code>public/index.html</code> to start building.</p>
      <button id="hello-btn" class="btn btn-primary" type="button">Say hello</button>
      <p id="hello-out" class="panel-note" role="status" aria-live="polite"></p>
    </section>
  </main>

  <script src="app.js"></script>
</body>
</html>
'''

STYLES_CSS = '''/* =========================================================
   {title}
   ========================================================= */

/* -- Variables ----------------------------------------- */
:root {{
  --bg:       #faf9f7;
  --surface:  #ffffff;
  --border:   #e5e1d9;
  --ink:      #23201a;
  --muted:    #6f675c;
  --accent:   #b8975a;

  --ff-sans:  'DM Sans', system-ui, sans-serif;

  --shadow-sm: 0 2px 8px rgba(35, 32, 26, 0.08);
  --shadow-md: 0 8px 32px rgba(35, 32, 26, 0.12);

  --radius-sm: 6px;
  --radius-md: 12px;

  --transition: 0.2s ease;
}}

/* -- Reset & Base -------------------------------------- */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: var(--ff-sans);
  background: var(--bg);
  color: var(--ink);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}

/* -- Header -------------------------------------------- */
.site-header {{
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}}

.header-inner {{
  max-width: 960px;
  margin: 0 auto;
  padding: 1.25rem 1.5rem;
}}

.logo-text {{
  font-weight: 500;
  letter-spacing: 0.04em;
}}

/* -- Layout -------------------------------------------- */
.app {{
  max-width: 960px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}}

.panel {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  padding: 2.5rem;
}}

.panel-title {{
  font-size: 2rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}}

.panel-desc {{ color: var(--muted); margin-bottom: 1.5rem; }}

.panel-note {{ color: var(--muted); margin-top: 1rem; min-height: 1.6em; }}

code {{
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.9em;
  background: var(--bg);
  border-radius: var(--radius-sm);
  padding: 0.1em 0.35em;
}}

/* -- Buttons ------------------------------------------- */
.btn {{
  font: inherit;
  border: 1px solid transparent;
  border-radius: var(--radius-sm);
  padding: 0.65rem 1.4rem;
  cursor: pointer;
  transition: background var(--transition), border-color var(--transition);
}}

.btn-primary {{
  background: var(--accent);
  color: var(--surface);
}}

.btn-primary:hover {{ background: #a5854c; }}

.btn:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
'''

APP_JS = '''/* =========================================================
   {title}
   ========================================================= */

'use strict';

// -- Elements ---------------------------------------------
const helloBtn = document.getElementById('hello-btn');
const helloOut = document.getElementById('hello-out');

// -- Events -----------------------------------------------
helloBtn.addEventListener('click', () => {{
  helloOut.textContent = 'Hello from {title}.';
}});
'''

README_MD = '''# {title}

A static site with no build step. `public/` is served as-is; `netlify.toml`
sets the publish directory and the security headers.

## Develop

```bash
python3 -m http.server 8000 --directory public
```

Then open http://localhost:8000

## Deploy

Netlify publishes `public/`. To call an external API from the browser, add
its host to `connect-src` in the Content-Security-Policy in `netlify.toml` —
requests to hosts not listed there are blocked.

## Layout

```
{name}/
  netlify.toml     build config + security headers
  public/
    index.html
    styles.css
    app.js
```
'''

GITIGNORE = '''.DS_Store
node_modules/
.netlify/
.env
.env.*
'''


def title_from_name(name):
    """my-project -> My Project"""
    return ' '.join(word.capitalize() for word in name.split('-') if word)


def build_files(name, title):
    """Map of relative path -> file contents for a new project."""
    return {
        'netlify.toml': NETLIFY_TOML,
        '.gitignore': GITIGNORE,
        'README.md': README_MD.format(title=title, name=name),
        'public/index.html': INDEX_HTML.format(title=title),
        'public/styles.css': STYLES_CSS.format(title=title),
        'public/app.js': APP_JS.format(title=title),
    }


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description='Scaffold a Netlify-ready static site project.')
    parser.add_argument(
        'name',
        help='project name — lowercase letters, digits and hyphens (e.g. my-project)')
    parser.add_argument(
        '--title',
        help='human-readable title used in the page (default: derived from name)')
    parser.add_argument(
        '--dir', default='.', metavar='PARENT',
        help='directory to create the project in (default: current directory)')
    parser.add_argument(
        '--force', action='store_true',
        help='overwrite files that already exist in the target directory')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if not NAME_RE.match(args.name):
        print(
            "error: invalid project name '%s' — use lowercase letters, digits "
            'and hyphens, starting with a letter or digit' % args.name,
            file=sys.stderr)
        return 2

    root = Path(args.dir).expanduser() / args.name
    title = args.title or title_from_name(args.name)
    files = build_files(args.name, title)

    if not args.force:
        clashes = sorted(rel for rel in files if (root / rel).exists())
        if clashes:
            print('error: %s already contains %s (use --force to overwrite)'
                  % (root, ', '.join(clashes)), file=sys.stderr)
            return 1

    for rel, content in sorted(files.items()):
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        print('created %s' % path)

    print()
    print('%s is ready. Next:' % title)
    print('  python3 -m http.server 8000 --directory %s' % (root / 'public'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
