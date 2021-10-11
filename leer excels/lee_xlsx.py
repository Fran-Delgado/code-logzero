import pandas as pd
import os

path = "C:\\Users\\f.delgadomartinez\\Desktop\\ARSB\\2021-09-15 - DUAL RUN decode and compare\\PLANIFICACION Y DISEÑO"
fichero = "CBUKPRE_list_excluded_columns_20210920.xlsx"

xls=os.path.join(path,fichero)
sheet = "CBUKPRE_list_excluded_columns_2"


#######################################################################################################
# Funciones para:
# Extraer información del excel con campos a excluir de ordenaciones y comparaciones. 
# Cargar lista de exclusiones a considerar en función del esquema que estamos tratando
# Generar la lista de campos finales a tener en consideración
#######################################################################################################

def extraer_info_excel(xls,sheet):
    df = pd.read_excel(io = xls, sheet_name= sheet,)

    owner_excel  = df['OWNER'].tolist()
    campo_excel  = df['COLUMN_NAME'].tolist()
    # Para la columna de tablas, eliminamos los "_" porque las tablas en los esquemas vienen informadas sin guiones.
    tabla_excel_temp  = df['TABLE_NAME'].tolist()
    tabla_excel=[]
    for string in tabla_excel_temp:
        new_string=string.replace("_","")
        tabla_excel.append(new_string)
    return owner_excel,tabla_excel,campo_excel

def cargar_lista_exc(tabla_oracle,xls_tablas,xls_campos):
    lista_sin_excluidos=[]
    for elemento in range(len(xls_tablas)):
        if xls_tablas[elemento].strip() == tabla_oracle:
            lista_sin_excluidos.append(xls_campos[elemento].strip()) 
    return lista_sin_excluidos 

def depurar_lista(lista):
    for elemento in lista_exc:
        if elemento in lista:
            lista.remove(elemento)
    return lista


# Extraemos la info de las columnas owners, tablas y campos (excluidos)
owner_excel,tabla_excel,campo_excel =extraer_info_excel(xls,sheet)
# Cargamos la lista de campos excluidos para una tabla dada. 
tabla = "PERSCONTRATO"
lista_exc = cargar_lista_exc(tabla,tabla_excel,campo_excel)
# Definimos una lista reducida a la que eliminaremos los campos del excel correspondientes.

lista_reducida=['PSC_TIPO_PERS',
                'PSC_COD_PERS',
                'PSC_IDEMPR',
                'PSC_IDCENT',
                'PSC_IDPROD',
                'PSC_IDCONTR',
                'PSC_TIPO_INTER',
                'PSC_ORD_INTERV',
                'PSC_IND_ENVIO',
                'PSC_FEALTCON',
                'PSC_USU_ULTACT',
                'PSC_EMULTACT',
                'PSC_CEULTACT',
                'PSC_FEC_ULTACT',
                'PSC_TIMULTAC',
                'PSC_IND_NIVACC',
                'PSC_SOP_CORRES',
                'PSC_PORC_RESPO',
                'PSC_NEMOC_NOM',
                'PSC_OBLIG_FIRM',
                'PSC_SITUA_RELA',
                'PSC_NRODOMIC',
                'PSC_INDDEVOL',
                'PSC_FEBAJCON',
                'PSC_TFORMINT',
                'PSC_CODIDIO',
                'PSC_CODSPROD',
                'PSC_CODPROD',
                'PSC_IDCONTRN']

########################################################################################################
# Hacemos una copia de lista_reducida en lista_reducida_keys porque han de ser diferentes ya que solo
# cambian las ordenaciones pero no la estructura del fichero.
# En lista_reducida_keys tendremos los campos de la tabla oracle habiendo quitado los campos a excluir.
########################################################################################################
lista_reducida_keys = lista_reducida[:]
lista_reducida_keys = depurar_lista(lista_reducida_keys)
