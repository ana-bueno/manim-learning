from manim import *
from scipy.integrate import solve_ivp


class primCena(Scene):
    def construct(self):

        # Cena de apresentação!
        textoApresentação = Tex(
            r"Olá, bem vindos ao minicurso \\ de introdução ao Manim!"
        )
        self.play(
            Write(textoApresentação),
            run_time=3,
        )
        self.wait()

        textoPossib = Tex("Vamos ver o que essa ferramenta pode fazer")
        self.play(Transform(textoApresentação, textoPossib))
        self.wait()

        self.play(
            FadeOut(textoApresentação),
        )

        # Primeira cena: criação texto matemático com LateX
        textoFerram_1 = Tex(
            r"1. Podemos escrever elementos matemáticos \\ utilizando o LateX:"
        )
        textoLatex_1 = MathTex(
            r"\int_{-12}^{18} x^3 - \dfrac{6x}{e^{-2x}}+ \tan (12x) \ dx"
        )
        textoFerram_1.to_corner(UL)
        self.play(FadeIn(textoFerram_1), Write(textoLatex_1))
        self.wait()

        self.play(FadeOut(textoLatex_1))

        # Segunda cena: criação e modificação de objs geométricos
        textoFerram_2 = Tex(r"2. Podemos criar e modificar elementos geométricos:")
        textoFerram_2.to_corner(UL)
        circul_1 = Circle(color=ORANGE, fill_opacity=1)
        triang_1 = Triangle(color=BLUE, fill_opacity=1)
        quadra_1 = Square(color=GREEN, fill_opacity=1)
        triang_1.next_to(circul_1, LEFT, buff=0.5)
        quadra_1.next_to(circul_1, RIGHT, buff=0.5)

        self.play(
            Transform(textoFerram_1, textoFerram_2),
            Create(circul_1),
            Create(triang_1),
            Create(quadra_1),
        )

        self.wait()

        circul_2 = Circle(color=YELLOW_E, fill_opacity=1)
        triang_2 = Triangle(color=RED_C, fill_opacity=1)
        quadra_2 = Square(color=BLUE_E, fill_opacity=1)
        circul_2.next_to(triang_2, RIGHT, buff=0.5)
        quadra_2.next_to(triang_2, LEFT, buff=0.5)
        self.play(
            Transform(triang_1, quadra_2),
            Transform(circul_1, triang_2),
            Transform(quadra_1, circul_2),
        )

        graficos_1 = VGroup(triang_1, quadra_1)
        self.play(
            graficos_1.animate.move_to(circul_1),
            ReplacementTransform(graficos_1, circul_1),
        )

        # criação do plano cartesiano

        textoFerram_3 = Tex(r"3. Podemos criar planos e \\ representar funções")
        textoFerram_3.to_corner(UL)

        # --------------Primeiro plano

        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            axis_config={"include_tip": True, "color": WHITE},
        )
        rotulos_ax = ax.get_axis_labels(x_label="x", y_label="f(x)")

        ponto_1 = Dot(ax.coords_to_point(2, 2), color=PURPLE)
        linhas_pt1 = ax.get_lines_to_point(ax.coords_to_point(2, 2))
        self.play(
            ReplacementTransform(textoFerram_1, textoFerram_3),
            # Transform(graficos_1, ponto_1),
            ReplacementTransform(circul_1, ponto_1),
            # FadeOut(graficos_1),
        )

        self.play(
            Create(ax),
            Create(rotulos_ax),
            Create(linhas_pt1),
            run_time=3,
        )

        ax_2 = Axes(
            x_range=[0, 5],
            y_range=[0, 5],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True, "color": WHITE},
        )
        rotulos_ax_2 = ax_2.get_axis_labels(x_label="x", y_label="f(x)")

        ponto_2 = Dot(ax_2.coords_to_point(2, 2), color=PURPLE)
        lines_pt2 = ax_2.get_lines_to_point(ax_2.coords_to_point(2, 2))

        self.play(
            FadeOut(circul_1),
            ReplacementTransform(ax, ax_2),
            ReplacementTransform(ponto_1, ponto_2),
            ReplacementTransform(linhas_pt1, lines_pt2),
            ReplacementTransform(rotulos_ax, rotulos_ax_2),
        )

        graficos_2 = VGroup(ax_2, ponto_2, lines_pt2, rotulos_ax_2)
        graficos_2.generate_target()
        graficos_2.target.shift(LEFT * 2 + DOWN).scale(1.2)

        self.play(MoveToTarget(graficos_2))

        self.wait()

        curva1_graf = ax_2.plot(lambda x: (x**2), color=MAROON, x_range=[0, 2.2])
        curva1_label = ax_2.get_graph_label(curva1_graf, "x^2")
        curva1_label.move_to((LEFT * 1.5) + (UP * 1.5))
        ponto_3 = Dot(ax_2.coords_to_point(2, 4), color=PURPLE, fill_opacity=1)
        lines_pt3 = ax_2.get_lines_to_point(ax_2.coords_to_point(2, 4))

        self.play(
            Create(curva1_graf),
            Create(curva1_label),
            ReplacementTransform(ponto_2, ponto_3),
            ReplacementTransform(lines_pt2, lines_pt3),
            FadeOut(textoFerram_3),
        )

        textoFerram_4 = Tex(
            r"4. Podemos criar e representar \\  funções em $\mathbb{R}^3$"
        )
        textoFerram_4.to_corner(UL)

        self.play(FadeIn(textoFerram_4))

        self.wait(3)
