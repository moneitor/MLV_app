from PySide2.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout
from mlv_app_logic import run_mlv

import sys


class MLV_app(QDialog):
    def __init__(self):
        super(MLV_app, self).__init__()
        self.setWindowTitle("MLV Dumper")
        self.setMinimumSize(500, 150)
        
        self.widgets()
        self.layouts()
        self.connections()
        
        
    def widgets(self):
        self.ln_file_path = QLineEdit()
        self.btn_file_search = QPushButton("...")
        
        self.ln_output_path = QLineEdit()
        self.btn_output_search = QPushButton("...")
        
        self.btn_cancel = QPushButton("Cancel")
        self.btn_convert = QPushButton("Convert")
        
        
    def layouts(self):
        self.grp_file = QGroupBox("Input Path")
        self.lyt_file = QHBoxLayout()
        self.lyt_file.addWidget(self.ln_file_path)
        self.lyt_file.addWidget(self.btn_file_search)
        self.grp_file.setLayout(self.lyt_file)
        
        self.grp_output = QGroupBox("Output Path")
        self.lyt_output = QHBoxLayout()
        self.lyt_output.addWidget(self.ln_output_path)
        self.lyt_output.addWidget(self.btn_output_search)
        self.grp_output.setLayout(self.lyt_output)
        
        self.lyt_buttons = QHBoxLayout()
        self.lyt_buttons.addStretch()
        self.lyt_buttons.addWidget(self.btn_convert)
        self.lyt_buttons.addWidget(self.btn_cancel)
        
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.grp_file)
        self.lyt_main.addWidget(self.grp_output)
        self.lyt_main.addLayout(self.lyt_buttons)
        
        
        
        
        self.lyt_main.addStretch()
        
        self.setLayout(self.lyt_main)
        
        
    def connections(self):
        pass
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MLV_app()
    w.show()
    
    sys.exit(app.exec_())