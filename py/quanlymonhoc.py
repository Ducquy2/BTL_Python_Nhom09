# Form implementation generated from reading ui file 'quanlymonhoc.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
from tkinter import messagebox

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Quanlymonhoc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 576)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QuanLyMonHoc = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.QuanLyMonHoc.setGeometry(QtCore.QRect(50, 20, 671, 351))
        self.QuanLyMonHoc.setObjectName("QuanLyMonHoc")
        self.QuanLyMonHoc.setColumnCount(6)
        self.QuanLyMonHoc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.QuanLyMonHoc.setHorizontalHeaderItem(5, item)
        self.btnThem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnThem.setGeometry(QtCore.QRect(760, 70, 91, 41))
        self.btnThem.setObjectName("btnThem")
        self.btnSua = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSua.setGeometry(QtCore.QRect(760, 130, 91, 41))
        self.btnSua.setObjectName("btnSua")
        self.btnXoa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnXoa.setGeometry(QtCore.QRect(760, 190, 91, 41))
        self.btnXoa.setObjectName("btnXoa")
        self.btnDSMH = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDSMH.setGeometry(QtCore.QRect(760, 250, 91, 41))
        self.btnDSMH.setObjectName("btnDSMH")
        self.txtMamh = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtMamh.setGeometry(QtCore.QRect(110, 390, 141, 31))
        self.txtMamh.setObjectName("txtMamh")
        self.txtTenMH = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTenMH.setGeometry(QtCore.QRect(110, 440, 141, 31))
        self.txtTenMH.setObjectName("txtTenMH")
        self.txtSoTrinh = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtSoTrinh.setGeometry(QtCore.QRect(110, 490, 141, 31))
        self.txtSoTrinh.setObjectName("txtSoTrinh")
        self.txtHtt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtHtt.setGeometry(QtCore.QRect(500, 390, 141, 31))
        self.txtHtt.setObjectName("txtHtt")
        self.txtHocKy = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtHocKy.setGeometry(QtCore.QRect(500, 440, 141, 31))
        self.txtHocKy.setObjectName("txtHocKy")
        self.txtPhongHoc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtPhongHoc.setGeometry(QtCore.QRect(500, 490, 141, 31))
        self.txtPhongHoc.setObjectName("txtPhongHoc")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 400, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 450, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 500, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 400, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 450, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 500, 61, 16))
        self.label_6.setObjectName("label_6")
        self.btnTim = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTim.setGeometry(QtCore.QRect(760, 310, 91, 41))
        self.btnTim.setObjectName("btnTim")
        self.btnReset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(760, 370, 91, 41))
        self.btnReset.setObjectName("btnReset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_data()
        self.btnTim.clicked.connect(self.tim_kiem)
        self.btnThem.clicked.connect(self.Add_MH)
        self.QuanLyMonHoc.itemDoubleClicked.connect(self.Hien_thi)
        self.btnSua.clicked.connect(self.Sua_MH)
        self.btnXoa.clicked.connect(self.Xoa_MH)
        self.btnReset.clicked.connect(self.Load_dulieu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuanLyMonHoc"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Môn Học"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên Môn Học"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số Trình"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hình Thức Thi"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Học Kỳ"))
        item = self.QuanLyMonHoc.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phòng Học"))
        self.btnThem.setText(_translate("MainWindow", "Thêm"))
        self.btnSua.setText(_translate("MainWindow", "Sửa"))
        self.btnXoa.setText(_translate("MainWindow", "Xóa"))
        self.btnDSMH.setText(_translate("MainWindow", "Danh sách môn"))
        self.label.setText(_translate("MainWindow", "Mã môn học"))
        self.label_2.setText(_translate("MainWindow", "Tên môn học"))
        self.label_3.setText(_translate("MainWindow", "Số trình"))
        self.label_4.setText(_translate("MainWindow", "Hình thức thi"))
        self.label_5.setText(_translate("MainWindow", "Học kỳ"))
        self.label_6.setText(_translate("MainWindow", "Phòng học"))
        self.btnTim.setText(_translate("MainWindow", "Tìm môn học"))
        self.btnReset.setText(_translate("MainWindow", "Làm mới"))

    def load_data(self):
        conn = sqlite3.connect('ql_diemHeDH.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM ql_MonHoc''')
        monhoc = cursor.fetchall()

        self.QuanLyMonHoc.setRowCount(len(monhoc))
        for row_index, row_data in enumerate(monhoc):
            for col_index, col_data in enumerate(row_data):
                self.QuanLyMonHoc.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col_data)))

        conn.close()

    def Load_dulieu(self):
        # Xóa nội dung trong các lineEdit
        self.txtMamh.clear()
        self.txtTenMH.clear()
        self.txtSoTrinh.clear()
        self.txtHtt.clear()
        self.txtHocKy.clear()
        self.txtPhongHoc.clear()

        self.load_data()


    def tim_kiem(self):
        maMH = self.txtMamh.text()
        tenMH = self.txtTenMH.text()
        soTrinh = self.txtSoTrinh.text()
        hinhThucThi = self.txtHtt.text()
        hocKy = self.txtHocKy.text()
        phongHoc = self.txtPhongHoc.text()

        # Xóa dữ liệu hiện có trong tableWidget
        self.QuanLyMonHoc.clearContents()

        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect('ql_diemHeDH.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM ql_MonHoc WHERE MaMH LIKE ? AND TenMH LIKE ? AND SoTrinh LIKE ? AND HinhThucThi LIKE ? AND "
            "HocKy LIKE ? AND PhongHoc LIKE ?",
            ('%' + maMH + '%', '%' + tenMH + '%', '%' + soTrinh + '%',
             '%' + hinhThucThi + '%',
             '%' + hocKy + '%', '%' + phongHoc + '%'))
        monhoc = cursor.fetchall()

        if not monhoc:
            # Hiển thị thông báo "Không có môn học nào"
            self.QuanLyMonHoc.setRowCount(0)
            messagebox.showinfo('Thông báo', 'Không có môn học nào phù hợp.')
            self.load_data()
        else:
            # Hiển thị danh sách môn học
            self.QuanLyMonHoc.setRowCount(len(monhoc))
            for row_index, row_data in enumerate(monhoc):
                for col_index, col_data in enumerate(row_data):
                    self.QuanLyMonHoc.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col_data)))


        conn.close()

    def Add_MH(self):
        maMH = self.txtMamh.text()
        tenMH = self.txtTenMH.text()
        soTrinh = self.txtSoTrinh.text()
        hinhThucThi = self.txtHtt.text()
        hocKy = self.txtHocKy.text()
        phongHoc = self.txtPhongHoc.text()

        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect('ql_diemHeDH.db')
        cursor = conn.cursor()

        # Thêm dữ liệu vào bảng "mon_hoc"
        cursor.execute("SELECT COUNT(*) FROM ql_MonHoc WHERE `MaMH` = ?", (maMH,))
        existing_count = cursor.fetchone()[0]

        if existing_count > 0:
            messagebox.showinfo('Thông báo', 'Tên môn học đã tồn tại')
        else:
            # Thêm dữ liệu vào bảng "mon_hoc"
            cursor.execute(
                "INSERT INTO ql_MonHoc (`MaMH`, `TenMH`, `SoTrinh`, `HinhThucThi`, `HocKy`, `PhongHoc`) VALUES (?, ?, ?, ?, ?, ?)",
                (maMH, tenMH, soTrinh, hinhThucThi, hocKy, phongHoc))
            conn.commit()
            messagebox.showinfo('Thông báo', 'Thêm thành công môn học')
        conn.close()
        self.load_data()

    def Hien_thi(self, item):
        # Lấy thông tin hàng được chọn trong tableWidget
        selected_row = item.row()
        maMH = self.QuanLyMonHoc.item(selected_row, 0).text()
        tenMH = self.QuanLyMonHoc.item(selected_row, 1).text()
        soTrinh = self.QuanLyMonHoc.item(selected_row, 2).text()
        hinhThucThi = self.QuanLyMonHoc.item(selected_row, 3).text()
        hocKy = self.QuanLyMonHoc.item(selected_row, 4).text()
        phongHoc = self.QuanLyMonHoc.item(selected_row, 5).text()

        # Hiển thị giá trị trong các lineEdit
        self.txtMamh.setText(maMH)
        self.txtTenMH.setText(tenMH)
        self.txtSoTrinh.setText(soTrinh)
        self.txtHtt.setText(hinhThucThi)
        self.txtHocKy.setText(hocKy)
        self.txtPhongHoc.setText(phongHoc)

    def Sua_MH(self, item):
        # Lấy giá trị từ các lineEdit
        maMH = self.txtMamh.text()
        tenMH = self.txtTenMH.text()
        soTrinh = self.txtSoTrinh.text()
        hinhThucThi = self.txtHtt.text()
        hocKy = self.txtHocKy.text()
        phongHoc = self.txtPhongHoc.text()

        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect('ql_diemHeDH.db')
        cursor = conn.cursor()

        # Sửa dữ liệu trong bảng "mon_hoc"
        cursor.execute("UPDATE ql_MonHoc SET TenMH=?, SoTrinh=?, HinhThucThi=?, HocKy=?, PhongHoc=? WHERE MaMH=?",
                       (tenMH, soTrinh, hinhThucThi, hocKy, phongHoc, maMH))
        conn.commit()
        messagebox.showinfo('Thông báo', 'Sửa thành công môn học')

        # Cập nhật lại dữ liệu trong tableWidget
        conn.close()
        self.load_data()

    def Xoa_MH(self):
        # Lấy thông tin hàng được chọn trong tableWidget
        selected_row = self.QuanLyMonHoc.currentRow()
        if selected_row == -1:
            messagebox.showinfo(self, "Lỗi", "Vui lòng chọn một hàng để xóa.")
            return

        # Lấy giá trị từ cột "MaMH" trong hàng được chọn
        maMH = self.QuanLyMonHoc.item(selected_row, 0).text()

        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect('ql_diemHeDH.db')
        cursor = conn.cursor()

        # Xóa dữ liệu trong bảng "mon_hoc"
        cursor.execute("DELETE FROM ql_MonHoc WHERE MaMH=?", (maMH,))
        conn.commit()
        messagebox.showinfo('Thông báo', 'Xóa thành công môn học')

        # Cập nhật lại dữ liệu trong tableWidget
        conn.close()
        self.load_data()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Quanlymonhoc()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

