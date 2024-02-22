from BPNeurode import BPNeurode
from FFNeurode import FFNeurode


class FFBPNeurode(FFNeurode, BPNeurode):
    """Creating class FFBPNeurode."""
    pass
    # def __init__(self):
    #     """Initialize an instance of FFBPNeurode Class.
    #      Parameters: None.
    #      """
    #     super().__init__()


print(FFBPNeurode.mro())
