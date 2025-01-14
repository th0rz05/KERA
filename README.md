# Kerma Project: Blockchain Node Implementation

## **Overview**
The Kerma project is a blockchain node implementation designed to support a simplified cryptocurrency network. It includes essential blockchain functionalities, such as managing a mempool, validating transactions, handling blocks, and maintaining consistency during chain reorganizations. The project adheres to the protocol specifications provided in the [Kerma Protocol Documentation](./Kerma_Project_Overview_W2024.pdf).

---

## **Features**

1. **Genesis Block Initialization**:
   - The node begins with a genesis block to bootstrap the blockchain.

2. **Mempool Management**:
   - Handles valid transactions waiting to be included in blocks.
   - Removes transactions already present in the blockchain.
   - Validates new transactions against the UTXO set.

3. **Transaction Validation**:
   - Verifies transaction inputs, signatures, and UTXO availability.
   - Rejects invalid or duplicate transactions.

4. **Block Validation and Mining**:
   - Supports creating and adding new blocks.
   - Handles coinbase transactions for miners.

5. **Chain Reorganization (Reorg)**:
   - Adapts the chain when a longer competing chain is detected.
   - Updates the mempool and UTXO state accordingly.

6. **Networking**:
   - Supports peer-to-peer communication for broadcasting transactions and blocks.
   - Implements protocol-specific message handling (e.g., `hello`, `getpeers`, `getobject`).

---

## **Components**

### **1. Main Script (`main.py`)**

- Entry point for the node.
- Manages peer connections, handles incoming messages, and coordinates between mempool, blockchain, and database modules.

### **2. Mempool (`mempool.py`)**

- Manages unconfirmed transactions.
- Validates transactions and integrates with the UTXO set.
- Handles chain reorganization logic to maintain consistency.

### **3. Blockchain Logic (`objects.py`)**

- Provides transaction and block validation utilities.
- Implements signature verification and UTXO updates.

### **4. Database Handling (`create_db.py`)**

- Initializes and manages the SQLite database for storing blocks, transactions, and UTXO state.

### **5. Networking Protocol**

- Implements peer-to-peer communication.
- Supports the protocol-defined messages such as `hello`, `getpeers`, and `object` handling.

---

## **Setup Instructions**

### **Prerequisites**

- Python 3.8 or higher
- Required Python libraries:
  - `cryptography`
  - `sqlite3`
  - `jcs`
  - `asyncio`

Install dependencies:

```bash
pip install cryptography
pip install jcs
```

### **Initialization**

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Start the node:

   ```bash
   make run
   ```

---

## **Usage**

1. Start the node.
2. Use the provided client to send transactions and blocks to the node.
3. Monitor the mempool and blockchain behavior during transactions and chain reorganizations.
