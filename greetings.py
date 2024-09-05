from datetime import  datetime

name = input('What is your name?')
hour = datetime.now().time().hour
greeting = 'Good morning' if 4 <= hour < 12 else 'Good aft>

print(f'{Greeting}, {name}!')
