from load_data import load_data
from json import load as jsload, dumps as jssave
from time import perf_counter


class Titanic:
    def __init__(self):
        self.data: dict = Titanic.load_data('ships_data.json')
        self.is_running = True
    def run(self):
        print(self.data.keys())
        with open('test.json','w') as f:
            f.write(jssave(self.data,indent=4))
        self.data['data']
        while self.is_running:
            print('Welcome to the Ships CLI! Enter \'help\' to view available commands.')
            user_input = input('>>> ')
            
            self.check_command(user_input) 
    def check_command(self,inp: str) -> None:
        if inp == 'help':
                print("help\nshow_countries\ntop_countries\n")
        elif inp == 'show_countries': 

                countrys = {ship['COUNTRY'] for ship in self.data['data']} #store all countrys in a set to eliminate duplicates

                print_string = '\n'.join(countrys) # create a string that contains all countrys. 
                # [REASON]: Calling the print function multiple times is very slow.
                # print_string = 1.5ms (^3.2 times faster) + time for creating the string approximately (^3 times)
                # print for    = 4.8ms
                print(print_string)
        elif inp == 'top_countries':
                pass
    def load_data(file_path: str) -> dict:
        "Load a json file"
        with open(file_path, "r") as handle:
            return jsload(handle)
if __name__ == '__main__':
    APP = Titanic()
    APP.run()
