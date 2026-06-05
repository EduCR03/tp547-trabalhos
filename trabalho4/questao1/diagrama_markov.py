from pathlib import Path

import matplotlib.pyplot as plt


def gerar_diagrama():
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.axis("off")

    estados = {
        "E0": (0, 1.5, "E0\noperacional\npermanece 0.7"),
        "E1": (2.3, 1.5, "E1\npequena degradacao\npermanece 0.5"),
        "E2": (4.6, 1.5, "E2\nfalha moderada\npermanece 0.5"),
        "E3": (6.9, 1.5, "E3\nmodo critico\npermanece 0.6"),
        "E4": (9.2, 1.5, "E4\nqueimado\npermanece 1.0"),
    }

    for _, (x, y, texto) in estados.items():
        ax.text(
            x,
            y,
            texto,
            ha="center",
            va="center",
            fontsize=9,
            bbox=dict(boxstyle="round", facecolor="lightblue", edgecolor="black"),
        )

    def seta(x1, y1, x2, y2, probabilidade, xt, yt):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->"))
        ax.text(xt, yt, probabilidade, ha="center", fontsize=9)

    seta(0.55, 1.78, 1.65, 1.78, "0.3", 1.15, 1.96)
    seta(1.65, 1.08, 0.55, 1.08, "0.2", 1.15, 0.90)
    seta(2.95, 1.78, 3.95, 1.78, "0.3", 3.45, 1.96)
    seta(3.95, 0.82, 2.95, 0.82, "0.1", 3.45, 0.64)
    seta(5.25, 1.5, 6.25, 1.5, "0.4", 5.75, 1.68)
    seta(7.55, 1.5, 8.55, 1.5, "0.4", 8.05, 1.68)

    ax.set_xlim(-1, 10.2)
    ax.set_ylim(0.4, 2.6)
    ax.set_title("Diagrama de transicao de estados")
    plt.tight_layout()
    saida = Path(__file__).with_name("diagrama_markov.png")
    plt.savefig(saida, dpi=150)
    plt.close()
    print(f"Diagrama salvo em: {saida}")


gerar_diagrama()
