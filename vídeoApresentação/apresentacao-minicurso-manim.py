from manim import *
from scipy import integrate
from scipy.integrate import solve_ivp, tplquad


class primCena(Scene):
    def construct(self):

#---------------------------------------------- Cena de apresentação
        self.wait(1)
        textoAprest = Tex(
            r"Olá, bem vindos ao minicurso \\ de introdução ao Manim!"
        )

        self.play(
            Write(textoAprest),
            run_time=2,
        )
        self.wait()

        textoPossib = Tex("Vamos ver o que essa ferramenta pode fazer")
        
        self.play(ReplacementTransform(textoAprest, textoPossib))
        self.wait()

        self.play(
            Unwrite(textoPossib)    
        )

#------------------------------------- cena ferramenta latex
        textoFerram_1 = Tex(
            r"1. Podemos escrever utilizando o LaTeX "
        )
        textoLatex_1 = MathTex(
            "\\int_{0}^{2\\pi}\\int_{0}^{\\pi}\\int_{0}^{1}=",
            "(\\rho cos(\\phi))^2",
            "\\rho ^2",
            "sen(\\phi)",
            "d\\rho d\\phi d\\theta",
        )
        textoFerram_1.to_corner(UL)

    # criação da caixa de destaque
        framebox1 = SurroundingRectangle(
            textoLatex_1[0], buff=0.1, stroke_opacity=0.5)
        framebox2 = SurroundingRectangle(
            textoLatex_1[1], buff=0.1, stroke_opacity=0.5)
        framebox3 = SurroundingRectangle(
            textoLatex_1[2], buff=0.1, stroke_opacity=0.5)
        framebox4 = SurroundingRectangle(
            textoLatex_1[3], buff=0.1, stroke_opacity=0.5)

        self.play(FadeIn(textoFerram_1), Write(textoLatex_1))
        self.play(Create(framebox1))
        self.wait()

    # animação das caixas de destaque
        self.play(
            ReplacementTransform(framebox1, framebox2),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox2, framebox3),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox3, framebox4),
        )
        self.wait()

        self.play(FadeOut(textoLatex_1), FadeOut(framebox4))

#-------------------------cena: modificação de objs geométricos
        textoFerram_2 = Tex(
            r"2. Podemos criar e modificar elementos geométricos:")
        textoFerram_2.to_corner(UL)

    # primeiro conj obje
        circul_1 = Circle(color=ORANGE, fill_opacity=1)
        triang_1 = Triangle(color=BLUE, fill_opacity=1)
        quadra_1 = Square(color=GREEN, fill_opacity=1)
    #posição dos prim obj
        triang_1.next_to(circul_1, LEFT, buff=0.5)
        quadra_1.next_to(circul_1, RIGHT, buff=0.5)

        self.play(
            ReplacementTransform(textoFerram_1, textoFerram_2),
            Create(circul_1),
            Create(triang_1),
            Create(quadra_1),
        )

        self.wait()
    
    # segundo conj de obj
        circul_2 = Circle(color=YELLOW_E, fill_opacity=1)
        triang_2 = Triangle(color=RED_C, fill_opacity=1)
        quadra_2 = Square(color=BLUE_E, fill_opacity=1)

        circul_2.next_to(triang_2, RIGHT, buff=0.5)
        quadra_2.next_to(triang_2, LEFT, buff=0.5)

        self.play(
            ReplacementTransform(triang_1, quadra_2),
            ReplacementTransform(circul_1, triang_2),
            ReplacementTransform(quadra_1, circul_2),
        )

        # ultima animação dos obj geométricos
        graficos_1 = VGroup(quadra_2, circul_2)
        self.play(
            graficos_1.animate.move_to(triang_2),
            ReplacementTransform(graficos_1, triang_2),
        )

