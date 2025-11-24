# orca Website Layout Switcher

## 📁 Dateien im Paket

| Datei | Beschreibung |
|-------|--------------|
| `index.html` | **Dark Mode** - Dunkles Design |
| `layout2.html` | **Light Mode** - Helles Design mit #1C2553 |
| `layout3.html` | **Actual CI Mode** - Platzhalter |

---

## 🎨 Light Mode Farbschema

- **Hauptfarbe**: `#1C2553` (RGB 28, 37, 83)
- **Kontrastfarbe**: `#f97316` (Orange)
- **Hintergrund**: Weiß (`#ffffff`)
- **Schrift**: Oswald (Google Fonts)
- **Schrift auf blauem Grund**: Weiß

---

## 📤 Anleitung: Upload zu GitHub

### Option A: Über GitHub Web-Interface (Einfach)

1. **Öffne dein Repository**
   ```
   https://github.com/ollisparks/Relaunch-Website
   ```

2. **Klicke auf "Add file" → "Upload files"**

3. **Ziehe die HTML-Dateien in das Upload-Feld**
   - `index.html`
   - `layout2.html`
   - `layout3.html`

4. **Commit Message eingeben**
   ```
   Add layout switcher with Dark Mode, Light Mode, and CI Mode
   ```

5. **Klicke auf "Commit changes"**

6. **Warte 1-2 Minuten** bis GitHub Pages aktualisiert

7. **Teste die Seite**
   ```
   https://ollisparks.github.io/Relaunch-Website/
   ```

---

### Option B: Über Git Command Line

```bash
# 1. Repository klonen (falls noch nicht geschehen)
git clone https://github.com/ollisparks/Relaunch-Website.git
cd Relaunch-Website

# 2. Dateien kopieren
# Kopiere index.html, layout2.html, layout3.html in den Ordner

# 3. Änderungen hinzufügen
git add index.html layout2.html layout3.html

# 4. Commit erstellen
git commit -m "Add layout switcher with Dark Mode, Light Mode, and CI Mode"

# 5. Push zu GitHub
git push origin main
```

---

## 🔄 Layout Switcher verwenden

Nach dem Upload findest du in der obersten Leiste ein Dropdown-Menü:

- **1 – Dark Mode** → `index.html`
- **2 – Light Mode** → `layout2.html`  
- **3 – Actual CI Mode** → `layout3.html`

Das Dropdown ist mit einem orangefarbenen **DEV**-Badge markiert und kann später entfernt werden.

---

## ⚠️ Wichtige Hinweise

1. **Alle Dateien müssen im selben Ordner liegen**
   - Die Links im Dropdown verweisen relativ aufeinander

2. **Cache leeren beim Testen**
   - `Ctrl + Shift + R` (Windows)
   - `Cmd + Shift + R` (Mac)

3. **GitHub Pages Verzögerung**
   - Nach dem Commit kann es 1-2 Minuten dauern

---

## 🎯 Nächste Schritte

1. ✅ Light Mode ist fertig
2. ⏳ Actual CI Mode folgt als nächstes
3. Nach Auswahl des finalen Designs wird das Dropdown entfernt

---

*Erstellt: November 2024*
