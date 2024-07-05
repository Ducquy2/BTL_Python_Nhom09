import sqlite3


class quanlydiemHeDH:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE ql_MonHoc (
                MaMH TEXT PRIMARY KEY,
                TenMH TEXT,
                SoTrinh INTEGER,
                HinhThucThi TEXT,
                HocKy INTEGER,
                PhongHoc TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Diem (
                MaSV TEXT,
                MonHoc TEXT,
                DiemLan1 REAL,
                DiemLan2 REAL,
                FOREIGN KEY(MonHoc) REFERENCES ql_MonHoc(MaMH)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Khoa (
                MaKhoa TEXT PRIMARY KEY,
                TenKhoa TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Lop (
                MaLop TEXT PRIMARY KEY,
                SoPhong INTEGER,
                TenMonHoc TEXT,
                TenGiangVien TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_HoSoSV (
                MaSV TEXT PRIMARY KEY,
                TenSV TEXT,
                Tuoi INTEGER,
                GioiTinh TEXT,
                DiaChi TEXT,
                Email TEXT,
                SDT TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_TaiKhoan (
                User TEXT PRIMARY KEY,
                Password TEXT,
                LoaiTaiKhoan TEXT CHECK(LoaiTaiKhoan IN ('Admin', 'SinhVien'))
            )
        """)

        self.conn.commit()

    def insert_data(self):
        self.cursor.executemany("""
                    INSERT INTO ql_MonHoc VALUES (?, ?, ?, ?, ?, ?)
                """, [
            ('MH01', 'Toán cao cấp', 4, 'Thi viết', 1, 'A101'),
            ('MH02', 'Triết', 3, 'Thi viết', 2, 'A102'),
            ('MH03', 'Lập trình Java', 4, 'Thi thực hành', 1, 'A101'),
            ('MH04', 'Python', 3, 'Thi viết', 2, 'A105'),
            ('MH05', 'Tư tưởng HCM', 2, 'Thi viết', 1, 'A601'),
            ('MH06', 'Tiếng anh CN', 2, 'Thi viết', 2, 'A401')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Diem VALUES (?, ?, ?, ?)
                """, [
            ('SVN01', 'MH01', 7.5, 8.0),
            ('SVN02', 'MH02', 8.0, 8.5),
            ('SVN03', 'MH03', 7.0, 7.5),
            ('SVN04', 'MH04', 8.5, 9.0),
            ('SVN05', 'MH05', 7.5, 8.0),
            ('SVN06', 'MH06', 8.0, 8.5)
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Khoa VALUES (?, ?)
                """, [
            ('K01', 'Khoa Công nghệ thông tin'),
            ('K02', 'Khoa Marketing'),
            ('K03', 'Khoa Du lịch'),
            ('K04', 'Khoa Oto'),
            ('K05', 'Khoa Dược'),
            ('K06', 'Khoa Luật')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Lop VALUES (?, ?, ?, ?)
                """, [
            ('L01', 101, 'Toán cao cấp', 'GV01'),
            ('L02', 102, 'Triết', 'GV02'),
            ('L03', 103, 'Lập trình Java', 'GV03'),
            ('L04', 104, 'Python', 'GV04'),
            ('L05', 105, 'Tư tưởng HCM', 'GV05'),
            ('L06', 106, 'Tiếng anh CN', 'GV06')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_HoSoSV VALUES (?, ?, ?, ?, ?, ?, ?)
                """, [
            ('SV01', 'Nguyễn Văn A', 20, 'Nam', 'Hà Nội', 'sv01@example.com', '0123456789'),
            ('SV02', 'Trần Thị B', 21, 'Nữ', 'Hải Phòng', 'sv02@example.com', '0123456790'),
            ('SV03', 'Phạm Văn C', 22, 'Nam', 'Đà Nẵng', 'sv03@example.com', '0123456709'),
            ('SV04', 'Lê Thị D', 23, 'Nữ', 'Cần Thơ', 'sv04@example.com', '0123456907'),
            ('SV05', 'Hoàng Văn E', 24, 'Nam', 'TP HCM', 'sv05@example.com', '0123456970'),
            ('SV06', 'Ngô Thị F', 25, 'Nữ', 'Nghệ An', 'sv06@example.com', '0123456798')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_TaiKhoan VALUES (?, ?, ?)
                """, [
            ('admin', 'admin123', 'Admin'),
            ('SV01', 'sv01@123', 'SinhVien'),
            ('SV02', 'sv02@123', 'SinhVien'),
            ('SV03', 'sv03@123', 'SinhVien'),
            ('SV04', 'sv04@123', 'SinhVien'),
            ('SV05', 'sv05@123', 'SinhVien'),
            ('SV06', 'sv06@123', 'SinhVien')
        ])

        self.conn.commit()


db = quanlydiemHeDH('ql_diemHeDH.db')
db.create_tables()
db.insert_data()
