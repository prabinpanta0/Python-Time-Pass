#ping in a loop 
import os
import time

class WebsitePing:
    def __init__(self, url):
        self.url = url

    def ping_website(self):
        try:
            # Using os.system to execute the ping command
            # Adjust the count parameter based on your needs
            os.system(f'ping -c 3 {self.url}')
            print("Website is reachable.")
        except Exception as e:
            print("Internet error!!")

    def run_pinger(self):
        while True:
            self.ping_website()
            time.sleep(2)

# Example usage
if __name__ == "__main__":
    website_url = input("Enter the URL to ping: ")
    pinger = WebsitePing(website_url)
    pinger.run_pinger()
