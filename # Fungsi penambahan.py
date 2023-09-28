# Fungsi penambahan
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak dapat dilakukan"

# Fungsi tree
def tree(expression):
    if isinstance(expression, tuple):  # Cek apakah ekspresi adalah tuple
        if len(expression) == 3:  # Ekspresi harus memiliki 3 elemen
            left, operator, right = expression
            if operator == '+':
                return add(tree(left), tree(right))
            elif operator == '-':
                return minus(tree(left), tree(right))
            elif operator == '*':
                return mult(tree(left), tree(right))
            elif operator == '/':
                return div(tree(left), tree(right))
            else:
                return "Error: Operator tidak valid"
        else:
            return "Error: Ekspresi tidak valid"
    else:
        return expression  # Jika ekspresi adalah angka, kembalikan angka tersebut

# Contoh pohon ekspresi : (2 +3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, "-", 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("\nHasil evaluasi pohon ekspresi:", result)
