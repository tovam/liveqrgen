try:
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtCore import Qt
    import qrcode
    from PIL.ImageQt import ImageQt
except ImportError as e:
    print("Error: Missing required packages.")
    print("Please install them by running: pip install PyQt5 qrcode[pil]")
    sys.exit(1)

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.layout = QHBoxLayout()

        # Text area on the left
        self.text_area = QTextEdit()
        self.text_area.textChanged.connect(self.update_qrcode)
        self.layout.addWidget(self.text_area)

        # Image display on the right
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Set the layout for the main widget
        self.setLayout(self.layout)
        self.setWindowTitle("Live QR Code Generator")

        # Generate an initial QR code
        self.update_qrcode()

    def update_qrcode(self):
        # Get the text from the text area
        text = self.text_area.toPlainText()

        # Generate a QR code from the text
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Convert the image to a format that Qt can display
        qt_image = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_image)

        # Update the label with the QR code
        self.image_label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    qr_generator = QRCodeGenerator()
    qr_generator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
