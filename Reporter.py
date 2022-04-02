from colorama import Fore, init, Style
import threading, requests, ctypes, os

class Reporter:
    def __init__(self):
        self.reported = 0
        self.errors = 0
        
    def session(self):
        session = requests.Session()
        session.trust_env = False
        return session

    def update_title(self):
        ctypes.windll.kernel32.SetConsoleTitleW("Discord Report Spammer By Altify | Sent: {0} | Errors: {1}".format(self.reported, self.errors))

    def report_message(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US",
            "User-Agent": "Discord/21887 CFNetwork/1197 Darwin/20.0.0",
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        json = {"channel_id": self.channel_id, "message_id": self.message_id, "guild_id": self.guild_id, "reason": self.reason}
        Report = self.session().post("https://discordapp.com/api/v8/report", json = json, headers = headers)
        if Report.status_code == 201:
            self.reported += 1
            self.update_title()
        else:
            self.errors += 1
            self.update_title()

    def reasons(self):
        os.system("cls")
        print("\n{0} > {1}{2}1: Illegal Content".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT))
        print("{0} > {1}{2}2: Harassment".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT))
        print("{0} > {1}{2}3: Spam or Phishing Links".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT))
        print("{0} > {1}{2}4: Self Harm".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT))
        print("{0} > {1}{2}5: NSFW Content".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT))
        option = str(input("\n{0} > {1}{2}".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        if option == "1" or option == "Illegal Content":
            self.reason = 0
        elif option == "2" or option == "Harassment":
            self.reason = 1
        elif option == "3" or option == "Spam or Phishing Links":
            self.reason = 2
        elif option == "4" or option == "Self Harm":
            self.reason = 3
        elif option == "5" or option == "NSFW Content":
            self.reason = 4
        else:
            self.reasons()
    
    def start(self):
        self.reasons()
        def my_function():
            self.report_message()
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target = my_function).start()

    def main(self):
        os.system("cls")
        self.token = str(input("\n{0} > {1}{2}Token: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.guild_id = str(input("{0} > {1}{2}Server ID: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.channel_id = str(input("{0} > {1}{2}Channel ID: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.message_id = int(input("{0} > {1}{2}Message ID: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.threads = int(input("{0} > {1}{2}Threads: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.start()

ctypes.windll.kernel32.SetConsoleTitleW("Discord Report Spammer By Altify")
init(convert = True, autoreset = True)
Reporter().main()
