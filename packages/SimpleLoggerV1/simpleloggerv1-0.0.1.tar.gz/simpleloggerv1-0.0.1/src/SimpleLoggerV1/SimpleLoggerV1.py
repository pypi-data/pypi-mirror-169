from urllib import response
from pymodbus.client.sync import ModbusTcpClient, ModbusSerialClient
import struct 
class SimpleLoggerV1:

    def __init__(self,method,ip=None,serialPort=None):
        if(method=='rtu'):
            self.client = ModbusSerialClient(method='rtu', port=serialPort, timeout=1,baudrate=460800)
        else:
            self.client = ModbusTcpClient(host=ip,port = 80)
        

    def uint16_to_float32(self,MSB,LSB):
        float32_msb = MSB.to_bytes(2, byteorder='big', signed=False)
        float32_lsb = LSB.to_bytes(2, byteorder='big', signed=False)
        float32_full = float32_msb + float32_lsb
        float32 = struct.unpack(">f",float32_full)
        return float32[0]

    def readA0(self):
        response = self.client.read_input_registers(30002,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA1(self):
        response = self.client.read_input_registers(30004,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA2(self):
        response = self.client.read_input_registers(30006,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA3(self):
        response = self.client.read_input_registers(30008,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA4(self):
        response = self.client.read_input_registers(30010,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA5(self):
        response = self.client.read_input_registers(30012,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA12(self):
        response = self.client.read_input_registers(30014,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA13(self):
        response = self.client.read_input_registers(30016,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA14(self):
        response = self.client.read_input_registers(30018,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA15(self):
        response = self.client.read_input_registers(30020,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA12A13(self):
        response = self.client.read_input_registers(30022,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA14A15(self):
        response = self.client.read_input_registers(30024,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA16(self):
        response = self.client.read_input_registers(30026,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA17(self):
        response = self.client.read_input_registers(30028,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA18(self):
        response = self.client.read_input_registers(30030,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA19(self):
        response = self.client.read_input_registers(30032,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA16A17(self):
        response = self.client.read_input_registers(30034,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readA18A19(self):
        response = self.client.read_input_registers(30036,2,unit=4)
        return self.uint16_to_float32(response.registers[0],response.registers[1])

    def readAllA(self):
        response = self.client.read_input_registers(30000,36,unit=4)
        result = []
        for i in range(0,len(response.registers),2):
            result.append(self.uint16_to_float32(response.registers[i],response.registers[i+1]))
        return result

    def readDO0(self):
        return self.client.read_coils(0x01).bits[0]

    def readDO1(self):
        return self.client.read_coils(0x02).bits[1]

    def writeDO0(self,value):
        self.client.write_coil(0x01, value,unit=4)

    def writeDO1(self,value):
        self.client.write_coil(0x02, value,unit=4)
