class Dompet:
    total_dompet = 0

    def __init__(self, kode_dompet, nama_pemilik, saldo_awal=0):
        self.__kode_dompet = kode_dompet
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal
        Dompet.total_dompet += 1

    @property
    def kode_dompet(self):
        return self.__kode_dompet

    @property
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai_baru):
        if nilai_baru >= 0:
            self.__saldo = nilai_baru
        else:
            print("Gagal: Saldo tidak boleh negatif!")

    def tampilkan_info(self):
        print(f"[{self.__kode_dompet}] Pemilik: {self.__nama_pemilik} | Saldo: Rp{self.__saldo:,}")

    @classmethod
    def info_total_dompet(cls):
        print(f"Total dompet terdaftar: {cls.total_dompet}")

    @staticmethod
    def validasi_kode(kode):
        return len(kode) == 5 and kode.startswith("DP")


class ManajemenKeuangan:
    def __init__(self, dompet):
        self.dompet = dompet
        self.riwayat_transaksi = []

    def catat_pemasukan(self, nominal, keterangan):
        if nominal <= 0:
            print("Nominal pemasukan harus lebih dari 0.")
            return
        self.dompet.saldo += nominal
        self.riwayat_transaksi.append(f"+ Rp{nominal:,} | Pemasukan: {keterangan}")
        print(f"Pemasukan Rp{nominal:,} tercatat. Saldo saat ini: Rp{self.dompet.saldo:,}")

    def catat_pengeluaran(self, nominal, keterangan):
        if nominal <= 0:
            print("Nominal pengeluaran harus lebih dari 0.")
            return
        if self.dompet.saldo >= nominal:
            self.dompet.saldo -= nominal
            self.riwayat_transaksi.append(f"- Rp{nominal:,} | Pengeluaran: {keterangan}")
            print(f"Pengeluaran Rp{nominal:,} tercatat. Sisa saldo: Rp{self.dompet.saldo:,}")
        else:
            print(f"Saldo tidak cukup! Saldo saat ini: Rp{self.dompet.saldo:,}")

    def tampilkan_riwayat(self):
        print(f"\n=== RIWAYAT TRANSAKSI ({self.dompet.nama_pemilik.upper()}) ===")
        if not self.riwayat_transaksi:
            print("Belum ada transaksi.")
        for item in self.riwayat_transaksi:
            print(item)
        print(f"Saldo Akhir: Rp{self.dompet.saldo:,}")


def jalankan_keuangan():
    kode_awal = "DP001"
    if not Dompet.validasi_kode(kode_awal):
        print("Kode dompet tidak valid!")
        return

    dompet_utama = Dompet(kode_awal, "Mahasiswa 3B", 500000)
    keuangan = ManajemenKeuangan(dompet_utama)

    while True:
        print("\n--- MENU KEUANGAN SEDERHANA ---")
        print("1. Cek Saldo & Info Dompet")
        print("2. Catat Pemasukan")
        print("3. Catat Pengeluaran")
        print("4. Lihat Riwayat Transaksi")
        print("5. Info Total Dompet")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            dompet_utama.tampilkan_info()
        elif pilihan == "2":
            ket = input("Keterangan pemasukan: ").strip()
            try:
                nominal = int(input("Nominal (Rp): ").strip())
                keuangan.catat_pemasukan(nominal, ket)
            except ValueError:
                print("Nominal harus berupa angka!")
        elif pilihan == "3":
            ket = input("Keterangan pengeluaran: ").strip()
            try:
                nominal = int(input("Nominal (Rp): ").strip())
                keuangan.catat_pengeluaran(nominal, ket)
            except ValueError:
                print("Nominal harus berupa angka!")
        elif pilihan == "4":
            keuangan.tampilkan_riwayat()
        elif pilihan == "5":
            Dompet.info_total_dompet()
        elif pilihan == "0":
            print("Program keuangan selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    jalankan_keuangan()