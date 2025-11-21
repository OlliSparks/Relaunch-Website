# orca MyTools Website

Moderne Website für die MyTools-Plattform von orca. organizing company assets GmbH.

## 📁 Dateistruktur

```
orca-website/
├── index.html                  # Homepage
├── prozesse-marketing.html     # Prozesse (für Interessenten)
├── prozesse-support.html       # Prozesse (für Nutzer/Support)
├── erfolgsgeschichten.html     # BMW Case Study & Partner
├── ueber-uns.html              # Über uns, Mission, Team
└── README.md                   # Diese Datei
```

## 🚀 Deployment

### Option 1: GitHub Pages

1. Repository auf GitHub erstellen
2. Alle Dateien hochladen
3. In Repository Settings → Pages → Branch "main" auswählen
4. Fertig! Website ist unter `https://[username].github.io/[repo-name]` erreichbar

### Option 2: Netlify

1. Ordner zu GitHub pushen
2. Bei Netlify anmelden
3. "New site from Git" → Repository auswählen
4. Deploy!

### Option 3: Eigener Server

Einfach alle Dateien auf Webserver hochladen. Keine Build-Steps nötig.

## 🎨 Features

- ✅ Dark Theme mit orca Branding
- ✅ Vollständig responsive (Mobile, Tablet, Desktop)
- ✅ Keine externen Abhängigkeiten (außer Google Fonts)
- ✅ Logo als base64 eingebettet
- ✅ Schnelle Ladezeiten
- ✅ SEO-optimiert

## 📄 Seiten-Übersicht

### Homepage (index.html)
- Hero mit Orca-Hintergrund
- Feature-Übersicht (6 Features)
- Prozess-Timeline (4 Prozesse)
- Stats (200.000 Werkzeuge, 7.500 Nutzer, etc.)
- CTA

### Prozesse Marketing (prozesse-marketing.html)
**Zielgruppe:** Neue Interessenten

- Alle 4 Prozesse im Detail
- Benefits & Verkaufsargumente
- CTAs zu Demo

### Prozesse Support (prozesse-support.html)
**Zielgruppe:** Bestehende Nutzer

- Video-Platzhalter für Anleitungen
- Links zu Support-Dokumentation
- Schritt-für-Schritt Guides

### Erfolgsgeschichten (erfolgsgeschichten.html)
- BMW MyTools Case Study
- Timeline 2021-2023
- Stats & Erfolge
- Partner-Ökosystem (Sulzer, conaya, Fischer)

### Über uns (ueber-uns.html)
- Mission & Vision
- Die orca Story
- Circle of Experts
- Werte
- Technologie & Partner

## 🛠️ Anpassungen

### Videos einfügen (prozesse-support.html)

Ersetze:
```html
<div class="video-placeholder"></div>
```

Mit:
```html
<iframe src="DEINE_VIDEO_URL" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
```

### Farben anpassen

CSS Variablen in `<style>` Section:
- `--primary: #2c4a8c` (Blau)
- `--secondary: #f97316` (Orange)
- `--success: #10b981` (Grün)

### Kontakt-Links

Suche nach `href="#"` und ersetze mit echten URLs.

## 📊 Statistiken

Aktuelle Zahlen auf der Website:
- **200.000+** Werkzeuge verwaltet
- **7.500** aktive Nutzer
- **3.000** Lieferanten in 70 Ländern
- **99.83%** Erfolgsquote Inventur
- **160.000** Werkzeuge inventarisiert

## 🎯 Browser-Support

- Chrome/Edge (neueste Version)
- Firefox (neueste Version)
- Safari (neueste Version)
- Mobile Browser (iOS, Android)

## 📝 Lizenz

© 2024 orca. organizing company assets GmbH  
Alle Rechte vorbehalten

## 📧 Kontakt

**orca. organizing company assets GmbH**  
Antonibergstraße 17  
86643 Rennertshofen  
Deutschland

---

Built with ❤️ für die Automobilindustrie