#---------------------------------------- criação do plano cartesiano
        textoFerram_3 = Tex(
            r"3. Podemos criar planos e \\ representar funções")
        textoFerram_3.to_corner(UL)

    # primeiro plano
        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            axis_config={"include_tip": True, "color": WHITE},
        )
        rotulos_ax = ax.get_axis_labels(x_label="x", y_label="f(x)")

        # criação ponto e linhas
        ponto_1 = Dot(ax.coords_to_point(2, 2), color=PURPLE, fill_opacity=1)
        linhas_pt1 = ax.get_lines_to_point(ax.coords_to_point(2, 2))

        self.play(
            ReplacementTransform(textoFerram_2, textoFerram_3),
            ReplacementTransform(triang_2, ponto_1),
        )

        self.play(
            Create(ax),
            Create(rotulos_ax),
            Create(linhas_pt1),
            run_time=2,
        )

    # segundo plano - atualização
        ax_2 = Axes(
            x_range=[0, 5],
            y_range=[0, 5],
            x_length=4,
            y_length=4,
            axis_config={"color": WHITE},
        )
        rotulos_ax_2 = ax_2.get_axis_labels(x_label="x", y_label="f(x)")

        ponto_2 = Dot(ax_2.coords_to_point(2, 2), color=PURPLE, fill_opacity=1)
        lines_pt2 = ax_2.get_lines_to_point(ax_2.coords_to_point(2, 2))

        # movimentação do bloco de obj - coordenado
        graficos_2 = VGroup(ax_2, ponto_2, lines_pt2, rotulos_ax_2)
        graficos_2.move_to(LEFT * 2 + 0.5 * DOWN).scale(1.1)

        self.remove(triang_2)

        self.play(
            ReplacementTransform(ponto_1, ponto_2),
            ReplacementTransform(ax, ax_2),
            ReplacementTransform(linhas_pt1, lines_pt2),
            ReplacementTransform(rotulos_ax, rotulos_ax_2),
        )

        # criação e plot do gráfico x^2
        curva1_graf = ax_2.plot(lambda x: (
            x**2), color=MAROON, x_range=[0, 2.2])
        curva1_label = ax_2.get_graph_label(curva1_graf, "x^2")
        curva1_label.move_to((LEFT * 1.5) + (UP * 1.5))

        ponto_3 = Dot(ax_2.coords_to_point(2, 4), color=PURPLE, fill_opacity=1)
        lines_pt3 = ax_2.get_lines_to_point(ax_2.coords_to_point(2, 4))

        self.play(
            Create(curva1_graf),
            Create(curva1_label),
            ReplacementTransform(ponto_2, ponto_3),
            ReplacementTransform(lines_pt2, lines_pt3),
            Unwrite(textoFerram_3),
        )

#---------------------------------cena: setup gráfico e plot em R^3
        textoFerram_4 = Tex(
            r"4. Podemos criar \\ gráficos em 3D"
        )
        textoFerram_4.to_corner(UL)

        ponto_4 = Dot(color=WHITE)
        graficos_3 = VGroup(
            ax_2, curva1_graf, curva1_label, ponto_3, lines_pt3, rotulos_ax_2
        )

        self.play(ReplacementTransform(graficos_3, ponto_4))
        self.wait(0.5)
        self.play(FadeIn(textoFerram_4))

        self.wait()


