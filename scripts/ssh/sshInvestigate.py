from enum import Enum


class RetVals(Enum):
    DEFAULT = {}
    FAILED = {}


class SshChecks():
    checks_passed = 0
    checks_defaulted = 0
    root_login = False

def check_root_login():
    sshd_config_path = '/etc/ssh/sshd_config'
    try:
        with open(sshd_config_path, 'r') as file:
            lines = file.readlines()
            value = None
            for line in lines:
                if line.startswith('PermitRootLogin'):
                    value = line.split()[1].strip()
                    print("PermitRootLogin value:", value)
                    if value.lower() != 'no':
                        value = line.split()[1].strip()
                        print("The value is likely set to:", value)
                        return False
                    else:
                        print("PermitRootLogin is likely set to:", value.lower())
                        return True
                if line.startswith('#PermitRootLogin'):
                    print("I saw: ",line)
                    print("PermitRootLogin is likely set to the default value")
                    return RetVals.DEFAULT
    except FileNotFoundError:
        print(f"Error: {sshd_config_path} not found.")
        return RetVals.FAILED
    except Exception as e:
        print(f"An error occured: {str(e)}")
        return False


if __name__ == "__main__":
    ssh_checks_instance = SshChecks()
    root_login = check_root_login()

    if root_login:
        ssh_checks_instance.checks_passed += 1
    print(ssh_checks_instance.checks_passed)
