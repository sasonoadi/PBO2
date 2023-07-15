CREATE TABLE `Petugas` (
	`kode_petugas` INT (11) NOT NULL AUTO_INCREMENT,
	`code_petugas` CHAR (11) NOT NULL UNIQUE,
	`nama` varchar (25)NOT NULL,
	`jk_petugas`ENUM ('L','P') DEFAULT'L' NOT NULL,
	`jabatan` varchar (11) NOT NULL,
	`no_telepon` char (15) NOT NULL,
	`alamat` varchar (30) NOT NULL,
	PRIMARY KEY (`kode_petugas`)
);

CREATE TABLE `Anggota` (
	`kode_anggota` INT (11) NOT NULL AUTO_INCREMENT,
	`code_anggota` CHAR (11) NOT NULL UNIQUE,
	`nama` varchar (25)NOT NULL,
	`jk_anggota`ENUM ('L','P') DEFAULT 'L',
	`jurusan` varchar (10)NOT NULL,
	`no_tlp` char (15)NOT NULL,
	`alamat` varchar (30) NOT NULL,
	PRIMARY KEY (`kode_anggota`)
);

CREATE TABLE `Buku` (
	`kode_buku` INT (11) NOT NULL AUTO_INCREMENT,
	`code_buku` CHAR (11) NOT NULL UNIQUE,
	`judul` varchar (20)NOT NULL,
	`penulis` varchar (20) NOT NULL,
	`penerbit` varchar (25) NOT NULL,
	`tahun_terbit` char (7) NOT NULL,
	`stok_buku` char (5) NOT NULL,
	PRIMARY KEY (`kode_buku`)
);

CREATE TABLE `Peminjaman` (
	`kode_kembali` INT (11) NOT NULL AUTO_INCREMENT,
	`code_pinjam` CHAR (11) NOT NULL UNIQUE,
	`tanggal_kembali` DATE NOT NULL,
	`batas_tgl_kembali` DATE NOT NULL,
	`denda_per_hari` INT (5) NOT NULL,
	`jumlah_hari` INT (5) NOT NULL,
	`total_denda` INT (10) NOT NULL,
	`kode_anggota` INT (11) NOT NULL,
	`kode_buku` INT (11) NOT NULL,
	`kode_petugas` INT (11) NOT NULL,
	PRIMARY KEY (`kode_kembali`)
);

CREATE TABLE `Pengembalian` (
	`kode_kembali` INT (11) NOT NULL AUTO_INCREMENT,
	`code_pengembalian` CHAR (11) NOT NULL UNIQUE,
	`tanggal_kembali` DATE NOT NULL,
	`batas_tgl_kembali` DATE NOT NULL,
	`denda_per_hari` INT (5) NOT NULL,
	`jumlah_hari` INT (5) NOT NULL,
	`total_denda` INT (10) NOT NULL,
	`kode_anggota` INT (11) NOT NULL,
	`kode_buku` INT (11) NOT NULL,
	`kode_petugas` INT (11) NOT NULL,
	PRIMARY KEY (`kode_kembali`)
);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk0` FOREIGN KEY (`kode_anggota`) REFERENCES `Anggota`(`kode_anggota`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk1` FOREIGN KEY (`kode_buku`) REFERENCES `Buku`(`kode_buku`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk2` FOREIGN KEY (`kode_petugas`) REFERENCES `Petugas`(`kode_petugas`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk0` FOREIGN KEY (`kode_anggota`) REFERENCES `Anggota`(`kode_anggota`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk1` FOREIGN KEY (`kode_buku`) REFERENCES `Buku`(`kode_buku`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk2` FOREIGN KEY (`kode_petugas`) REFERENCES `Petugas`(`kode_petugas`);






