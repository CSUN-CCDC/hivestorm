import sys

POLICY_SAMPLE_FILE_STRING = "SamplePolicy"
POLICY_SAMPLE_POLICY_OPTION = 'yes'
POLICY_SAMPLE_POLICY_OPTION = 'yes'

class FileConfigTests:
    def __init__(self, sshd_config_path):
        self.file_config_path = FILE_CONFIG_PATH
        self.number_of_tests = 0
        self.checks_passed = 0
        self.lines = self.read_file_config()

    def run_tests(self):
        self.number_of_tests += 1
        if self.check_test_condition():
            self.checks_passed += 1

    def read_file_config(self):
        try:
            with open(self.file_config_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: {self.file_config_path} not found.")
            return []

    def check_test_condition(self):
        for line in self.lines:
            if line.startswith(POLICY_SAMPLE_FILE_STRING):
                key = line.split()[1].strip()
                print(line)
                if key.lower() != POLICY_SAMPLE_POLICY_OPTION:
                    print("FAILED: ", line)
                    return False
                else:
                    print("PASSED: ", line)
                    return True
            elif line.startswith('#', POLICY_SAMPLE_FILE_STRING):
                print("DEFAULT: ", line)
                return False


if __name__ == "__main__":
    FILE_CONFIG_PATH = 'tests/configFile'
    file_tests_instance = FileConfigTests(FILE_CONFIG_PATH)

    file_tests_instance.run_tests()
    print("Tests passed ", file_tests_instance.checks_passed, "/", file_tests_instance.number_of_tests)
    if file_tests_instance.number_of_tests == file_tests_instance.checks_passed:
        print("All checks passed")
        sys.exit(0)
    else:
        print("Some checks failed")
        sys.exit(file_tests_instance.number_of_tests - file_tests_instance.checks_passed)
