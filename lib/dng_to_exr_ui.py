from PySide2.QtWidgets import QApplication, QDialog, QFormLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QFileDialog, QRadioButton, QProgressBar
from PySide2.QtWidgets import QListView, QAbstractItemView, QTreeView
from PySide2.QtCore import Qt
from dng_to_exr_logic import convert_all_dngs_to_exr

import os
import sys


class DNG_EXR_app(QDialog):
    def __init__(self):
        super(DNG_EXR_app, self).__init__()
        self.setWindowTitle("DNG to EXR")
        self.setMinimumSize(600, 300)
        
        self.in_path = ""
        self.out_path = ""
        self.first_frame =1
        self.last_frame = 1
        
        self.option = "dng"
        
        self.folders = []
        
        self.widgets()
        self.layouts()
        self.connections()
        
        
    def widgets(self):
        self.ln_file_path = QLineEdit()
        self.ln_file_path.setReadOnly(True)
        self.btn_file_search = QPushButton("Folder")
        
        self.pb_progress = QProgressBar()              
        
        self.spn_first_frame = QSpinBox()
        self.spn_first_frame.setMaximum(10000)
        self.spn_first_frame.setMinimum(1)
        self.spn_last_frame = QSpinBox()
        self.spn_last_frame.setMaximum(10000)
        self.spn_last_frame.setMinimum(1)
        self.spn_last_frame.setValue(100)       

        
        self.btn_cancel = QPushButton("Cancel")
        self.btn_convert = QPushButton("Convert")
        
        
    def layouts(self):
        self.grp_file = QGroupBox("Input Path")
        self.lyt_file = QHBoxLayout()
        self.lyt_file.addWidget(self.ln_file_path)
        self.lyt_file.addWidget(self.btn_file_search)
        self.grp_file.setLayout(self.lyt_file)
        
        self.grp_output = QGroupBox("Progress")        
        self.lyt_output = QHBoxLayout()
        self.lyt_output.addWidget(self.pb_progress)
        self.grp_output.setLayout(self.lyt_output)
        self.grp_output.setAlignment(Qt.AlignLeft)
                
        self.lyt_buttons = QHBoxLayout()                      
        self.lyt_buttons.addWidget(self.btn_convert)
        self.lyt_buttons.addWidget(self.btn_cancel)
        self.lyt_buttons.addStretch()

        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.grp_file)
        self.lyt_main.addWidget(self.grp_output)    
        self.lyt_main.addStretch()
        self.lyt_main.addLayout(self.lyt_buttons)          
        
        self.setLayout(self.lyt_main)
        
        
    def connections(self):
        self.btn_file_search.clicked.connect(self.lookup_dir)        
        self.btn_convert.clicked.connect(self.dng_to_exr)
        self.btn_cancel.clicked.connect(self.close)  
    

    
    def lookup_dir(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QListView, 'listView')

        # to make it possible to select multiple directories:
        if file_view:
            file_view.setSelectionMode(QAbstractItemView.MultiSelection)
        f_tree_view = file_dialog.findChild(QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)

        if file_dialog.exec():
            paths = file_dialog.selectedFiles()
            
        if len(paths) > 1:
            self.folders = paths.pop(0)
            
        self.folders = paths
        
        folder_names = [os.path.basename(name) for name in paths]
        st = "   --   ".join(f for f in folder_names)
        
        print(folder_names)
        
        filter = 'DNG File (*.DNG *.dng)'
        
        #dng_dir = QFileDialog.getExistingDirectory(self, "Select a MLV file. ", filter)      

        if len(paths) > 1:
            self.ln_file_path.setText(st)
        else:
            self.ln_file_path.setText(paths[0])       

        
    def save_dir(self):       
        
        output_dir = QFileDialog.getExistingDirectory(self, "Select Folder")        
        self.ln_output_path.setText(output_dir)
        self.folder = output_dir
        
        self.out_path = output_dir        
        
        print(output_dir)
        
        
    def dng_to_exr(self):
        for folder in self.folders:
            output_path = folder + "_EXR"
            convert_all_dngs_to_exr(folder, output_path, self.pb_progress)
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = DNG_EXR_app()
    w.show()
    
    sys.exit(app.exec_())