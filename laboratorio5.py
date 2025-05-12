class AnalizadorLexico:
    def _init_(self):
        self.tokens = []
        self.errores = []

    def es_digito(self, char):
        return '0' <= char <= '9'

    def es_letra_mayuscula(self, char):
        return 'A' <= char <= 'Z'

    def es_hex_digito(self, char):
        return self.es_digito(char) or ('A' <= char <= 'F')

    def es_espacio(self, char):
        return char in {' ', '\t', '\n', '\r'}

    def analizar_credito(self, codigo, i):
        n = len(codigo)
        if i + 3 >= n or codigo[i:i + 3] != 'CRE':
            return i, None

        i += 3
        num_str = ""

        while i < n and self.es_digito(codigo[i]):
            num_str += codigo[i]
            i += 1

        if not num_str:
            return i, None

        numero = int(num_str)
        if numero <= 0 or numero >= 90:
            return i, None

        return i, ('crédito', f"CRE{num_str}")

    def analizar_hexadecimal(self, codigo, i):
        n = len(codigo)
        num_str = ""

        while i < n and self.es_hex_digito(codigo[i]):
            num_str += codigo[i]
            i += 1

        if i + 2 >= n or codigo[i:i + 3] != 'x00':
            return i, None

        i += 3

        if not num_str:
            num_str = "0"

        return i, ('Numero hexadecimal', num_str)

    def analizar_numero(self, codigo, i):
        n = len(codigo)
        num_str = ""
        es_real = False
        tiene_digitos = False

        while i < n:
            if self.es_digito(codigo[i]):
                num_str += codigo[i]
                i += 1
                tiene_digitos = True
            elif codigo[i] == '.':
                if es_real:
                    break  # Detenerse si ya se encontró un punto
                es_real = True
                num_str += codigo[i]
                i += 1
            else:
                break

        if not tiene_digitos:
            return i, None

        if es_real:
            if num_str[-1] == '.':
                return i, None
            return i, ('constante real', num_str)
        else:
            return i, ('Constante entera', num_str)

    def analizar(self, codigo):
        i = 0
        n = len(codigo)

        while i < n:
            char = codigo[i]

            if self.es_espacio(char):
                i += 1
                continue

            # Intentar crédito
            j, token = self.analizar_credito(codigo, i)
            if token:
                self.tokens.append(token)
                i = j
                continue

            # Intentar número decimal
            j, token = self.analizar_numero(codigo, i)
            if token:
                self.tokens.append(token)
                i = j
                continue

            # Manejar caso como ".36" => "0.36"
            if char == '.' and i + 1 < n and self.es_digito(codigo[i + 1]):
                j, token = self.analizar_numero('0' + codigo[i:], 0)
                if token:
                    self.tokens.append(token)
                    i += j - 1  # Ajuste para posición correcta
                    continue

            # Intentar hexadecimal
            if self.es_hex_digito(char):
                j, token = self.analizar_hexadecimal(codigo, i)
                if token:
                    self.tokens.append(token)
                    i = j
                    continue

            # Manejar 'x' y '00'
            if char == 'x':
                self.errores.append(('error', 'x'))
                i += 1
                continue

            if i + 1 < n and codigo[i] == '0' and codigo[i + 1] == '0':
                self.tokens.append(('Constante entera', '00'))
                i += 2
                continue

            # Carácter no reconocido
            self.errores.append(('error', char))
            i += 1

    def imprimir_resultados(self):
        for token in self.tokens:
            print(f"{token[1]} {token[0]}")

        for error in self.errores:
            print(f"{error[1]} {error[0]}")


if _name_ == "_main_":
    analizador = AnalizadorLexico()
    codigo_ejemplo = input("entrada a analizar: ")

    analizador.analizar(codigo_ejemplo)
    analizador.imprimir_resultados()
