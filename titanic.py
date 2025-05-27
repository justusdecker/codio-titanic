from load_data import load_data
def colored_text(text: str,color: int) -> None:
    "get the colorcodes from this site: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797/#color-codes"
    print(f"\033[38;5;{color}m{text}\033[39m")
class Titanic:
    def __init__(self):
        self.data: dict = load_data()
        self.is_running = True
    def run(self) -> None:
        "Main Logic. This method runs until the user enters: EXIT"
        self.data['data']
        while self.is_running:
            print('Welcome to the Ships CLI! Enter \'help\' to view available commands.')
            user_input = input('>>> ')
            
            self.check_command(user_input) 
    def check_command(self,inp: str) -> None:
        if inp == "quit" or inp == 'exit':
            self.is_running = False
        elif inp == 'help':
                print("help\nshow_countries\ntop_countries\nexit\nquit")
        elif inp == 'show_countries': 
                countryies = {ship['COUNTRY'] for ship in self.data['data']} #store all countrys in a set to eliminate duplicates
                countryies = list(countryies) # convert to a list to sort this later
                countryies = sorted(countryies)
                for idx, country in enumerate(countryies):
                    colored_text(country,247 if idx % 2 else 249)
        elif inp.startswith('top_countries'):
            splitted = inp.split(' ')
            if len(splitted) == 2:
                l = splitted[1]
                if l.isdecimal():
                    countryies = {}
                    for ship in self.data['data']:
                        if ship['COUNTRY'] in countryies:
                            countryies[ship['COUNTRY']] += 1
                        else:
                            countryies[ship['COUNTRY']] = 1    
                    countryies = list([(country,countryies[country]) for country in countryies]) # convert to a list to sort this later
                    countryies = sorted(countryies,key = lambda c: c[1],reverse=True)[:int(l)] # sort the list based on the second values each element in the list which means: [COUNTRY_COUNT]
                    for idx, country in enumerate(countryies):
                        colored_text(f"{country[0]:<15}: {country[1]}",247 if idx % 2 else 249)
                else:
                    colored_text(f"Cant process the given argument [{l}]",9)
            else: # splitted not [..., ...]
                colored_text(f'Different argument count! Cant unpack({len(splitted) - 1} given. Expected 1)',9)
        elif inp.isspace() or not inp:
            colored_text("Input is empty try again!",9)
        else:
            colored_text("Something went wrong try again!",9)
                
if __name__ == '__main__':
    APP = Titanic()
    APP.run()
