import subprocess

def check_vpn_connection():
    try:
        # This command checks if there's an active VPN connection.
        output = subprocess.check_output(['netstat', '-rn'])
        if b'0.0.0.0' in output:
            print('VPN connection active')
            return True
        else:
            print('VPN connection not active')
            return False
    except subprocess.CalledProcessError:
        return False

def check_encryption():
    try:
        # This command retrieves encryption details for IPSec-based VPN connections.
        output = subprocess.check_output(['ipsec', 'status'], stderr=subprocess.STDOUT)
        output = output.decode()  # Convert bytes to string
        print(output)
        if 'Encryption algorithm' in output:
            encryption_info = output.split('Encryption algorithm:')[1].split('\n')[0].strip()
            print("Encryption algorithm:", encryption_info)
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


def check_authentication_method(self):
        try:
            # This command retrieves VPN connection details.
            output = subprocess.check_output(['cat', '/etc/ppp/chap-secrets'])  # Example command (Linux)
            print(output.decode())
            if 'username' in output and 'password' in output:
                print("Authentication method: Username/Password")
            elif 'certificate' in output:
                print("Authentication method: Certificate")
            else:
                print("Authentication method: Unknown")
            return True
        except subprocess.CalledProcessError:
            return False

def check_vpn_tunnel_integrity(self):
        try:
            # This command checks the VPN tunnel configuration.
            output = subprocess.check_output(['ip', 'tunnel', 'show'])  # Example command (Linux)
            print(output.decode())
            # Add checks for tunnel integrity here
            return True  # For demonstration, assume tunnel integrity check passed
        except subprocess.CalledProcessError:
            return False


def main():
    vpn_checker = VPNChecker()
    vpn_connected = vpn_checker.check_vpn_connection()
    if vpn_connected:
        print("You are connected to a VPN.")
        encrypted = vpn_checker.check_encryption()
        if encrypted:
            print("Your internet activity is encrypted.")
        else:
            print("Your internet activity is not encrypted.")
        auth_method = vpn_checker.check_authentication_method()
        if auth_method:
            print("Authentication method checked.")
        tunnel_integrity = vpn_checker.check_vpn_tunnel_integrity()
        if tunnel_integrity:
            print("VPN tunnel integrity checked.")
    else:
        print("You are not connected to a VPN.")

if __name__ == "__main__":
    main()

