import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)-d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.log'
)

def start_app():
    logging.info('Application starts running')
    
def exit_app():
    logging.info('Application has been stopped')
    
def wrong_credential():
    logging.warning('A wrong access input of credentials done.')
    
def remove_event(event_name):
    logging.warning('An event named %r has been removed', event_name)

def remove_manager(username):
    logging.warning('The manager with username %r has been removed', username)
    

    