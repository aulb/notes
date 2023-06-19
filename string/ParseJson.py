from enum import Enum
class StringStates(Enum):
    NEW = 0
    BUILDING_KEY = 1
    END_OF_KEY = 2
    BUILDING_VAL = 3
    END_OF_VAL = 4

class JSONParser:
    def __init__(self, string):
        # Always "{}" -> ignored
        # \".*\":[true|false|null|".*"|[0-9]*],
        self.string = string[1:-1] # Assume string is ok
        self.result = {}
        self.__reset_states()
        self.__parse()

    def __reset_states(self):
        self.__parse_state = StringStates.NEW
        self.__current_val_is_string = False
        self.__current_key = ""
        self.__current_val = ""

    def __get_actual_current_value(self):
        if self.__current_val_is_string: return self.__current_val
        elif self.__current_val == "true": return True
        elif self.__current_val == "false": return False
        elif self.__current_val == "null": return None
        else: return int(self.__current_val)
    
    def __commit_to_result(self):
        self.__parse_state = StringStates.NEW
        self.result[self.__current_key] = self.__get_actual_current_value()
        self.__reset_states()
    
    def __parse(self):
        # if its " => either start key/val or part of key/val -> also value string
            # Simplify, no " or backspaces for now
        # if : -> depending on the state -> ignore or part of key/val
        # if , -> depending on the state -> commit or part of key/val
        # if empty_space -> depending on the state -> ignore or part of key/val
            # Simplify, no. 
        # is any other -> part of key/val 
        if len(self.string) == 0: return
        for char in self.string:
            if char == "\"":
                if self.__parse_state == StringStates.NEW:
                    self.__parse_state = StringStates.BUILDING_KEY
                elif self.__parse_state == StringStates.BUILDING_KEY:
                    self.__parse_state = StringStates.END_OF_KEY
                elif self.__parse_state == StringStates.END_OF_KEY:
                    self.__current_val_is_string = True
                    self.__parse_state = StringStates.BUILDING_VAL
                elif self.__parse_state == StringStates.BUILDING_VAL:
                    self.__parse_state = StringStates.END_OF_VAL
            elif char == ":" or char == ",":
                if char == "," and self.__parse_state == StringStates.END_OF_VAL:
                    self.__commit_to_result()
                if char == "," and self.__parse_state == StringStates.BUILDING_VAL:
                    if self.__current_val_is_string:
                        self.__current_val += char
                    else:
                        self.__commit_to_result()
                elif self.__parse_state == StringStates.BUILDING_KEY:
                    self.__current_key += char
                elif self.__parse_state == StringStates.BUILDING_VAL:
                    self.__current_val += char
            else:
                if self.__parse_state == StringStates.BUILDING_KEY:
                    self.__current_key += char
                elif self.__parse_state in [StringStates.END_OF_KEY, StringStates.BUILDING_VAL]:
                    self.__parse_state = StringStates.BUILDING_VAL
                    self.__current_val += char
        self.__commit_to_result()

def printing(testCase):
    print(JSONParser(testCase).result)

if __name__ == "__main__":
    # Identify states
    # Identify/learn the input. For example JSON string has a specific pattern
    # Identify places where you need to simplify to unblock
    printing('{"hello":true,"world":"false"}')
    printing('{"hello":true,"":"false"}')
    printing('{"":true,"":""}')
    printing('{"hello":true,"wor;:ld":"   "}')
    printing('{"hel,lo":19,"world":null}')
    printing('{"hel,lo":19,"world":null}')
    printing('{}')