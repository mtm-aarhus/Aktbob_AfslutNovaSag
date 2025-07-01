
# 📄 README

## Aktbob Afslut Nova Sag Robot

**Aktbob Afslut Nova Sag** is an automation for **Teknik og Miljø, Aarhus Kommune**. It closes building cases in KMD Nova, updates their metadata, and marks all related tasks as completed, ensuring cases are fully finalized and traceable in the system.

---

## 🚀 Features

✅ **Queue-Driven Execution**
- Consumes queue items containing Deskpro IDs
- Processes multiple cases linked to each Deskpro ticket

✅ **KMD Nova Case Updates**
- Retrieves case metadata (title, date) via Nova API
- Updates case status to *Afsluttet* (Closed) with final dates and category *BomByg*

✅ **Task Management**
- Retrieves all associated tasks in the case
- Identifies specific tasks (e.g., *Klar til sagsbehandling*, *Afslut sagen*)
- Marks tasks as completed with timestamps and descriptions

✅ **Credential Management**
- Automatically refreshes KMD Nova access tokens
- Securely manages credentials in OpenOrchestrator

✅ **Database Integration**
- Looks up cases linked to Deskpro IDs in SQL Server
- Updates database records to mark cases as closed

---

## 🧭 Process Flow

1. **Queue Trigger**
   - Starts when a queue element with a Deskpro ID is received (`Addqueue.py`)

2. **Token Retrieval**
   - Gets or refreshes KMD Nova access token (`GetKMDAcessToken.py`)

3. **Case Identification**
   - Queries the orchestrator database to find all Case UUIDs tied to the Deskpro ID

4. **Case Update**
   - Retrieves the case title and date
   - Sets case state to *Afsluttet* and updates key fields (decision date, close date)

5. **Task Update**
   - Fetches all tasks linked to the case
   - Updates each relevant task to status *Færdig*

6. **Logging**
   - Prints status messages and handles errors gracefully

---

## 🔐 Privacy & Security

- All API communication uses HTTPS
- Tokens and credentials are stored securely in OpenOrchestrator
- No sensitive data is persisted locally

---

## ⚙️ Dependencies

- Python 3.10+
- `requests`
- `pyodbc`
- `pytz`
- `uuid`

---

## 👷 Maintainer

Gustav Chatterton  
*Digital udvikling, Teknik og Miljø, Aarhus Kommune*
