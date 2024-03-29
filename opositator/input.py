
class InputReader:
    def __init__(self):
        self.file_path = 'input/input.txt'

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='latin-1') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file '{self.file_path}': {e}")
            return None
        
    def extract_details(self, content):
        all_lines = content.split('\n')
        return [line for line in all_lines if line != '']
                