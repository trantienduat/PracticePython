# Menu class
class Menu:
    def __init__(self):
        self.items = []

    def add_item_to_menu(self, item):
        self.items.append(item)

    def display_menu(self, message):
        print(message)
        for i in range(len(self.items)):
            print("%d." % (i+1), self.items[i])

    def get_option_from_user(self):
        max_option = self.items.__len__()
        is_valid = False
        while not is_valid:
            try:
                choice = int(input('Enter your option (1 -> {}): '.format(max_option)))
                if 1 <= choice <= max_option:
                    is_valid = True;
                    continue;
                if 3 < choice > 1:
                    print(Constants.WARNING_STATUS + ' Option only between from 1 to {}'.format(max_option))
                    is_valid = False;
            except ValueError:
                print(Constants.ERROR_STATUS + ' Your option should be an integer number')
        return choice


# Class contains Constants
class Constants:
    # Format constants
    FORMAT_COLUMN = '| {:^8s} | {:^15s} | {:^5s} | {:^10s} | {:^20s} | {:^30s} |'
    FORMAT_RECORD = '| %-8s | %-15s | %-5s | %-10s | %-20s | %-30s |'
    FORMAT_EDGE = '+%-8s+%-15s+%-5s+%-10s+%-20s+%-30s+'

    # Status constants
    INFO_STATUS = '[ INFO ]'
    ERROR_STATUS = '[ ERROR ]'
    WARNING_STATUS = '[ WARNING ]'
