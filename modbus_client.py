from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Connect to the Modbus server
client = ModbusClient('modbus-server', port=5020)
client.connect()

# Read multiple holding registers (from address 1 to 5)
result = client.read_holding_registers(1, 5)  # Start at register 1, read 5 registers
if result.isError():
    print("Error reading holding registers:", result)
else:
    print("Holding registers:", result.registers)

#write a value to a register (example: writing 100 to register 1)
client.write_register(1, 100)
print("Wrote 100 to register 1")

#Again reading the registers
result = client.read_holding_registers(1, 5)

if result.isError():
    print("Error reading holding registers:", result)
else:
    print("Holding registers:", result.registers)

client.close()

