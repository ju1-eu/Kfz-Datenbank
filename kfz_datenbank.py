import sys
import csv
import sqlite3
from PyQt5.QtWidgets import (QFileDialog, QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QMessageBox, QComboBox)

FELD_NAMES = ['Uebungsnummer', 'Fahrzeug', 'Problem', 'Fehlerspeicher', 'Besonderheit', 'Ursache']



class KfzDatenbank:
    def __init__(self):
        self.conn = sqlite3.connect('kfz.db')
        self.create_table()

    def _execute(self, query, args=None, commit=False):
        if args is None:
            args = ()
        with self.conn:
            result = self.conn.execute(query, args).fetchall()
            if commit:
                self.conn.commit()
            return result

    def create_table(self):
        columns = ", ".join([f"{name.lower()} TEXT" for name in FELD_NAMES])
        self._execute(f"CREATE TABLE IF NOT EXISTS kfz (id INTEGER PRIMARY KEY, {columns});", commit=True)

    def search_entries(self, field, term):
        return self._execute(f"SELECT * FROM kfz WHERE {field.lower()} LIKE ?", ('%' + term + '%',))


    def add_or_update_entry(self, *data_args, id_val=None):
        placeholders = ", ".join(["?" for _ in FELD_NAMES])
        if id_val:  # If id is provided
            self._execute(f"REPLACE INTO kfz (id, {', '.join(FELD_NAMES).lower()}) VALUES (?, {placeholders})", (id_val, *data_args), commit=True)
        else:
            self._execute(f"INSERT INTO kfz ({', '.join(FELD_NAMES).lower()}) VALUES ({placeholders})", data_args, commit=True)
    
    def update_entry(self, id_val, *args):
        placeholders = ", ".join([f"{name.lower()} = ?" for name in FELD_NAMES])
        self._execute(f"UPDATE kfz SET {placeholders} WHERE id=?", (*args, id_val), commit=True)

    def search_by_fahrzeug(self, term):
        return self._execute(f"SELECT * FROM kfz WHERE fahrzeug LIKE ?", ('%' + term + '%',))

    def search_by_uebungsnummer(self, term):
        return self._execute(f"SELECT * FROM kfz WHERE uebungsnummer LIKE ?", ('%' + term + '%',))

    def search_by_fehlerspeicher(self, term):
        print("SQL-Abfrage:", f"SELECT * FROM kfz WHERE fehlerspeicher LIKE '%{term}%'")
        print("Suche nach Fehlerspeicher:", term)
        return self._execute(f"SELECT * FROM kfz WHERE fehlerspeicher LIKE ?", ('%' + term + '%',))


    def get_all_entries(self):
        return self._execute("SELECT * FROM kfz")

    def remove_duplicates(self):
        columns = ", ".join(FELD_NAMES).lower()
        self._execute(f"CREATE TEMPORARY TABLE kfz_temp AS SELECT DISTINCT {columns} FROM kfz;", commit=True)
        self._execute("DELETE FROM kfz;", commit=True)
        self._execute(f"INSERT INTO kfz ({columns}) SELECT {columns} FROM kfz_temp;", commit=True)
        self._execute("DROP TABLE kfz_temp;", commit=True)
        
    def entry_exists(self, data_row):
        query_conditions = " AND ".join([f"{name.lower()} = ?" for name in FELD_NAMES[1:]])
        return self._execute(f"SELECT 1 FROM kfz WHERE {query_conditions}", data_row)

    def entry_with_id_exists(self, id_val):
        result = self._execute("SELECT 1 FROM kfz WHERE id=?", (id_val,))
        return len(result) > 0
    
    def delete_entry(self, id_val):
        self._execute("DELETE FROM kfz WHERE id=?", (id_val,), commit=True)

    def search_by_problem(self, term):
        return self._execute(f"SELECT * FROM kfz WHERE problem LIKE ?", ('%' + term + '%',))

    def search_by_besonderheit(self, term):
        return self._execute(f"SELECT * FROM kfz WHERE besonderheit LIKE ?", ('%' + term + '%',))

    def search_by_ursache(self, term):
        return self._execute(f"SELECT * FROM kfz WHERE ursache LIKE ?", ('%' + term + '%',))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.db = KfzDatenbank()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        row_idx = 0
        self.inputs = {}
        for idx, feld_name in enumerate(FELD_NAMES):
            label = QLabel(feld_name, self)
            line_edit = QLineEdit(self)
            layout.addWidget(label, row_idx, 0)
            layout.addWidget(line_edit, row_idx, 1)
            self.inputs[feld_name] = line_edit
            row_idx += 1

        self.id_input = QLineEdit(self)
        layout.addWidget(QLabel('ID (leer lassen zum Hinzufügen):'), row_idx, 0)
        layout.addWidget(self.id_input, row_idx, 1)
        row_idx += 1

        self.add_btn = QPushButton('Hinzufügen', self)
        self.add_btn.clicked.connect(self.add_entry_to_db)
        self.update_btn = QPushButton('Aktualisieren', self)
        self.update_btn.clicked.connect(self.update_entry_in_db)
        layout.addWidget(self.add_btn, row_idx, 0)
        layout.addWidget(self.update_btn, row_idx, 1)
        row_idx += 1

        self.search_criteria = QComboBox(self)
        self.search_criteria.addItems(FELD_NAMES)
        self.search_input = QLineEdit(self)
        self.search_btn = QPushButton('Suchen', self)
        self.search_btn.clicked.connect(self.search_entries)
        layout.addWidget(self.search_criteria, row_idx, 0)
        layout.addWidget(self.search_input, row_idx, 1)
        layout.addWidget(self.search_btn, row_idx, 2)
        row_idx += 1

        self.show_data_btn = QPushButton('Daten anzeigen', self)
        self.show_data_btn.clicked.connect(self.show_entries)
        layout.addWidget(self.show_data_btn, row_idx, 0, 1, 3)
        row_idx += 1

        self.text_display = QTextEdit(self)
        layout.addWidget(self.text_display, row_idx, 0, 1, 3)
        row_idx += 1

        self.import_btn = QPushButton('Importieren', self)
        self.import_btn.clicked.connect(self.import_from_csv)
        self.export_btn = QPushButton('Exportieren', self)
        self.export_btn.clicked.connect(self.export_to_csv)
        self.remove_duplicates_btn = QPushButton('Duplikate entfernen', self)
        self.remove_duplicates_btn.clicked.connect(self.remove_db_duplicates)
        layout.addWidget(self.import_btn, row_idx, 0)
        layout.addWidget(self.export_btn, row_idx, 1)
        layout.addWidget(self.remove_duplicates_btn, row_idx, 2)
        row_idx += 1

        self.delete_btn = QPushButton('Löschen', self)
        self.delete_btn.clicked.connect(self.delete_entry_from_db)
        layout.addWidget(self.delete_btn, row_idx, 0, 1, 3)
        
        # Nach Ihren anderen Widgets
        self.entries_layout = QVBoxLayout()
        layout.addLayout(self.entries_layout, row_idx, 0, 1, 3)
        row_idx += 1

        self.setLayout(layout)
        self.setWindowTitle('KFZ Datenbank')
        self.show_entries()  # Fügen Sie diese Zeile am Ende der Methode hinzu
        self.resize(700, 800)

        

    def add_entry_to_db(self):
        data = [widget.text() for widget in self.inputs.values()]
        # Validierung hinzufügen
        for entry in data:
            if not entry:  # Überprüfen, ob das Eingabefeld leer ist
                self._show_message_box("Fehler", "Alle Felder müssen ausgefüllt werden.", QMessageBox.Critical)
                return
        id_val = self.id_input.text()
        if id_val.isdigit():
            self.db.add_or_update_entry(*data, id_val=int(id_val))
        else:
            self.db.add_or_update_entry(*data)
        self.show_entries()

    def update_entry_in_db(self):
        update_id = self.id_input.text().strip()
        if not update_id.isdigit():  # Überprüfen, ob die ID eine Nummer ist
            self._show_message_box("Fehler", "ID muss eine Zahl sein.", QMessageBox.Critical)
            return
        if not self.db.entry_with_id_exists(update_id):
            self._show_message_box("Fehler", "Kein Eintrag mit dieser ID gefunden.", QMessageBox.Critical)
            return
        data = [widget.text().strip() for widget in self.inputs.values()]  # Verwendung von strip() um Leerzeichen am Anfang und Ende zu entfernen
        if not all(data):  # Überprüfung, ob alle Felder gefüllt sind
            self._show_message_box("Fehler", "Bitte füllen Sie alle Felder aus.", QMessageBox.Critical)
            return
        self.db.update_entry(update_id, *data)
        self.show_entries()


    def search_entries(self):
        self.text_display.clear()
        search_term = self.search_input.text()
        search_field = self.search_criteria.currentText()

        results = self.db.search_entries(search_field, search_term)

        if results:
            for entry in results:
                self.text_display.append(', '.join([str(entry[FELD_NAMES.index(feld_name)]) for feld_name in FELD_NAMES]))
                self.text_display.append('-' * 40)
        else:
            self.text_display.append("Keine Ergebnisse gefunden.")



    def _execute_db_operation(self, operation_func, *args, success_msg=None):
        try:
            operation_func(*args)
            if success_msg:
                self._show_message_box("Erfolg", success_msg)
            self.show_entries()
        except Exception as e:
            self._show_message_box("Fehler", str(e), QMessageBox.Critical)

    def import_from_csv(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV files (*.csv);;All files (*.*)")
        if filepath:
            self._execute_db_operation(self._import_csv_data, filepath, success_msg="CSV erfolgreich importiert.")

    def _import_csv_data(self, filepath):
        try:
            with open(filepath, "r", newline="", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=';')
                next(csv_reader)  # Überspringe die Kopfzeile
                for row in csv_reader:
                    if not self.db.entry_exists(row[1:]):
                        self.db.add_or_update_entry(*row)
                    else:
                        self._show_message_box("Eintrag existiert bereits", '; '.join(row), QMessageBox.Warning)
        except Exception as e:
            self._show_message_box("Fehler beim Importieren der CSV-Datei", str(e), QMessageBox.Critical)

    def export_to_csv(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV files (*.csv);;All files (*.*)")
        if filepath:
            self._execute_db_operation(self._export_csv_data, filepath, success_msg="CSV erfolgreich exportiert.")

    def _export_csv_data(self, filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=';')
            csv_writer.writerow(FELD_NAMES)
            for entry in self.db.get_all_entries():
                csv_writer.writerow(entry[1:])


    def delete_entry_from_db(self):
        delete_id = self.id_input.text()
        if delete_id.isdigit() and self.db.entry_with_id_exists(delete_id):
            self.db.delete_entry(delete_id)
            self.show_entries()
            self._show_message_box("Erfolg", "Eintrag erfolgreich gelöscht.")
        else:
            self._show_message_box("Fehler", "Kein Eintrag mit dieser ID gefunden.", QMessageBox.Critical)


    def show_entry_details(self, entry):
        details = ', '.join([str(entry[FELD_NAMES.index(feld_name)]) for feld_name in FELD_NAMES])
        self._show_message_box("Eintragsdetails", details)

    def remove_db_duplicates(self):
        self._execute_db_operation(self.db.remove_duplicates, success_msg="Duplikate erfolgreich entfernt.")

    def show_entries(self):
        self.text_display.clear()
        for entry in self.db.get_all_entries():
            self.text_display.append('; '.join([str(entry[FELD_NAMES.index(feld_name)]) for feld_name in FELD_NAMES]))
            self.text_display.append('-' * 40)


    def _show_message_box(self, title, message, icon=QMessageBox.Information):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
