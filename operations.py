import sqlite3
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

DB_PATH = "data/library.db"

def add_member(name, email):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
            logging.info(f"Miembro registrado: {name} ({email})")
    except sqlite3.IntegrityError:
        print("⚠️ Email duplicado. No se puede registrar el miembro.")

def list_members():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id, name, email, join_date FROM members")
        return c.fetchall()
    
def add_book(title, author, copies):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO books (title, author, copies) VALUES (?, ?, ?)", (title, author, copies))
            logging.info(f"Libro registrado: {title} de {author}, {copies} copias")
    except sqlite3.IntegrityError:
        print("⚠️ Error al registrar el libro.")

def list_books():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id, title, author, copies FROM books")
        return c.fetchall()
    
def loan_book(member_id, book_id, days):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT copies FROM books WHERE id=?", (book_id,))
            result = c.fetchone()

            if not result:
                print("⚠️ El libro no existe.")
                return

            if result[0] <= 0:
                print("⚠️ No hay copias disponibles.")
                return

            due_date = (datetime.now() + timedelta(days=days)).date()
            c.execute("INSERT INTO loans (member_id, book_id, due_date) VALUES (?, ?, ?)", (member_id, book_id, due_date))
            c.execute("UPDATE books SET copies = copies - 1 WHERE id = ?", (book_id,))
            logging.info(f"Libro prestado: libro {book_id} a miembro {member_id}, vencimiento {due_date}")
    except sqlite3.IntegrityError:
        print("⚠️ Error al registrar el préstamo.")

def return_book(loan_id):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT book_id FROM loans WHERE id=? AND return_date IS NULL", (loan_id,))
        result = c.fetchone()

        if not result:
            print("⚠️ Préstamo no encontrado o ya devuelto.")
            return

        book_id = result[0]
        return_date = datetime.now().date()

        c.execute("UPDATE loans SET return_date=? WHERE id=?", (return_date, loan_id))
        c.execute("UPDATE books SET copies = copies + 1 WHERE id=?", (book_id,))
        logging.info(f"Libro devuelto: préstamo {loan_id}, libro {book_id}")

def overdue_loans():
    today = datetime.now().date()
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            SELECT loans.id, members.name, books.title, loans.due_date 
            FROM loans 
            JOIN members ON loans.member_id = members.id 
            JOIN books ON loans.book_id = books.id 
            WHERE loans.return_date IS NULL AND loans.due_date < ?
        """, (today,))
        return c.fetchall()