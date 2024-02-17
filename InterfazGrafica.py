import tkinter as tk
from os import remove
import matplotlib.pyplot as plt
import pandas as pd
from pandastable import Table


def cargardatos():
    url = "https://raw.githubusercontent.com/Richv83/POO-TF/main/Residuos.csv"
    rg = pd.read_csv(url, sep=";", encoding="latin-1")
    return rg


def lectura_reporte():
    data = pd.read_excel("Reporte.xlsx")
    return data


def reporteuno(rg):
    reporte_1 = rg.pivot_table(index="PERIODO", values="QRESIDUOS_MUN", aggfunc="sum")
    reporte_1.columns = ["Residuos Generados"]
    reporte_1.index.name = "Año"

    reporte_excel = reporte_1.to_excel("Reporte.xlsx")

    tabla = Table(
        ventana_tabla,
        dataframe=lectura_reporte(),
        showtoolbar=False,
        showstatusbar=False,
        editable=False,
    )
    tabla.show()

    reporte_1_g = reporte_1.plot(kind="barh", color="grey")
    reporte_1_g.set_title(
        "Cantidad de residuos totales generados anualmente",
        fontweight="bold",
        loc="center",
    )
    reporte_1_g.set_xlabel("Residuos Generados")
    reporte_1_g.set_ylabel("Año")
    reporte_1_g.set_xlim(0, 9000000)
    reporte_1_g.set_xticks(
        [
            0,
            1000000,
            2000000,
            3000000,
            4000000,
            5000000,
            6000000,
            7000000,
            8000000,
            9000000,
        ]
    )
    reporte_1_g.set_xticklabels(
        ["0", "1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M", "9M"]
    )
    reporte_1_g.bar_label(reporte_1_g.containers[0], fmt="%.2f", padding=3)
    reporte_1_g.legend(loc="upper right")
    plt.show()


def reportedos(rg):
    reporte_2 = rg.pivot_table(index="REG_NAT", values="QRESIDUOS_MUN", aggfunc="sum")
    reporte_2.columns = ["Residuos Generados"]
    reporte_2.index.name = "Región Natural"

    reporte_excel = reporte_2.to_excel("Reporte.xlsx")

    tabla = Table(
        ventana_tabla,
        dataframe=lectura_reporte(),
        showtoolbar=False,
        showstatusbar=False,
        editable=False,
    )
    tabla.show()

    reporte_2_g = reporte_2.plot(
        kind="pie",
        y="Residuos Generados",
        autopct="%.2f%%",
        startangle=90,
        explode=(0.1, 0.1, 0.1),
        shadow=True,
    )
    reporte_2_g.set_ylabel("")
    reporte_2_g.axis("equal")
    reporte_2_g.legend(loc="lower right")
    reporte_2_g.set_title(
        "Porcentaje de residuos generados por región natural",
        fontweight="bold",
        loc="center",
    )
    plt.show()


def reportetres(rg):
    reporte_3 = rg.pivot_table(
        index="DEPARTAMENTO", values="QRESIDUOS_MUN", aggfunc="sum"
    )
    reporte_3.columns = ["Residuos Generados"]
    reporte_3.index.name = "Departamento"

    reporte_excel = reporte_3.to_excel("Reporte.xlsx")

    tabla = Table(
        ventana_tabla,
        dataframe=lectura_reporte(),
        showtoolbar=False,
        showstatusbar=False,
        editable=False,
    )
    tabla.show()

    reporte_3_g = reporte_3.plot(kind="bar", color="grey", figsize=(10, 5))
    reporte_3_g.set_title(
        "Cantidad de residuos totales generados por departamento",
        fontweight="bold",
        loc="center",
    )
    reporte_3_g.set_xlabel("Departamento")
    reporte_3_g.set_ylabel("Residuos Generados")
    reporte_3_g.set_ylim(0, 20000000)
    reporte_3_g.set_yticks(
        [
            0,
            2000000,
            4000000,
            6000000,
            8000000,
            10000000,
            12000000,
            14000000,
            16000000,
            18000000,
            20000000,
        ]
    )
    reporte_3_g.set_yticklabels(
        ["0", "2M", "4M", "6M", "8M", "10M", "12M", "14M", "16M", "18M", "20M"]
    )
    reporte_3_g.set_xticklabels(
        reporte_3.index, rotation=45, ha="right", rotation_mode="anchor"
    )
    reporte_3_g.legend(loc="upper right")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
    plt.show()


