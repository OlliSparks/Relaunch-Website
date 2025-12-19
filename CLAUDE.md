# ORCA Website - Relaunch

## Projekt-Uebersicht

Statische Website fuer ORCA - Organizing Company Assets. Marketing- und Support-Website fuer das BMW Asset-Management-System.

- **Live-URL:** https://ollisparks.github.io/Relaunch-Website/
- **Repository:** https://github.com/OlliSparks/Relaunch-Website

---

## Struktur

```
Relaunch-Website/
├── index.html                  # Startseite (Dark Mode)
├── light-mode-index.html       # Startseite (Light Mode)
├── support.html                # Support-Bereich
├── prozesse.html               # Prozess-Dokumentation (~1MB)
├── lieferanten.html            # Lieferanten-Info
├── ueber-uns.html              # Ueber uns
├── erfolgsgeschichten.html     # Erfolgsgeschichten
├── kontakt.html                # Kontaktformular
├── faq.html                    # FAQ
├── datenschutz*.html           # Datenschutz-Seiten
├── impressum.html              # Impressum
├── nutzungsbedingungen.html    # AGB
└── [weitere Unterseiten]
```

---

## Seiten-Kategorien

### Haupt-Navigation
| Seite | Dark Mode | Light Mode |
|-------|-----------|------------|
| Startseite | index.html | light-mode-index.html |
| Support | support.html | light-mode-support.html |
| Prozesse | prozesse.html | light-mode-prozesse.html |
| Lieferanten | lieferanten.html | light-mode-lieferanten.html |
| Ueber uns | ueber-uns.html | light-mode-ueber-uns.html |

### Rollen-Seiten
- `stocktaker.html` - Inventurdurchfuehrer
- `assetresponsible.html` - Werkzeugverantwortlicher
- `assetcoordinator.html` - Asset-Koordinator
- `buyer.html` - Einkaufer
- `admin.html` - Administrator

### Prozess-Seiten
- `inventur2025.html` - Inventur 2025
- `abl.html` - ABL-Prozess
- `prozess-verlagerung.html` - Verlagerung
- `toolingcoordinator-*.html` - Tooling-Koordinator Prozesse
- `subsuppliermanagement.html` - Unterlieferanten

### Info-Seiten
- `history.html` - Historie
- `onboarding.html` - Onboarding
- `dialogveranstaltung.html` - Events
- `videos.html` - Video-Bibliothek
- `basics.html` - Grundlagen

---

## Design-System

### Farben (Dark Mode)
```css
--bg-main: #0a0a0a
--text-primary: #ffffff
--accent: #00bcd4 (Cyan)
--accent-hover: #00acc1
```

### Farben (Light Mode)
```css
--bg-main: #ffffff
--text-primary: #1a1a1a
--accent: #0097a7 (Teal)
```

### CI-Skill
Siehe `skills/Fachliche Skills/ci-website/SKILL.md` im orca-app Repo.

---

## Entwicklung

### Lokaler Server
```bash
cd /c/Users/orcao/Relaunch-Website
python -m http.server 8080
# Dann: http://localhost:8080
```

### Git
```bash
git status
git add .
git commit -m "Beschreibung"
git push
```

### Dark/Light Mode Sync
Bei Aenderungen an Dark Mode Seiten muessen Light Mode Varianten auch aktualisiert werden.
Script: `sync_light_mode.py` (falls vorhanden)

---

## Footer-Template

Alle Seiten haben einheitlichen Footer:
```html
<footer class="footer">
    <div class="footer-links">
        <a href="impressum.html">Impressum</a>
        <a href="datenschutz.html">Datenschutz</a>
        <a href="kontakt.html">Kontakt</a>
    </div>
    <p>&copy; 2024 orca. organizing company assets GmbH</p>
</footer>
```

Script zum Footer-Update: `update_footer.py`

---

## Verknuepfung mit ORCA App

Die Website dient als oeffentliche Dokumentation. Der ORCA Allgemein-Agent (`agent-allgemein.js`) holt Inhalte von:
- support.html
- prozesse.html
- ueber-uns.html
- lieferanten.html

---

## TODOs

- [ ] Light Mode Seiten auf Stand bringen
- [ ] Prozesse-Seite optimieren (~1MB ist zu gross)
- [ ] Mobile Responsiveness pruefen
- [ ] SEO-Optimierung

---

## Skills

Relevante Skills im orca-app Repo:
- `skills/Fachliche Skills/ci-website/` - Corporate Design
- `skills/Prozess-Skills/` - Prozess-Beschreibungen
