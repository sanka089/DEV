def crc_ccitt_encoder(dataword):
    # Define the CRC-CCITT (16-bits) polynomial 0x1021
    polynomial = 0x1021
    crc = 0xFFFF  # Initial CRC value

    # Convert the binary dataword to an integer
    dataword_int = int(dataword, 2)

    # XOR each bit of the dataword with the CRC
    for i in range(len(dataword)):
        # Get the most significant bit of the current CRC value
        msb = (crc >> 15) & 1

        # Shift CRC left by 1 bit
        crc <<= 1

        # XOR the current CRC value with the next bit of dataword
        crc ^= ((dataword_int >> (len(dataword) - i - 1)) & 1)

        # Check if the most significant bit was 1
        if msb:
            crc ^= polynomial

    # Convert the CRC value to a 16-bit binary string
    crc_codeword = format(crc, '016b')

    # Return the CRC codeword
    return crc_codeword


def main():
    # Get the binary dataword as input
    dataword = input("Enter the binary dataword (0s and 1s): ")

    # Calculate the CRC codeword
    crc_codeword = crc_ccitt_encoder(dataword)

    print(f"CRC-CCITT (16-bits) Codeword: {crc_codeword}")

    # Simulate the receiver's end (you can modify this part as needed)
    received_codeword = input("Enter the received codeword: ")

    if received_codeword == crc_codeword:
        print("No errors detected. Data is correct.")
    else:
        print("Error detected. Data is corrupt.")


if __name__ == "__main__":
    main()
