from load_data import load_data
from json import load as jsload

class Titanic:
    def __init__(self):
        self.data: dict = Titanic.load_data('ships_data.json')
        self.is_running = True
    def run(self):
        print(self.data.keys())
        
        while self.is_running:
            print('Welcome to the Ships CLI! Enter \'help\' to view available commands.')
            user_input = input('>>> ')
    def check_command(self,inp: str) -> None:
        match inp:
            case 'help':
                print()
            
            
    def load_data(file_path: str) -> dict:
        "Load a json file"
        with open(file_path, "r") as handle:
            return jsload(handle)
if __name__ == '__main__':
    APP = Titanic()
    APP.run()
