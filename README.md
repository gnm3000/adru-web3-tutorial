# **$ADRU - Launching a Memecoin on Polygon with Web3.py**

## **📌 Overview**
$ADRU is a **memecoin inspired by the craftsmanship of Luthiers**, the artisans who meticulously handcraft guitars. This project is created for **educational purposes** to demonstrate how to deploy an ERC-20 token on **Polygon** using **Web3.py** and launch it on **Uniswap (QuickSwap)**.

The goal of this repository is to provide a **step-by-step guide** for creating, deploying, and adding liquidity to a memecoin on a decentralized exchange (DEX).

## **🔧 Project Features**
- 🚀 **Deploy an ERC-20 Token ($ADRU) on Polygon** using **Web3.py**.
- 📜 **Smart Contract Development** in **Solidity**.
- 💰 **Add liquidity on QuickSwap (Polygon’s Uniswap equivalent)**.
- 🔍 **Educational insights into launching a memecoin**.
- 🔗 **Interact with Polygon’s blockchain programmatically**.



### **📂 Project Structure**
```
├── contracts/              # Contains the Solidity contract for $ADRU
│   ├── AdruToken.sol       # ERC-20 token contract
├── scripts/                # Python scripts for deployment and liquidity addition
│   ├── compile_contract.py # Compile Solidity contract using solcx
│   ├── deploy_adru.py      # Deploy $ADRU token on Polygon
│   ├── add_liquidity.py    # Add liquidity to QuickSwap
├── .env                    # Private keys and API credentials (DO NOT SHARE)
├── README.md               # Documentation for the project
├── requirements.txt        # Dependencies
```

### **📜 File Descriptions**
#### `contracts/AdruToken.sol`
- Solidity contract implementing the ERC-20 standard for $ADRU.

#### `scripts/compile_contract.py`
- Compiles the Solidity contract and outputs ABI and Bytecode.

#### `scripts/deploy_adru.py`
- Deploys the compiled contract to the Polygon blockchain using Web3.py.

#### `scripts/add_liquidity.py`
- Adds $ADRU token liquidity to QuickSwap (Uniswap V2 on Polygon).

#### `.env`
- Contains **PRIVATE_KEY** and **POLYGON_RPC**.

#### `requirements.txt`
- Lists dependencies: Web3, eth_account, solcx, python-dotenv.

---
🚀 **This structure ensures a smooth process for launching and managing $ADRU on Polygon!**




## **📜 Steps to Deploy $ADRU**

### **1️⃣ Environment Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/adru-memecoin.git
   cd adru-memecoin
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with your **Polygon RPC URL** and **private key**:
   ```
   PRIVATE_KEY="your-private-key"
   POLYGON_RPC="https://polygon-mainnet.infura.io/v3/YOUR_INFURA_API"
   ```

### **2️⃣ Compile & Deploy the Smart Contract**
1. Run the contract compilation script:
   ```bash
   python scripts/compile_contract.py
   ```
2. Deploy the contract on **Polygon Mainnet or Testnet (Mumbai)**:
   ```bash
   python scripts/deploy_adru.py
   ```
   **Expected Output:** Smart contract address on Polygon.

### **3️⃣ Add Liquidity on QuickSwap**
1. Approve the token for QuickSwap Router.
2. Add liquidity by providing **MATIC and ADRU tokens**:
   ```bash
   python scripts/add_liquidity.py
   ```
   **Expected Output:** Liquidity pool created on QuickSwap.

### **4️⃣ Verify the Token on Polygonscan**
Once deployed, verify your token contract on **[Polygonscan](https://polygonscan.com/)**.

### **5️⃣ Promote & Grow the Memecoin**
- Share the contract address.
- List it on DEX trackers.
- Build a community!

## **⚠️ Disclaimer**
This project is for **educational purposes only**. **$ADRU has no real-world value** and should not be considered an investment.

---
🚀 **Let's launch the $ADRU memecoin together!** 🎸