#-----------------------------------cena em r3 - classe ThreeDScene
class segCena(ThreeDScene):
    def construct(self):

        textoFerram_4 = Tex(
            r"4. Podemos criar \\ gráficos em 3D"
        )
        textoFerram_4.to_corner(UL)
        self.add_fixed_in_frame_mobjects(textoFerram_4)
        
        ax_3 = ThreeDAxes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            z_range=[0, 4],
            z_length=4,
        )
        labels_ax_3 = ax_3.get_axis_labels(Tex("x"), Tex("y"), Tex(""))
                
        ponto_4 =Dot3D(point=ax_3.coords_to_point(0,0,0), color=WHITE)
        self.add(ponto_4)

        self.set_camera_orientation(zoom=0.5)

        self.play(
            GrowFromCenter(ax_3), 
            Create(labels_ax_3)
        )

        self.move_camera(phi=75 * DEGREES, theta=30 *
                         DEGREES, zoom=0.8, run_time=1.5)

    # criação gráfico em r3
        # criação e animação cilindro
        altura_1 = 0
        raio = 3
        altura_anim = ValueTracker(altura_1)

        def cilind(u, v):
            angulo = TAU * u

            x = raio * np.cos(angulo)
            y = raio * np.sin(angulo)
            z = altura_anim.get_value() * v

            return np.array([x, y, z])

        cilindro_1 = Surface(
            cilind,
            u_range=(0, 1),
            v_range=(0, 1),
            resolution=(32, 1),
            checkerboard_colors=[GREEN_D, GREEN_D],
            fill_opacity=0.5
        )

        cilindro_1.add_updater(
            lambda m: m.become(
                Surface(
                    cilind,
                    u_range=(0, 1),
                    v_range=(0, 1),
                    resolution=(32, 1),
                    checkerboard_colors=[GREEN_D, GREEN_D],
                    fill_opacity=0.5
                )
            )
        )

        self.play(Create(cilindro_1))

        self.play(altura_anim.animate.set_value(2), run_time=1.5)

        cilindro_1.remove_updater(lambda m: m.become(cilindro_1))

        self.wait()

        self.play(
            Unwrite(cilindro_1),
            run_time=2,
            )

    # criação e plot em r3 - linhas 
        ax_5 = ThreeDAxes()
        ponto_5 = Dot3D()

        self.play(
            ReplacementTransform(ax_3, ax_5),
            #GrowFromCenter(ax_5)
        )

        theta = Line(ORIGIN, ax_5.c2p(0,0,2), color=PINK)
        theta_2 = Line(ORIGIN, ax_5.c2p(2,2,2), color=PINK)
        vertical_line    = DashedLine(ax_5.c2p(2,0),ax_5.c2p(2,2))
        horizontal_line  = DashedLine(ax_5.c2p(0,2),ax_5.c2p(2,2))
        fall_line        = DashedLine(ax_5.c2p(2,2),ax_5.c2p(2,2,2))

        ponto_6 = Dot3D(point=ax_5.c2p(2,2,2), color=PINK)
        self.play(
            ReplacementTransform(ponto_5, theta),
        )

        self.play(
            ReplacementTransform(theta, theta_2),
            GrowFromCenter(ponto_6),
            Write(vertical_line),
            Write(horizontal_line),
            Write(fall_line)
        )

    # criação e plot em r3 funções em r3
        self.move_camera(phi=70 * DEGREES, theta=9 *
                         DEGREES, run_time=1.5) 

        self.play(FadeOut(textoFerram_4))
# --------------------------------------------------------------- ultima cena função e câmera
        textoFerram_5 = Tex(r"E muito mais !")
        textoFerram_5.to_corner(UL)
        self.add_fixed_in_frame_mobjects(textoFerram_5)

        funcao = ParametricFunction(
            lambda t: (
                np.sin(t),
                np.cos(t),
                0.1 * t
            ),
            t_range = (-4*PI, 4*PI, 0.01),
            color=YELLOW_C,
        ).set_shade_in_3d(True)

        graficos_4 = VGroup(theta_2, ponto_6, vertical_line, horizontal_line, fall_line, ponto_5)
        
        self.play(
            FadeOut(graficos_4)
        )

        self.play(
        Write(funcao),
        run_time=3,
        )

        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(2)

        graficos_5 = VGroup(textoFerram_5, funcao, ax_5, ponto_4, labels_ax_3) 
        self.play(
            FadeOut(graficos_5, target_position = ponto_4)
        )

        self.wait()

class ultimCena(Scene):
    def construct(self):
        #self.add_sound("choose-motivation-281450.mp3")
        textoFinal = Tex(
            r"Minicurso de produção de vídeos com Manim ofertado na \\ ?? Semana da Matemática \\ UEM 2025"
        )

        self.play(
            Write(textoFinal),
            run_time=3,
        )

        self.wait(3)


