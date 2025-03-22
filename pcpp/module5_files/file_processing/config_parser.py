import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost', 'env': 'dev'}
config['mysql'] = {'host': 'localhost', 'env': 'dev'}
config['postgresql'] = {'host': '127.0.0.1', 'env': 'prod'}
config['mongodb'] = {}

print(config['mysql']['env'])
print(config['postgresql']['env'])
print(config['mongodb']['env'])
