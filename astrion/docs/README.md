# Astrion

Astrion ist eine leistungsstarke Sammlung von Tools für Blockchain, Netzwerke, Kryptographie, KI, Quanten und mehr. Dieses Open-Source-Projekt bietet Entwicklern, Forschern und Technik-Enthusiasten eine zentrale Plattform für nützliche Tools.

## **Hauptfunktionen**

### **1. Blockchain Tools**
- **Wallet Balance Checker**: Überprüft das Guthaben einer Wallet (z. B. Ethereum).
- **Token Price Checker**: Zeigt aktuelle Preise für Kryptowährungen an.

### **2. Netzwerk Tools**
- **URL to IP Converter**: Wandelt eine URL in die zugehörige IP-Adresse um.
- **IP to Location**: Zeigt den geografischen Standort einer IP-Adresse an.

### **3. Kryptographie Tools**
- **Hash Generator**: Erzeugt SHA-256-Hashes für beliebige Eingaben.

### **4. KI Tools**
- **Text Summarizer**: Fasst lange Texte auf wesentliche Punkte zusammen.
- **Sentiment Analyzer**: Analysiert die Stimmung eines Textes (positiv, neutral, negativ).

### **5. Quantum Tools**
- **Quantum Random Number Generator**: Generiert echte Zufallszahlen basierend auf Quantenmethoden.

---

## **Technologie**

- **Frontend**: HTML, CSS, JavaScript (Bootstrap).
- **Backend**: Flask (Python).
- **Datenbank**: SQLite (optional, für zukünftige Erweiterungen).

---

## **Installation**

### **1. Voraussetzungen**
- Python 3.x
- Node.js (optional, für erweitertes Frontend-Testing)
- Ein Browser mit Live Server Plugin (z. B. in VS Code)

### **2. Projekt klonen**
```bash
git clone https://github.com/<dein-benutzername>/astrion.git
cd astrion
```

### **3. Backend einrichten**
1. Navigiere in den Backend-Ordner:
   ```bash
   cd backend
   ```
2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Starte das Backend:
   ```bash
   python app.py
   ```

### **4. Frontend starten**
1. Navigiere in den Ordner `frontend`.
2. Öffne die Datei `index.html` mit einem Live Server Plugin.

---

## **Nutzung**

### **1. Tools**
- Navigiere über das linke Menü zu einer Kategorie, z. B. Blockchain oder Netzwerk.
- Nutze die Tools direkt im Browser, z. B. Wallet Balance Checker oder URL to IP Converter.

### **2. API**
Astrion bietet eine RESTful API für jedes Tool. Beispiel:
- **Wallet Balance Checker**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"wallet_address": "0x123456789"}' \
       http://127.0.0.1:5000/api/blockchain/wallet_balance
  ```
Weitere Details findest du in der [API-Dokumentation](./API_REFERENCE.md).

---

## **Projektstruktur**

```plaintext
Astrion/
├── backend/                     # Backend für API und Logik
│   ├── app.py                   # Haupt-Backend-Datei
│   ├── tools/                   # Module für verschiedene Kategorien
│   │   ├── blockchain.py
│   │   ├── network.py
│   │   ├── cryptography.py
│   │   ├── ai.py
│   │   ├── quantum.py
│   └── requirements.txt         # Python-Abhängigkeiten
├── frontend/                    # Frontend-Dateien
│   ├── index.html               # Dashboard
│   ├── pages/                   # Kategorie-Seiten
│   │   ├── blockchain.html
│   │   ├── network.html
│   │   ├── cryptography.html
│   │   ├── ai.html
│   │   ├── quantum.html
│   │   └── utilities.html
│   ├── assets/
│   │   ├── css/                 # Stylesheets
│   │   └── js/                  # JavaScript-Dateien
└── README.md                    # Projektübersicht
```

---

## **Beitrag leisten**

Wir freuen uns über Beiträge! Erstelle einfach einen Fork dieses Repositories, füge deine Änderungen hinzu und sende einen Pull-Request. 

---

## **Lizenz**

Dieses Projekt steht unter der [MIT-Lizenz](./LICENSE.md). Du kannst Astrion frei nutzen, modifizieren und verbreiten, solange der Hinweis auf die ursprünglichen Entwickler erhalten bleibt.

---

## **Kontakt**

Bei Fragen oder Vorschlägen kannst du dich gerne melden:
- **Projektleitung**: Dein Name
- **Mitentwicklung**: Astrion OpenAI

---
```

---

Du kannst diesen Text kopieren und in einer Datei mit dem Namen `README.md` speichern. Wenn du weitere Anpassungen brauchst, lass es mich wissen! 🚀