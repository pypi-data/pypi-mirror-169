from requests import request
import os
import time

class Bot:

    def __init__(self, token: str = None):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN') if token is None else token
        
        # Prepare all urls that would be used so we don't have to do it in each method
        self.base_url = 'https://api.telegram.org/bot{token}/{method}'
        self.get_updates_url = self.base_url.format(token=self.token, method='getUpdates')
        self.send_message_url = self.base_url.format(token=self.token, method='sendMessage')
        self.timeout = 10

    def __make_request(self, request_method, url, data=None, params=None, timeout=None):
        
        if timeout is None:
            timeout = self.timeout
        return request(request_method, url, data=data, params=params, timeout=timeout)
    
    def __acknowledge_update(self, update_id:int) -> bool:
        """Acknoledges that the previos update has been received. The system works
        by sending another getUpdates request with incremented update_id

        Args:
            update_id (int): The update_id of the message we would like to acknowledge

        Raises:
            Exception: If HTTP status code is not 200

        Returns:
            bool: True if the previos message was acknoledged correctly
        """

        payload = {'offset' : update_id + 1}
        r = self.__make_request('get', self.get_updates_url, data=payload)

        if r.status_code != 200:
            raise Exception(f'An error occured with message acknowledgement')
        return True
    
    def send_msg(self, to:str, msg:str) -> None:
        
        payload = {'chat_id' : to, 'text' : msg}  

        r = self.__make_request('post', self.send_message_url, data=payload)

        if r.status_code != 200:
            raise Exception(f'An error occured with message notification - {r.status_code}')
        return True

    def __execute_command(self, about):
        print(f'cmd has been executed for {about}')
        # TO DO
        # Implement method that executes a command on the host machine
        pass
    
    def __get_message(self):
        """Get a single message by polling
        """

        return 
    def listen(self, interval:int) -> None:
        """Main loop that polls messages for a particular bot as defined by the
        get_updates_url.
        
        The way Telegram's polling system works is by getting the last messages from
        getUpdates API. Once message is received you have to acknowledgement it,
        otherwise it will stay in the queue.
        The acknowledgement system works by sending another request to getUpdates API
        with incremented update_id parameter. See self.__acknowledge_update method
        
        Args:
            interval (int): Interval between each poll.
        """
        print('Bot started listening for updates...')

        while True:
            time.sleep(interval)
            r = self.__make_request('get', self.get_updates_url)

            if r.json()['result']:
                update_id = r.json()['result'][0]['update_id']
                self.__acknowledge_update(update_id)
                self.__execute_command(about=update_id)