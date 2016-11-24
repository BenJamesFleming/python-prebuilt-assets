# © Ben Fleming
# TextInput Class
# Prebuilt Class To Let User Input Some Text
# View Examples For Help

# TODO: Add Filter Function

class TextInput():

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
    message = "Please Enter Input Here"

    # Function INIT
    # To Setup The Class
    # Variables
    # header as str;  String To Put In Frount Of The List
    # choices as arr; Array Of Choices For The User To Pick From
    def __init__(self, **kwargs):

        # Load The Variables Into The Class
        self.message = kwargs.get("message", self.message)

        return

    # Function Get Input
    # To Get User Input
    def getInput(self):

        # Choose The Right Input Method
        # Get The Input
        try:
            return raw_input(self.preFormat)
        except Exception:
            return input(self.preFormat)

    def flattenOutput(self, arr, **kwargs):

        # Variables
        end=""
        string=""

        for obj in [obj for obj in arr if type(obj) is str]:
            string += self.preFormat+str(obj)+kwargs.get("end", end)
        return string

    # Function Run
    # To Get User Input
    def get(self, **kwargs):

        # Load The Variables Into The Class
        self.message = kwargs.get("message", self.message)

        print(self.flattenOutput([self.message] if type(self.message) is str else self.message))
        return self.getInput()
