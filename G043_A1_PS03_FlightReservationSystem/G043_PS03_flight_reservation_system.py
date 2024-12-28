def initiateFlightSystem(read_input_file):
    """
     Reads the input file and creates a flight reservation system and all associated data structures,
     calling the necessary functions as mentioned in the input file.
        Input: Input file name with path.
        Output: None.
     """
    pass
def addFlight(flight_string=""):
    """
    Creates a flight along with a unique Flight-ID and adds it to the reservation system.
    Input: Flight string (e.g., flight destination, details).
    Output: "ADDED:<Unique Flight-ID> - <Flight String>"
    """
    pass
def removeFlight(flight_string="", flight_id=""):
    """
    Removes a flight along with a unique Flight-ID from the reservation system.
    Input: Flight string or Flight-ID.
    Output: "REMOVED:<Unique Flight-ID> - <Flight String>"
    """
    pass
def searchFlight(search_string=""):
    """
    Searches for a flight and returns the associated Flight-ID.
    Input: Flight string or Flight-ID.
    Output: "SEARCHED:<Search String> \n----------------------------------------\n<Flight-ID> - <Flight String>"
    """
    pass

def bookFlight(flight_string="", flight_id=""):
    """
    Marks a flight as booked and returns a confirmation.
    Input: Flight string or Flight-ID.
    Output: "BOOKED:<Unique Flight-ID> - <Flight String>"
    """
    pass


def unbookFlight(flight_string="", flight_id=""):
    """
    Marks a flight as available (unbooked).
    Input: Flight string or Flight-ID.
    Output: "UNBOOKED:<Unique Flight-ID> - <Flight String>"
    """
    pass

def statusFlight():
    """
    Displays the status of all flights (Booked and Available).
    Input: None.
    Output: "FLIGHT STATUS:\n--------------------------------------------------\n<Flight-ID> -<Flight String> - <Status (Booked/Available)>"
    """
    pass