def reportecuatro(rg):
    reporte_4 = rg.pivot_table(
        index=["PERIODO", "DEPARTAMENTO"], values="QRESIDUOS_MUN", aggfunc="sum"
    )
    reporte_4.columns = ["Residuos Generados"]
    reporte_4.index.names = ["Año", "Departamento"]

    reporte_4_sorted = reporte_4.sort_values(
        by=["Año", "Residuos Generados"], ascending=False
    )

    reporte_4_sorted_top5 = reporte_4_sorted.groupby("Año").head()

    reporte_excel = reporte_4_sorted_top5.to_excel("Reporte.xlsx")

    tabla = Table(
        ventana_tabla,
        dataframe=lectura_reporte(),
        showtoolbar=False,
        showstatusbar=False,
        editable=False,
    )
    tabla.show()

    reporte_4_sorted_top5_g = reporte_4_sorted_top5.plot(kind="barh", figsize=(15, 5))
    reporte_4_sorted_top5_g.set_title(
        "Top 5 mayores cantidades de residuos generados por departamento en cada año",
        fontweight="bold",
        loc="center",
    )
    reporte_4_sorted_top5_g.set_xlabel("Residuos Generados")
    reporte_4_sorted_top5_g.set_ylabel("Año - Departamento")
    reporte_4_sorted_top5_g.set_xlim(0, 4000000)
    reporte_4_sorted_top5_g.set_xticks(
        [0, 500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000]
    )
    reporte_4_sorted_top5_g.set_xticklabels(
        ["0", "0.5M", "1M", "1.5M", "2M", "2.5M", "3M", "3.5M", "4M"]
    )
    reporte_4_sorted_top5_g.bar_label(
        reporte_4_sorted_top5_g.containers[0],
        fmt="%.2f",
        padding=3,
        label_type="edge",
        fontsize=6,
    )
    reporte_4_sorted_top5_g.legend(loc="upper right")
    plt.show()


def reportecinco(rg):
    reporte_5 = rg.pivot_table(
        index=["PERIODO", "DEPARTAMENTO"], values="QRESIDUOS_MUN", aggfunc="sum"
    )
    reporte_5.columns = ["Residuos Generados"]
    reporte_5.index.names = ["Año", "Departamento"]

    reporte_5_sorted = reporte_5.sort_values(
        by=["Año", "Residuos Generados"], ascending=True
    )

    reporte_5_sorted_top5 = reporte_5_sorted.groupby("Año").head()

    reporte_excel = reporte_5_sorted_top5.to_excel("Reporte.xlsx")

    tabla = Table(
        ventana_tabla,
        dataframe=lectura_reporte(),
        showtoolbar=False,
        showstatusbar=False,
        editable=False,
    )
    tabla.show()

    reporte_5_sorted_top5_g = reporte_5_sorted_top5.plot(kind="barh", figsize=(15, 5))
    reporte_5_sorted_top5_g.set_title(
        "Top 5 menores cantidades de residuos generados por departamento en cada año",
        fontweight="bold",
        loc="center",
    )
    reporte_5_sorted_top5_g.set_xlabel("Residuos Generados")
    reporte_5_sorted_top5_g.set_ylabel("Año - Departamento")
    reporte_5_sorted_top5_g.bar_label(
        reporte_5_sorted_top5_g.containers[0],
        fmt="%.2f",
        padding=3,
        label_type="edge",
        fontsize=6,
    )
    reporte_5_sorted_top5_g.legend(loc="upper right")
    plt.show()


def cerrar():
    try:
        remove("Reporte.xlsx")
        ventana.destroy()
    except FileNotFoundError:
        ventana.destroy()


# Interfaz gráfica
ventana = tk.Tk()
ventana.title("SA-RMGA")

ventana_tabla = tk.Frame(ventana, width=700, height=500, bg="white")
ventana_tabla.grid(row=0, column=1, padx=10, pady=10, rowspan=7, columnspan=7)

boton_titulo = tk.Label(
    ventana,
    text="Reportes",
    font=("Arial", 20),
    width=7,
    height=1,
    bg="white",
    fg="black",
)
boton_titulo.grid(row=0, column=0, pady=10)

boton_1 = tk.Button(
    ventana,
    command=lambda: reporteuno(cargardatos()),
    text="Reporte 1",
    font=("Arial", 19),
    width=7,
    height=1,
    bg="blue",
    fg="white",
)

boton_2 = tk.Button(
    ventana,
    command=lambda: reportedos(cargardatos()),
    text="Reporte 2",
    font=("Arial", 19),
    width=7,
    height=1,
    bg="blue",
    fg="white",
)

boton_3 = tk.Button(
    ventana,
    command=lambda: reportetres(cargardatos()),
    text="Reporte 3",
    font=("Arial", 19),
    width=7,
    height=1,
    bg="blue",
    fg="white",
)

boton_4 = tk.Button(
    ventana,
    command=lambda: reportecuatro(cargardatos()),
    text="Reporte 4",
    font=("Arial", 19),
    width=7,
    height=1,
    bg="blue",
    fg="white",
)

boton_5 = tk.Button(
    ventana,
    command=lambda: reportecinco(cargardatos()),
    text="Reporte 5",
    font=("Arial", 19),
    width=7,
    height=1,
    bg="blue",
    fg="white",
)

boton_1.grid(row=1, column=0, pady=10)
boton_2.grid(row=2, column=0, pady=10)
boton_3.grid(row=3, column=0, pady=10)
boton_4.grid(row=4, column=0, pady=10)
boton_5.grid(row=5, column=0, pady=10)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

ventana.mainloop()
