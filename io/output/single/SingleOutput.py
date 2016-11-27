# © Ben Fleming
# SingleOutput Class
# Prebuilt Class To Let User Input Some Text
# View Examples For Help

class SingleOutput():

    # Global Variables
    # [START]
    global clear
    # [END]

    # Config Variables
    # preFormat as str;     The Format For The Output
    # clear as fuc;         Function To Clear The CLI
    # [START]
    preFormat = ">> "
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # fuc; Clear Command Line
    # [END]

    # User Variables
    outputstr = "SingleOutput Error: Failed To Get Message"

    # Function INIT
    # To Setup The Class
    # Variables
    # output as str;  String To Output To The Screen
    def __init__(self, **kwargs):

        # Load The Variables Into The Class
        self.outputstr = kwargs.get("output", self.outputstr)
        self.output()

        return

    def output(self):
        print(self.preFormat+self.outputstr)
