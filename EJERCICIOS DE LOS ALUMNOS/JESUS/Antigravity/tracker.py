import json
import os

DATA_FILE = "transactions.json"

def load_data():
    """Carga las transacciones desde el archivo JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(transactions):
    """Guarda las transacciones en el archivo JSON."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(transactions, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar los datos: {e}")

def add_transaction(transactions, transaction_type):
    """Añade una nueva transacción (ingreso o gasto)."""
    try:
        amount = float(input(f"Introduce la cantidad del {transaction_type}: "))
        if amount <= 0:
            print("La cantidad debe ser positiva.")
            return

        description = input(f"Introduce una descripción para el {transaction_type}: ").strip()
        
        # Si es gasto, guardamos como negativo internamente o usamos el tipo para diferenciar
        # Aquí guardaremos el tipo explícitamente y el monto siempre positivo, 
        # calculando el balance según el tipo.
        
        transaction = {
            "type": transaction_type, # "ingreso" o "gasto"
            "amount": amount,
            "description": description
        }
        
        transactions.append(transaction)
        save_data(transactions)
        print(f"{transaction_type.capitalize()} añadido correctamente.")
        
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número válido para la cantidad.")

def view_balance(transactions):
    """Calcula y muestra el balance total."""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "ingreso")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "gasto")
    balance = total_income - total_expense
    
    print("\n--- Balance Actual ---")
    print(f"Total Ingresos: {total_income:.2f} €")
    print(f"Total Gastos:   {total_expense:.2f} €")
    print(f"Balance Final:  {balance:.2f} €")
    print("----------------------")

def view_history(transactions):
    """Muestra el historial de todas las transacciones."""
    if not transactions:
        print("\nNo hay transacciones registradas.")
        return

    print("\n--- Historial de Transacciones ---")
    for i, t in enumerate(transactions, 1):
        sign = "+" if t["type"] == "ingreso" else "-"
        print(f"{i}. [{t['type'].upper()}] {t['description']}: {sign}{t['amount']:.2f} €")
    print("----------------------------------")

def main():
    transactions = load_data()
    
    while True:
        print("\n=== Control de Gastos e Ingresos ===")
        print("1. Añadir Ingreso")
        print("2. Añadir Gasto")
        print("3. Ver Balance")
        print("4. Ver Historial")
        print("5. Salir")
        
        option = input("\nSelecciona una opción: ")
        
        if option == "1":
            add_transaction(transactions, "ingreso")
        elif option == "2":
            add_transaction(transactions, "gasto")
        elif option == "3":
            view_balance(transactions)
        elif option == "4":
            view_history(transactions)
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
