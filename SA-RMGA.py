import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


def cargardatos():
    url = "https://raw.githubusercontent.com/Richv83/POO-TF/main/Residuos.csv"
    rg = pd.read_csv(url, sep=";", encoding="latin-1")
    return rg


def reporteuno(rg):
    reporte_1 = rg.pivot_table(index="PERIODO", values="QRESIDUOS_MUN", aggfunc="sum")
    reporte_1.columns = ["Residuos Generados"]
    reporte_1.index.name = "Año"

    print("\n--- Reporte 1 : Cantidad de residuos totales generados anualmente ---\n")
    print(
        tabulate(
            reporte_1,
            headers="keys",
            tablefmt="fancy_grid",
            showindex="always",
            numalign="right",
            floatfmt=".2f",
        )
    )

    reporte_1_g = reporte_1.plot(kind="barh", color="grey")
    reporte_1_g.set_title("Cantidad de residuos totales generados anualmente")
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

    print("\n--- Reporte 2 : Cantidad de residuos generados por región natural ---\n")
    print(
        tabulate(
            reporte_2,
            headers="keys",
            tablefmt="fancy_grid",
            showindex="always",
            numalign="right",
            floatfmt=".2f",
        )
    )

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
    reporte_2_g.set_title("Porcentaje de residuos generados por región natural")
    plt.show()


def reportetres(rg):
    reporte_3 = rg.pivot_table(
        index="DEPARTAMENTO", values="QRESIDUOS_MUN", aggfunc="sum"
    )
    reporte_3.columns = ["Residuos Generados"]
    reporte_3.index.name = "Departamento"

    print("\n--- Reporte 3 : Cantidad de residuos generados por departamento ---\n")
    print(
        tabulate(
            reporte_3,
            headers="keys",
            tablefmt="fancy_grid",
            showindex="always",
            numalign="right",
            floatfmt=".2f",
        )
    )

    reporte_3_g = reporte_3.plot(kind="bar", color="grey", figsize=(10, 5))
    reporte_3_g.set_title("Cantidad de residuos totales generados por departamento")
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

    # obtener los 5 departamentos con mayor cantidad de residuos generados en cada año
    reporte_4_sorted_top5 = reporte_4_sorted.groupby("Año").head()

    print(
        "\n--- Reporte 4 : Top 5 mayores cantidades de residuos generados por departamento en cada año ---\n"
    )
    print(
        tabulate(
            reporte_4_sorted_top5.reset_index(),
            headers="keys",
            tablefmt="fancy_grid",
            showindex="False",
            numalign="right",
            floatfmt=".2f",
        )
    )


def reportecinco(rg):
    reporte_5 = rg.pivot_table(
        index=["PERIODO", "DEPARTAMENTO"], values="QRESIDUOS_MUN", aggfunc="sum"
    )
    reporte_5.columns = ["Residuos Generados"]
    reporte_5.index.names = ["Año", "Departamento"]

    reporte_5_sorted = reporte_5.sort_values(
        by=["Año", "Residuos Generados"], ascending=True
    )

    # obtener los 5 departamentos con menor cantidad de residuos generados en cada año
    reporte_5_sorted_top5 = reporte_5_sorted.groupby("Año").head()

    print(
        "\n--- Reporte 5 : Top 5 menores cantidades de residuos generados por departamento en cada año ---\n"
    )
    print(
        tabulate(
            reporte_5_sorted_top5.reset_index(),
            headers="keys",
            tablefmt="fancy_grid",
            showindex="False",
            numalign="right",
            floatfmt=".2f",
        )
    )


def menu():
    print("\n        SA-RMGA          ")
    print("-------------------------------")
    print("[1] Mostrar Reporte 1")
    print("[2] Mostrar Reporte 2")
    print("[3] Mostrar Reporte 3")
    print("[4] Mostrar Reporte 4")
    print("[5] Mostrar Reporte 5")
    print("[6] Salir")
    print("-------------------------------")
    op = ingresaOpcion("Ingresa tu opción: ", 1, 6)
    return op


def ingresaOpcion(etiqueta, inferior, superior):
    while True:
        try:
            numint = int(input(etiqueta))
            if inferior <= numint <= superior:
                return numint
            else:
                print("Opción no existe, inténtelo nuevamente")
        except ValueError:
            print("El valor ingresado debe ser un número")


def main():
    rg = cargardatos()
    while True:
        op = menu()
        if op == 1:
            reporteuno(rg)
        elif op == 2:
            reportedos(rg)
        elif op == 3:
            reportetres(rg)
        elif op == 4:
            reportecuatro(rg)
        elif op == 5:
            reportecinco(rg)
        elif op == 6:
            print("Saliendo del programa...")
            break


# Inicio del programa
main()
