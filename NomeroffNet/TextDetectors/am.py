from .base import OCR


class Am(OCR):
    def __init__(self):
        OCR.__init__(self)
        self.letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.max_text_len = 7
        self.max_plate_length = 7
        self.letters_max = len(self.letters)+1
        self.label_length = 32 - 2

        self.init_label_converter()


am = Am()
