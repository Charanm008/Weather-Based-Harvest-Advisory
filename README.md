# Weather-Based-Harvest-Advisory
“Weather‑Based Harvest Advisory: A Smart Python Tool for Farmers”

# 🛠️ Python Logic Engines: Agriculture & Disaster Response

This repository contains a suite of **Core Python** decision-support tools designed to solve real-world problems in agriculture and emergency management. No external libraries—just pure logic.

---

## 🌾 01. PestGuard // Infestation Tracker
**Domain:** Crop Protection & Early Warning Systems

### 📋 Overview
PestGuard is a lightweight, rule-based monitoring system. It tracks daily pest sightings and classifies the severity of the infestation to help farmers make data-driven decisions before damage becomes irreversible.

### ⚙️ The Logic Engine
Instead of reacting to a single bad day, the system calculates the **Moving Average** to smooth out short-term fluctuations.

| Average Count | Status | Action Required |
| :--- | :--- | :--- |
| **< 4** | 🟢 **Normal** | Routine monitoring. |
| **4.0 — 7.9** | 🟡 **Warning** | Increase inspection frequency. |
| **≥ 8** | 🔴 **Critical** | Immediate intervention required. |

> **Key Feature:** Built with **Input Validation** to ensure zero data entry errors in the field.

---

## 🆘 02. ReliefDistributor // Crisis Logic
**Domain:** Disaster Management & Humanitarian Logistics

### 📋 Overview
In a disaster, resources are finite. This engine implements a **Priority-Queue** to distribute aid (food, medicine, water) to the most vulnerable regions first, ensuring ethical and efficient resource allocation.

### 🕹️ Priority Matrix
The system ranks locations using a strict urgency hierarchy:
1.  🔴 **Critical** (Life-threatening)
2.  🟠 **High** (Severe shortage)
3.  🟡 **Medium** (Stable but declining)
4.  🔵 **Low** (Stable)

### 🧠 The "All-or-Nothing" Principle
To prevent "half-help" scenarios where a location receives insufficient supplies to survive, the engine only allocates **full requirements**. If the inventory is too low, the request is logged in a **Pending List** for the next supply cycle.

---

## 🛰️ 03. HarvestSense // Weather-Logic Engine
**Domain:** Post-Harvest Risk Mitigation

### 📋 Overview
Wet weather is the enemy of a successful harvest. **HarvestSense** analyzes the "Hydraulic Stress" of the last 3–7 days to determine if your crop is safe to pull from the field.

### 🧪 Threshold Parameters
The system executes a binary decision based on the intersection of two critical environmental factors:

* **Precipitation Limit:** < 5mm (Avg)
* **Humidity Limit:** < 70% (Avg)

```python
The Core Logic
IF (Avg_Rainfall < 5) AND (Avg_Humidity < 70):
    ADVISORY = "🟢 PROCEED: Field conditions are optimal."
ELSE:
    ADVISORY = "🔴 DELAY: High risk of mold and rot."
```
### ⚡ Technical Standards (Across All Projects)

  - Zero Dependencies: 100% Pure Python. Runs on anything from a high-end server to a Raspberry Pi.

  - Precision Math: Uses continuous floating-point averages for boundary accuracy (e.g., 69.9% vs 70.1%).

  - Scalability: The Disaster Relief module is stress-tested to handle up to 500 unique locations.

### 📈 Future Applications

    API Integration: Transition from manual entry to automated data fetching via OpenWeatherMap API.

    Crop Profiles: Presets for different crops (e.g., "Wheat Mode" vs. "Tomato Mode") with tailored humidity thresholds.

    Mobile Deployment: Integration into a simple SMS-based alert system for farmers in remote areas with limited internet.

### 🛠️ Installation & Usage

  Clone the Suite:

    git clone [https://github.com/yourusername/python-logic-suite.git](https://github.com/yourusername/python-logic-suite.git)

  Execute a Module:
    
    python pest_monitor.py
    # OR
    python relief_distributor.py
    # OR
    python harvest_sense.py

**Developed by Charan Manthena.** *Developed to bridge the gap between meteorological data and practical farming decisions.*
