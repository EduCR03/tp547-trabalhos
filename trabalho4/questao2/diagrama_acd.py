from pathlib import Path

import matplotlib.pyplot as plt


def gerar_diagrama():
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis("off")

    caixas = [
        ("Chegada", 0, 2),
        ("Fila recepcao", 2, 2),
        ("Cadastro", 4, 2),
        ("Fila triagem", 6, 2),
        ("Triagem", 8, 2),
        ("Fila medica", 2, 0.8),
        ("Consulta\n2 medicos", 5, 0.8),
        ("Saida", 8, 0.8),
    ]

    for texto, x, y in caixas:
        ax.text(
            x,
            y,
            texto,
            ha="center",
            va="center",
            fontsize=10,
            bbox=dict(boxstyle="round", facecolor="lightblue", edgecolor="black"),
        )

    def seta(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->"))

    seta(0.6, 2, 1.4, 2)
    seta(2.6, 2, 3.4, 2)
    seta(4.6, 2, 5.4, 2)
    seta(6.6, 2, 7.4, 2)
    seta(8, 1.7, 2, 1.1)
    seta(2.7, 0.8, 4.3, 0.8)
    seta(5.7, 0.8, 7.4, 0.8)

    ax.text(5, 0.15, "Se recurso estiver ocupado, paciente permanece na fila.", ha="center", fontsize=9)
    ax.set_xlim(-1, 9)
    ax.set_ylim(0, 2.8)
    ax.set_title("Diagrama ACD do consultorio")
    plt.tight_layout()
    saida = Path(__file__).with_name("diagrama_acd.png")
    plt.savefig(saida, dpi=150)
    plt.close()
    print(f"Diagrama salvo em: {saida}")


gerar_diagrama()
