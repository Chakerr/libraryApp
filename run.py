from operations import *
from db import init_db
from rich.console import Console
from rich.table import Table

init_db()
console = Console()

def mostrar_tabla(data, columnas):
    table = Table(show_header=True, header_style="bold magenta")
    for col in columnas:
        table.add_column(col)
    for row in data:
        table.add_row(*[str(cell) for cell in row])
    console.print(table)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar miembro")
        print("2. Listar miembros")
        print("3. Registrar libro")
        print("4. Listar libros")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Ver préstamos vencidos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            add_member(name, email)

        elif opcion == "2":
            miembros = list_members()
            mostrar_tabla(miembros, ["ID", "Nombre", "Email", "Fecha ingreso"])

        elif opcion == "3":
            title = input("Título: ")
            author = input("Autor: ")
            copies = int(input("Copias: "))
            add_book(title, author, copies)

        elif opcion == "4":
            libros = list_books()
            mostrar_tabla(libros, ["ID", "Título", "Autor", "Copias"])

        elif opcion == "5":
            member_id = int(input("ID del miembro: "))
            book_id = int(input("ID del libro: "))
            days = int(input("Días de préstamo: "))
            loan_book(member_id, book_id, days)

        elif opcion == "6":
            loan_id = int(input("ID del préstamo: "))
            return_book(loan_id)

        elif opcion == "7":
            vencidos = overdue_loans()
            mostrar_tabla(vencidos, ["ID", "Miembro", "Libro", "Vencimiento"])

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")

try:
    menu()
except KeyboardInterrupt:
    print("\nSaliendo...")