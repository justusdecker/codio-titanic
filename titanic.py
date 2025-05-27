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
                countryies = {ship['COUNTRY'] for ship in self.data['data']} #store all countrys in a set to eliminate duplicates
                countryies = list(countryies) # convert to a list to sort this later
                countryies = sorted(countryies)
                for country in countryies:
                    print(country)
        elif inp.startswith('top_countries'):
            splitted = inp.split(' ')
            if len(splitted) == 2:
                if splitted[1].isdecimal():
                    pass
                else:
                    print(f"Cant process the given argument [{splitted[1]}]")
            else: # splitted not [..., ...]
                print(f'Different argument count! Cant unpack({len(splitted) - 1} given. Expected 1)')
    def load_data(file_path: str) -> dict:
        "Load a json file"
        with open(file_path, "r") as handle:
            return jsload(handle)
if __name__ == '__main__':
    APP = Titanic()
    APP.run()
