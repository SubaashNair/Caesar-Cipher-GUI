from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget
from PyQt6.QtCore import Qt

def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

class CipherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Decipher")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        # Encryption Section
        self.layout.addWidget(QLabel("--- ENCRYPTION ---", alignment=Qt.AlignmentFlag.AlignCenter))
        self.layout.addWidget(QLabel("Plain Text:"))
        self.e1 = QLineEdit()
        self.layout.addWidget(self.e1)
        self.layout.addWidget(QLabel("Shift:"))
        self.e2 = QLineEdit()
        self.layout.addWidget(self.e2)
        self.layout.addWidget(QLabel("Cipher Text:"))
        self.e3 = QLineEdit()
        self.layout.addWidget(self.e3)
        self.encrypt_button = QPushButton('Encrypt')
        self.encrypt_button.clicked.connect(self.encrypt_message)
        self.layout.addWidget(self.encrypt_button)

        # Decryption Section
        self.layout.addWidget(QLabel("--- DECRYPTION ---", alignment=Qt.AlignmentFlag.AlignCenter))
        self.layout.addWidget(QLabel("Cipher Text:"))
        self.e4 = QLineEdit()
        self.layout.addWidget(self.e4)
        self.layout.addWidget(QLabel("Shift:"))
        self.e5 = QLineEdit()
        self.layout.addWidget(self.e5)
        self.layout.addWidget(QLabel("Plain Text:"))
        self.e6 = QLineEdit()
        self.layout.addWidget(self.e6)
        self.decrypt_button = QPushButton('Decrypt')
        self.decrypt_button.clicked.connect(self.decrypt_message)
        self.layout.addWidget(self.decrypt_button)

    def encrypt_message(self):
        text = self.e1.text()
        shift = int(self.e2.text())
        self.e3.setText(encrypt(text, shift))

    def decrypt_message(self):
        text = self.e4.text()
        shift = int(self.e5.text())
        self.e6.setText(decrypt(text, shift))

app = QApplication([])
window = CipherApp()
window.show()
app.exec()