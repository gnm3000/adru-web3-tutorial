import solcx
import json

solcx.install_solc('0.8.0')

with open("contracts/AdruToken.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = solcx.compile_source(contract_source_code, output_values=["abi", "bin"])
contract_interface = compiled_sol["<stdin>:AdruToken"]

# Save ABI and Bytecode
with open("scripts/AdruToken.json", "w") as f:
    json.dump(contract_interface, f)

print("Contract compiled successfully.")

