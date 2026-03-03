import time
from smbus2 import SMBus

# -----------------------------
# I2C addresses
BH1750_ADDR = 0x23
MPU6050_ADDR = 0x68

# MPU6050 registers
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

bus = SMBus(1)

# -----------------------------
# BH1750 functions
def read_bh1750():
    # Continuous H-Resolution mode
    bus.write_byte(BH1750_ADDR, 0x10)
    time.sleep(0.18)  # sensor measurement time

    data = bus.read_i2c_block_data(BH1750_ADDR, 0x00, 2)
    raw = (data[0] << 8) | data[1]
    lux = raw / 1.2
    return lux

# -----------------------------
# MPU6050 functions
def mpu6050_init():
    # Wake up MPU6050
    bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg + 1)
    value = (high << 8) | low
    if value >= 0x8000:
        value = value - 65536
    return value

def read_accel():
    ax = read_word(ACCEL_XOUT_H)
    ay = read_word(ACCEL_XOUT_H + 2)
    az = read_word(ACCEL_XOUT_H + 4)

    # Convert to g (±2g scale)
    ax /= 16384.0
    ay /= 16384.0
    az /= 16384.0

    return ax, ay, az

# -----------------------------
# Main
mpu6050_init()

while True:
    lux = read_bh1750()
    ax, ay, az = read_accel()

    wind_level = abs(ax) + abs(ay) + abs(az)

    print(f"Light: {lux:6.1f} lux | "
          f"Accel (g): ax={ax:.2f}, ay={ay:.2f}, az={az:.2f} | "
          f"Wind level: {wind_level:.2f}")

    time.sleep(1)
