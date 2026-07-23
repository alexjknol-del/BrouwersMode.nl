# BrouwersMode.nl

Statische site, gegenereerd met Python. Geen frameworks. Onafhankelijke gids over herenkleding.

## Bouwen

    python3 build.py

De site komt in `site/`.

## Deployen (Cloudflare Pages via GitHub)

Framework preset: None, build command `python3 build.py`, output directory `site`.
Daarna het domein toevoegen onder Custom domains.

## Structuur

Alle content staat als data bovenin `build.py`. Een item toevoegen betekent een blok toevoegen aan de
betreffende lijst en opnieuw bouwen. De illustraties zijn eigen SVG's in `assets/`, geen foto's onder licentie.
