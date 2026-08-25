# My Project

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
my-project/
  netlify.toml     build config + security headers
  public/
    index.html
    styles.css
    app.js
```
