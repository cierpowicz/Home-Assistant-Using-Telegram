
import os
#import gateway_flask_24
from src import esp_class
from gateway_flask_24 import Program_Flask



class ProgramMenager:
    def __init__(self):
        self.name = "test"
        self.numbers_runing_programs = 0
        self.bigest_len_word = 1
        self.program_list = []


    def print(self):
        return self.name


    def wazna_funkcja(self,program_pierwszy_polskiego_radia):
        print(program_pierwszy_polskiego_radia.return_hello())
        

    #
    # Print sectiorn (glownie jakies takie ladnie wzorki)
    #
    #
    # {"="*self.bigest_len_word}
    #
    #
    #

    def return_TOP_screen(self):
        return f"""
============================{"="*self.bigest_len_word}============================
| Program ID | Program Name{" "*self.bigest_len_word}| Status |   Last  Update   |
============================{"="*self.bigest_len_word}============================
"""
    
    def return_MIDLE_screen(self):
        return """|   000001   | siemanko to  | ACTIVE | 12:21 22.11.2023 |"""
    
    #
    # Clear console func
    #


    def clear_okienko(self):
        os.system('clear')




program_01 = ProgramMenager()

#esc_class_01 = Esp_Menager()

flask_class_01 = Program_Flask()


program_01.wazna_funkcja(flask_class_01)


def main():

    print(flask_class_01.return_hello())

    

main()