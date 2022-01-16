from PySide2.QtWidgets import QApplication, QDialog, QFormLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QFileDialog, QRadioButton
from PySide2.QtCore import Qt
from mlv_app_logic import run_mlv

import os
import sys


class MLV_app(QDialog):
    def __init__(self):
        super(MLV_app, self).__init__()
        self.setWindowTitle("MLV Dumper")
        self.setMinimumSize(600, 400)
        
        self.in_path = ""
        self.out_path = ""
        self.first_frame =1
        self.last_frame = 1
        
        self.option = "dng"
        
        self.widgets()
        self.layouts()
        self.connections()
        
        
    def widgets(self):
        self.ln_file_path = QLineEdit()
        self.ln_file_path.setReadOnly(True)
        self.btn_file_search = QPushButton("...")
        
        self.ln_output_path = QLineEdit()
        self.ln_output_path.setReadOnly(True)
        self.btn_output_search = QPushButton("...")
        
        self.spn_first_frame = QSpinBox()
        self.spn_first_frame.setMaximum(10000)
        self.spn_first_frame.setMinimum(1)
        self.spn_last_frame = QSpinBox()
        self.spn_last_frame.setMaximum(10000)
        self.spn_last_frame.setMinimum(1)
        self.spn_last_frame.setValue(100)
        
        self.grp_chks = QGroupBox("Output Type")
        self.chk_dng = QRadioButton("DNG")
        self.chk_raw = QRadioButton("RAW")    
        self.chk_dng.setChecked(True)    
         
        self.chk_dng.setChecked(True) 
        
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
        self.grp_output.setAlignment(Qt.AlignRight)
        
        self.lyt_form_frames = QHBoxLayout()
        self.form_frames = QFormLayout()        
        self.form_frames.addRow("First Frame: " , self.spn_first_frame)
        self.form_frames.addRow("Last Frame: " , self.spn_last_frame)
        self.lyt_form_frames.addLayout(self.form_frames)
        self.lyt_form_frames.addStretch()
        
        self.lyt_buttons = QHBoxLayout()                      
        self.lyt_buttons.addWidget(self.btn_convert)
        self.lyt_buttons.addWidget(self.btn_cancel)
        self.lyt_buttons.addStretch()
        
        self.lyt_chks = QHBoxLayout()             
        self.lyt_chks.addWidget(self.chk_dng)  
        self.lyt_chks.addWidget(self.chk_raw)         
        self.grp_chks.setLayout(self.lyt_chks)
        self.lyt_chks.addStretch()                 
        
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.grp_file)
        self.lyt_main.addWidget(self.grp_output)    
        self.lyt_main.addLayout(self.lyt_form_frames)  
        self.lyt_main.addStretch()  
        self.lyt_main.addWidget(self.grp_chks) 
        self.lyt_main.addStretch()
        self.lyt_main.addLayout(self.lyt_buttons)          
        
        self.setLayout(self.lyt_main)
        
        
    def connections(self):
        self.btn_file_search.clicked.connect(self.lookup_dir)
        self.btn_output_search.clicked.connect(self.save_dir)
        self.spn_first_frame.valueChanged.connect(self.update_frames)
        self.spn_last_frame.valueChanged.connect(self.update_frames)
        
        self.btn_convert.clicked.connect(self.run_mlv_dump)
        self.btn_cancel.clicked.connect(self.close)
    
    
    def lookup_dir(self):
        
        filter = 'MLV File (*.MLV *.mlv)'
        
        files = []
        
        mlv_dir = QFileDialog.getOpenFileNames(self, "Select a MLV file. ", os.getcwd(), filter)[0]
        
        for f in mlv_dir:
            text = f.split("/")[-1]
            files.append(text)
        print(files)
            
        st = " - ".join(f for f in files)
            
        self.ln_file_path.setText(st)
        self.in_path = mlv_dir
        self.folder = mlv_dir    
        
        self.update_frames()    
        
        
        
        
    def update_frames(self):
        self.first_frame = self.spn_first_frame.text()
        self.last_frame = self.spn_last_frame.text()
        
        
    def save_dir(self):       
        
        output_dir = QFileDialog.getExistingDirectory(self, "Select Folder")        
        self.ln_output_path.setText(output_dir)
        self.folder = output_dir
        
        self.out_path = output_dir
        
        self.update_frames()
        
        print(output_dir)
        
        
    def run_mlv_dump(self):
        if self.chk_dng.isChecked():
            mode = 0
        if self.chk_raw.isChecked():
            mode = 1
        
        
        self.update_frames()
        run_mlv(self.in_path, self.out_path, int(self.first_frame), int(self.last_frame), mode)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MLV_app()
    w.show()
    
    sys.exit(app.exec_())