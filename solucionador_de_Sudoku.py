print("=======================================")
print("Bienvenido(a) al solucionador de Sudoku")
print("=======================================\n")

sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def print_sudoku(sudoku): 
    for l in sudoku:
        print(l)

def encontrar_coordenada_grid(val):
    if val <= 2:
        return 0
    elif val <= 5:
        return 1
    else:
        return 2

def obtener_grid_para_celda(x, y, sudoku):
    subgrid_col = encontrar_coordenada_grid(x)
    subgrid_fila = encontrar_coordenada_grid(y)
    
    grid = []
    for fila in sudoku[subgrid_fila *3: subgrid_fila *3 + 3]:
        for col in fila[subgrid_col *3: subgrid_col *3 + 3]:
            grid.append(col)
            
    return grid


def revision_celdas (x, y, valor_rc, sudoku):
    # Revisar la fila
    if valor_rc in sudoku[y]:
        return False
    
    # Revisar la columna
    col = [fila[x] for fila in sudoku]
    if valor_rc in col:
        return False
    
    # Revisar sub grid 3x3
    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if valor_rc in grid3x3:
        return False
    
    return True

print("La solución es:\n")

def resolver_sudoku(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if revision_celdas (x, y, valor, sudoku):
                        sudoku[y][x] = valor
                        resolver_sudoku(sudoku)
                        sudoku[y][x] = 0
                return
    print_sudoku(sudoku)
    return


if __name__ == "__main__":
    resolver_sudoku(sudoku)


