import typing_extensions
from manim import *
#manim -pql primeiro-teste.py primCena


class primCena(Scene):
    def construct(self):

        self.wait(1)

        #-----------------------------------------CHAVE DA DIVISAO
        linha = Line([0,0,0], [2,0,0])
        linhav = Line([0,0,0], [0,1,0])
        chave_div = VGroup(linha, linhav)

        #----------------------------------------TEXTOS-DIVIDENDO-DIVISOR-RESTO-QUOCIENTE
        dividendo = Tex(
            r"dividendo"
            )
        dividendo.move_to(LEFT*2)

        divisor = Tex(
            r"divisor"
        )
        divisor.next_to(dividendo, RIGHT, buff=0.5)

        resto = Tex(
            r"resto"
        )
        resto.next_to(dividendo, DOWN, buff=0.5)

        quosciente = Tex(
            r"quociente"
        )
        quosciente.next_to(divisor, DOWN, buff=0.5)

        #---------------------------------- GRUPO TEXTOS
        textos_1div = VGroup(dividendo, divisor, resto, quosciente)
        textos_1div.move_to(UP*0.1)

        #----------------------------------------ESCREVER A CHAVE E OS TEXTOS
        self.play(
            Write(chave_div),
            run_time=3,
        )

        self.wait(1)

        self.play(
            Write(textos_1div),
           run_time=2 
        )
        
        self.wait()

        #--------------------------------------- FRAMEBOX
        framebox_00= SurroundingRectangle(textos_1div[0], buff=0.3)
        framebox_01 =SurroundingRectangle(textos_1div[1], buff=0.3)
        framebox_02 =SurroundingRectangle(textos_1div[2], buff=0.3)
        framebox_03 =SurroundingRectangle(textos_1div[3], buff=0.3)

        self.play(Create(framebox_00))

        self.wait()

        #--------------------------MOVIMENTACAO DAS FRAMEBOX PELO TEXTO
        self.play(
            ReplacementTransform(framebox_00, framebox_01),
        )
        self.wait()

        self.play(
            ReplacementTransform(framebox_01, framebox_02),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox_02, framebox_03),
        )
        
        self.wait(2)

        #ReplacementTransform

        dividendo_1 = Tex(r"156")
        dividendo_1.move_to(UP*0.5 + LEFT*1).scale(1.5)
        divisor_1 = Tex(r"77")
        divisor_1.next_to(dividendo_1, RIGHT, buff=1).scale(1.5)
        valor_1 = Tex(r"-154")
        valor_1.next_to(dividendo_1, DOWN, buff=0.5).scale(1.5)
        quos_1 = Tex(r"2")
        quos_1.next_to(divisor_1, DOWN, buff=0.5).scale(1.5)
        rest_1 = Tex(r"2")
        rest_1.next_to(valor_1, DOWN, buff=0.5).scale(1.5)

        primeiros_valores = VGroup(dividendo_1, divisor_1, valor_1, quos_1, rest_1)

        self.play(
            Unwrite(textos_1div),
            FadeOut(framebox_03),
            FadeOut(chave_div),
            run_time=2
        )

        self.wait(3)

        divisão_txt = Tex(
            r"Divisão?"
        )

        self.play(Write(divisão_txt), run_time=2)

        self.play(divisão_txt.animate.shift(UP*2), run_time=2)

        divisao_definicao = Tex(
            r"Divisão: Ação de repartir, distribuir, partilhar; \\ repartição, distribuição, partilha"
        )

        caixa_3 = Square(color=GREEN, fill_opacity=1)
        caixa_1 = Square(color=GREEN, fill_opacity=1)
        caixa_2 = Square(color=GREEN, fill_opacity=1)
        caixa_4 = Square(color=GREEN, fill_opacity=1)
        caixa_5 = Square(color=GREEN, fill_opacity=1)
        
        """caixa_3.scale(0.8)
        caixa_1.next_to(caixa_3, LEFT, buff=0.5).scale(0.8)
        caixa_2.next_to(caixa_1, LEFT, buff=0.5).scale(0.8)
        caixa_4.next_to(caixa_3, RIGHT, buff=0.5).scale(0.8)
        caixa_5.next_to(caixa_4, RIGHT, buff=0.5).scale(0.8)"""


        caixas_tot = VGroup(caixa_1, caixa_2, caixa_3, caixa_4, caixa_5).set_x(0).arrange(buff=0.5).scale(0.8)

        self.play(
            Write(caixas_tot),
            run_time=3
        )

        pessoa_01 = Tex(
            r"João"
        )
        pessoa_01.move_to(UP*3 + LEFT*3.5)
        pessoa_02 = Tex(
            r"Maria"
        )
        pessoa_02.move_to(UP*3 + RIGHT*3.5)

        self.wait(1)
        self.play(Write(pessoa_01), Write(pessoa_02))

        self.wait(2)

        self.play(
            caixa_2.animate.shift(UP + LEFT*0.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            caixa_1.animate.shift(UP + LEFT*0.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            caixa_3.animate.shift(DOWN + LEFT*3.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            caixa_4.animate.shift(UP + RIGHT*0.5).scale(0.8).set_fill(BLUE).set_stroke(BLUE),
            caixa_5.animate.shift(UP + RIGHT*0.5).scale(0.8).set_fill(BLUE).set_stroke(BLUE),
            run_time=3
        )

        self.wait(4)

        self.play(
            caixa_2.animate.shift(LEFT),
            caixa_1.animate.shift(DOWN*2 + RIGHT*7).set_fill(BLUE).set_stroke(BLUE),
            caixa_3.animate.shift(RIGHT*8).set_fill(BLUE).set_stroke(BLUE),
            run_time=3
        )

        self.wait(4)

        self.play(
            Unwrite(pessoa_01),
            Unwrite(pessoa_02),
            caixas_tot.animate.set_x(0).arrange(buff=0.5).set_fill(GREEN).set_stroke(GREEN),
            run_time=3
        )

        self.wait(2)

        self.play(
            FadeOut(caixas_tot),
            FadeOut(divisão_txt)
        )

        self.wait()

        self.play(
            AddTextWordByWord(divisao_definicao),
            run_time=10
        )

        self.wait(4)

        self.play(Unwrite(divisao_definicao), run_time=4)

        self.play(FadeIn(caixas_tot), run_time=4)

        self.wait()
        
        pessoa_03 = Tex(
            r"João"
        )
        pessoa_03.move_to(UP*3 + LEFT*3.5)
        pessoa_04 = Tex(
            r"Maria"
        )
        pessoa_04.move_to(UP*3 + RIGHT*3.5)
        resto_00 = Tex(
            r"Resto"
        )
        resto_00.move_to(DOWN*3)

        self.play(Write(pessoa_03), Write(pessoa_04))


        self.play(
            caixa_2.animate.shift(UP + LEFT*0.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            caixa_1.animate.shift(UP + LEFT*0.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            #caixa_3.animate.shift(DOWN + LEFT*3.5).scale(0.8).set_fill(PURPLE).set_stroke(PURPLE),
            caixa_4.animate.shift(UP + RIGHT*0.5).scale(0.8).set_fill(BLUE).set_stroke(BLUE),
            caixa_5.animate.shift(UP + RIGHT*0.5).scale(0.8).set_fill(BLUE).set_stroke(BLUE),
            run_time=3
        )
        self.play(Write(resto_00))
        self.play(
            caixa_3.animate.shift(DOWN*2).scale(0.8)
        )

        self.wait(1)

        self.play(FadeOut(pessoa_03), FadeOut(pessoa_04), FadeOut(resto_00), FadeOut(caixas_tot))


        bolas_gr = VGroup(*[Circle(radius=0.2, color=YELLOW, fill_opacity=1) for s in range(0,61)])

        bolas_gr.arrange_in_grid(rows=5, buff=0.3)

        self.play(
                Create(bolas_gr)
                )

        caixas_03 = VGroup(*[Square(side_length=3.4) for s in range(0,3)])
        caixas_03.arrange_in_grid(rows=1, buff=0.5).move_to(UP*1.5)

        #caixas_texto_1 = MarkupText("1").next_to(caixas_03[0], UP*.5)
        #caixas_texto_2 = MarkupText("2").next_to(caixas_03[1], UP*.5)
        #caixas_texto_resto = MarkupText("Resto").next_to(caixas_03[2], UP*.5)

        self.play(
            bolas_gr.animate.shift(DOWN*2).scale(0.7),
        )

        self.play(
            FadeIn(caixas_03), 
            #Write(caixas_texto_1), 
            #Write(caixas_texto_2),
            #Write(caixas_texto_resto)
        )

        self.wait(1)

        self.play(bolas_gr[0].animate.shift(UP*3.85+LEFT*2), run_time=0.3)

        for i in range(1,30):
            if i%5 !=0:
                self.play(
                    bolas_gr[i].animate.next_to(bolas_gr[i-1], RIGHT, buff=0.25),#.scale(0.8)
                    run_time=0.3
                )
            else:
                self.play(
                    bolas_gr[i].animate.next_to(bolas_gr[i-5], DOWN, buff=0.25),#.scale(0.8)
                    run_time=0.3
                )

        self.play(bolas_gr[30].animate.next_to(bolas_gr[4], RIGHT*6), run_time=0.3)
        for i in range(31,60):
            if i%5 !=0:
                self.play(
                    bolas_gr[i].animate.next_to(bolas_gr[i-1], RIGHT, buff=0.25),
                    run_time=0.3
                )
            else:
                self.play(
                    bolas_gr[i].animate.next_to(bolas_gr[i-5], DOWN, buff=0.25),
                    run_time=0.3
                )
        
        self.play(bolas_gr[60].animate.next_to(bolas_gr[42], RIGHT*15, buff=0.25), run_time=0.3)
        self.wait()

        self.play(
            Uncreate(bolas_gr),
            #Uncreate(caixas_texto_1),
            #Uncreate(caixas_texto_2),
            #Uncreate(caixas_texto_resto),
            Uncreate(caixas_03),
            run_time=0.5
        )

        self.wait()

       
        caixas_04 = VGroup(*[Square(color=DARK_BLUE, fill_opacity=1) for s in range(0,5)])
        caixas_04.arrange_in_grid(rows=1, buff=0.5).scale(0.6)

        self.play(Write(caixas_04))

        caixas_05 = caixas_04[0:4].copy()
        caixas_05.arrange_in_grid(rows=2, buff=0.5)

        plus_sig = Tex(r"+")
        plus_sig.next_to(caixas_05, RIGHT*3).scale(2)
        self.play(
            ReplacementTransform(caixas_04[0:4], caixas_05),
            Write(plus_sig)
        )
        self.wait(2)

        num_2_2 = Tex(r"2x(")
        num_2_pa = Tex(r")")
        num_2_pa.next_to(plus_sig, LEFT*2).scale(3)
        num_2_2.next_to(num_2_pa, LEFT*16).scale(3)

        self.play(
            ReplacementTransform(caixas_05[0:2], num_2_2),
            Create(num_2_pa),
            caixas_05[2:4].animate.shift(UP*.9 + LEFT*.4),
            )

        self.wait(2)

        self.play(Uncreate(caixas_05), Uncreate(num_2_pa), Uncreate(num_2_2), Uncreate(plus_sig), Uncreate(caixas_04[-1]))

        texto_math = MathTex(r"2 \cdot 2 + 1 = 5")
        texto_math.scale(2)

        self.play(Write(texto_math))
        self.wait(5)

        texto_math_2= MathTex(r" 4", "+ 1 = 5")
        texto_math_2.scale(2)
        self.play(ReplacementTransform(texto_math, texto_math_2))

        self.wait(1)

        framebox_04 =  SurroundingRectangle(texto_math_2[0], buff=0.3)
        texto_expli = MathTex(r"2 \cdot 2 \\ 4 < 5")
        texto_expli.next_to(texto_math_2[0], DOWN, buff=0.5)

        self.play(Create(framebox_04), run_time=3)
        self.play(Write(texto_expli))

        self.wait(5)
        
        self.play(
            Unwrite(texto_expli),
            Unwrite(framebox_04),
            Unwrite(texto_math_2)
        )

        self.wait(3)

        bolas_grupo= VGroup(*[Circle(radius=0.5, color=ORANGE, fill_opacity=1) for s in range(0,17)])
        bolas_grupo.arrange_in_grid(cols=5, buff=0.5)

        self.play(Create(bolas_grupo), run_time=3)

        self.wait(3)

        self.play(bolas_grupo[0:5].animate.to_corner(UL).set_fill(PURPLE_D).set_stroke(PURPLE_D))
        self.play(bolas_grupo[5:10].animate.next_to(bolas_grupo[0:5], DOWN*1.5, buff=0.5).set_fill(RED_C).set_stroke(RED_C))
        self.play(bolas_grupo[10:15].animate.next_to(bolas_grupo[5:10], DOWN*1.5, buff=0.5).set_fill(GREEN_C).set_stroke(GREEN_C))
        self.play(bolas_grupo[15:17].animate.next_to(bolas_grupo[9], RIGHT*8))

        self.wait(1)

        texto_01 = MathTex(r"3 \cdot 5 = 15")
        texto_01.move_to(DOWN*2+LEFT*3)
        
        self.play(Write(texto_01), run_time=2)

        texto_02 = MathTex(r"+2")
        texto_02.next_to(texto_01, RIGHT*20)
        self.play(Write(texto_02), run_time=2)

        textos_0102 = VGroup(texto_01, texto_02)


        texto_03 = MathTex(r"17 =", "3 \cdot 5"," + 2")
        texto_03.move_to(DOWN*2).scale(1.5)

        self.play(ReplacementTransform(textos_0102, texto_03), run_time=2)
        
        self.wait(2)

        self.play(FadeOut(bolas_grupo, shift=UP))
        self.play(texto_03.animate.shift(UP*2).scale(1.5))

        self.wait(2)

        framebox_05= SurroundingRectangle(texto_03[1], buff=0.2)
        texto_expli_2 = MathTex(r"15 < 17")
        texto_expli_2.next_to(texto_03, DOWN, buff=0.5)

        self.play(Create(framebox_05), run_time=2)
        self.wait()
        self.play(Write(texto_expli_2))

        self.wait(4)

        self.play(
            Unwrite(texto_expli_2),
            Unwrite(framebox_05),
            Unwrite(texto_03)
        )

        self.wait(3)

class segunCena(Scene):
    def construct(self):

        linha = Line([0,0,0], [2,0,0])
        linhav = Line([0,0,0], [0,1,0])
        chave_div = VGroup(linha, linhav)

        self.wait(1)
        texto_04 = Tex(r"Algoritmo da divisão")
        texto_04.scale(2)

        self.play(Write(texto_04), run_time=3)

        self.wait(2)

        texto_05 = MathTex(r"a,b \in \mathbb{Z} \\ b \neq 0")
        texto_05.move_to(LEFT*5 + UP)
        num_2 = Tex(r"b")
        num_2.move_to(UP*.5+RIGHT*1).scale(1.5)
        num_5 = Tex(r"a")
        num_5.move_to(UP*.5+LEFT*1).scale(1.5)
        num_q = Tex(r"q")
        num_q.next_to(num_2, DOWN, buff=0.5).scale(1.5)
        num_r = Tex(r"r")
        num_r.next_to(num_5, DOWN, buff=0.6).scale(1.5)
        numes = VGroup(num_5, num_2, num_r, num_q)

        texto_06 = MathTex(r"a = b \cdot ","q"," + ", "r")
        texto_06.scale(1.5)

        self.play(texto_04.animate.shift(UP*2.5).scale(0.8))
        self.play(Write(texto_05))
        self.play(Write(chave_div))
        self.play(Write(numes))

        self.wait(2)

        texto_chave = VGroup(numes, chave_div)
        self.play(
            ReplacementTransform(texto_chave, texto_06)
        )

        self.wait(3)

        framebox_10 = SurroundingRectangle(texto_06[0:2], buff=0.2)
        framebox_11 = SurroundingRectangle(texto_06[2:4], buff=0.2)

        frame_explic = VGroup(framebox_10, framebox_11)

        self.play(Write(framebox_10))
        self.wait()
        self.play(ReplacementTransform(framebox_10, framebox_11))
        self.wait()

        self.play(Unwrite(framebox_11))
        self.wait()
        self.play(
            texto_06.animate.shift(UP*1.5)
        )

        texto_07 = MathTex(r"17 = 3 \cdot "," 5 ", "+", " 2 ")
        texto_07.scale(1.5)

        self.play(Write(texto_07), run_time=2)

        self.wait(1)

        framebox_06 = SurroundingRectangle(texto_07[1], buff=0.2)
        framebox_07 = SurroundingRectangle(texto_06[1], buff=0.2)
        framebox_08 = SurroundingRectangle(texto_07[-1], buff=0.2)
        framebox_09 = SurroundingRectangle(texto_06[-1], buff=0.2)

        frame_quoci = VGroup(framebox_06, framebox_07)
        frame_resto = VGroup(framebox_08, framebox_09)

        self.play(Write(frame_quoci), run_time=2)

        self.wait()

        self.play(ReplacementTransform(frame_quoci, frame_resto), run_time=2)

        self.play(
            Unwrite(frame_resto), 
            Unwrite(texto_07),
            Unwrite(texto_06),
            Unwrite(texto_05),
            Unwrite(texto_04)
        )

        self.wait(2)



#--------------------------------------------------------3 cena
class terceiraCena(Scene):
    def construct(self):

        self.wait()
        texto_01 = MathTex(r"a = b \cdot ","q"," + ", "r")
        texto_01.scale(1.5)

        self.play(Write(texto_01))

        framebox_00 = SurroundingRectangle(texto_01[1], buff=0.2)
        framebox_01 = SurroundingRectangle(texto_01[-1], buff=0.2)
        frame_texto01 = VGroup(framebox_00, framebox_01)

        self.play(Write(frame_texto01))

        texto_02=Tex(r"?")
        texto_02.next_to(texto_01, DOWN, buff=1)

        self.play(Write(texto_02))

        self.wait(1)

        self.play(Unwrite(texto_02), Unwrite(texto_01), Unwrite(frame_texto01))

        self.wait()

class quartaCena(Scene):
    def construct(self):
        self.wait()

        linha = Line([0,0,0], [2,0,0])
        linhav = Line([0,0,0], [0,1,0])
        chave_div = VGroup(linha, linhav)

        texto_0 = MathTex(r"156")
        texto_1 = MathTex(r"77")

        texto_0.move_to(LEFT*1.5+UP*.5).scale(2)
        texto_1.move_to(RIGHT+UP*.5).scale(2)

        self.play(Write(chave_div), Write(texto_0), Write(texto_1))

        grupo_01 = VGroup(chave_div, texto_0, texto_1)
        self.play(grupo_01.animate.shift(UP*2.7).scale(.5))

        caixas_0 = VGroup(*[Square(color=DARK_BLUE, side_length=.3, fill_opacity=1) for s in range(0,156)])
        caixas_0.arrange_in_grid(rows=9, buff=0.3)

        self.wait()

        self.play(Create(caixas_0))

        self.wait()

        self.play(
            caixas_0[0:77].animate.set_fill(YELLOW).set_stroke(YELLOW),
            caixas_0[77:154].animate.set_fill(RED).set_stroke(RED)
        )

        texto_4 = texto_1.copy()
        texto_2 = Tex(r"+77")
        texto_3 = Tex(r"+2")

        texto_4.move_to(RIGHT*6+UP*2)
        texto_2.next_to(texto_4, DOWN, buff=1.8)
        texto_3.next_to(texto_2, DOWN, buff=1.8)

        self.wait()
        self.play(Write(texto_4), Write(texto_2), Write(texto_3))

        self.wait()
        self.play(
            Uncreate(texto_3),
            Uncreate(texto_2),
            Uncreate(texto_4),
            Uncreate(caixas_0),
        )

        self.play(grupo_01.animate.shift(DOWN*2.7).scale(2))

        self.wait()

        self.play(Unwrite(grupo_01))

        self.wait()

class quintaCena(Scene):
    def construct(self):
        self.wait()

        texto_150 = MathTex(r"150 = 77 \cdot 1 + 73")
        texto_150.move_to(UP*2)

        texto_156 = MathTex(r"150 + 6 = 77 \cdot 1 + 73 + 6")
        texto_156.next_to(texto_150, DOWN, buff=.5)

        texto_1561 = MathTex(r"156 = 77 \cdot 1 + 79")
        texto_1561.next_to(texto_156, DOWN, buff=.5)

        texto_1562 = MathTex(r"156 = 77 \cdot 1 + 77 \cdot 1 + 2")
        texto_1562.next_to(texto_1561, DOWN, buff=.5)

        texto_1563 = MathTex(r"156 = 77 \cdot (1+1) + 2")
        texto_1563.next_to(texto_1562, DOWN, buff=.5)
        
        texto_1564 = MathTex(r"156 = 77 \cdot ","2"," + ", "2")
        texto_1564.next_to(texto_1563, DOWN, buff=.5)

        self.play(
            Write(texto_150),
            run_time =2
        )

        self.wait(8)

        self.play(
            FadeIn(texto_156, shift=DOWN),
            run_time =2
        )
        self.wait(8)

        self.play(
            FadeIn(texto_1561, shift=DOWN),
            run_time =2
        )
        self.wait(6)

        self.play(
            FadeIn(texto_1562, shift=DOWN),
            run_time =2
        )
        self.wait(4)

        self.play(
            FadeIn(texto_1563, shift=DOWN),
            run_time =2
        )
        self.wait(4)

        self.play(
            FadeIn(texto_1564, shift=DOWN),
            run_time =2
        )
        self.wait(4)

        self.play(
            Unwrite(texto_150),
            Unwrite(texto_156),
            Unwrite(texto_1561),
            Unwrite(texto_1562),
            Unwrite(texto_1563),
        )

        self.play(
            texto_1564.animate.shift(UP*3).scale(1.5)
        )

        framebox_0 = SurroundingRectangle(texto_1564[1], buff=.2)
        framebox_1 = SurroundingRectangle(texto_1564[-1], buff=.2)

        
        self.wait(1)

        self.play(Create(framebox_0), run_time=2)
        
        self.wait(1)

        self.play(Create(framebox_1), run_time=2)

        self.wait(3)

        self.play(
            Unwrite(framebox_0),
            Unwrite(framebox_1),
            Unwrite(texto_1564),
            run_time = 2,
        )

        self.wait()


class sextaCena(Scene):
    def construct(self):
        self.wait()
        
        circunfe = Circle(radius=2, color=RED, )
        ponto = Dot()
        ponto2 = ponto.copy().shift(RIGHT*2)
    
        self.play(GrowFromCenter(circunfe), GrowFromCenter(ponto))
        self.play(Transform(ponto, ponto2))
        self.play(MoveAlongPath(ponto, circunfe), run_time=2, rate_func=linear)

        #self.wait()

        self.play(Uncreate(circunfe), Uncreate(ponto), Uncreate(ponto2))

        self.wait()

        numeros = Tex(r"0 1 2 3 4 5 6 7 8 9") 
        numeros.scale(2)

        self.play(Write(numeros), run_time=3)

        self.wait()

        self.play(Unwrite(numeros))


class decimaCena(Scene):
    def construct(self):
        self.wait()

        texto_0 = Tex(r"Posicional ", "Decimal")
        texto_0.scale(1.5)

        self.play(Write(texto_0))
        self.wait()

        self.play(texto_0.animate.shift(UP*2))

        self.play(texto_0[1].animate.set_fill(YELLOW).set_stroke(YELLOW))

        self.wait()

        txt_0 = Tex(r"0")
        txt_1 = Tex(r"1")
        txt_2 = Tex(r"2")
        txt_3 = Tex(r"3")
        txt_4 = Tex(r"4")
        txt_5 = Tex(r"5")
        txt_6 = Tex(r"6")
        txt_7 = Tex(r"7")
        txt_8 = Tex(r"8")
        txt_9 = Tex(r"9")

        numeros = VGroup(txt_0, txt_1, txt_2, txt_3, txt_4, txt_5, txt_6, txt_7, txt_8, txt_9)

        numeros.scale(3)

        self.play(Write(txt_0))
        self.play(ReplacementTransform(txt_0, txt_1))
        self.play(ReplacementTransform(txt_1, txt_2))
        self.play(ReplacementTransform(txt_2, txt_3))
        self.play(ReplacementTransform(txt_3, txt_4))
        self.play(ReplacementTransform(txt_4, txt_5))
        self.play(ReplacementTransform(txt_5, txt_6))
        self.play(ReplacementTransform(txt_6, txt_7))
        self.play(ReplacementTransform(txt_7, txt_8))
        self.play(ReplacementTransform(txt_8, txt_9))
        self.wait()

        numeros_txt = Tex(r"1","2","3")
        numeros_txt.scale(2)
        num_321 = Tex(r"3","2","1")
        num_321.next_to(numeros_txt, DOWN, buff=.5).scale(2)

        self.play(ReplacementTransform(txt_9, numeros_txt))
        self.play(
            texto_0[1].animate.set_fill(WHITE).set_stroke(WHITE),
            texto_0[0].animate.set_fill(YELLOW).set_stroke(YELLOW)
        )
        self.wait()
        self.play(FadeIn(num_321, shift=DOWN))
        self.wait()

        framebox_0 = SurroundingRectangle(numeros_txt[2], buff=0.1)
        framebox_1 = SurroundingRectangle(num_321[0], buff=0.1)

        frame= VGroup(framebox_0, framebox_1)
        self.play(Write(frame))
        self.wait(1)

        self.play(
            Unwrite(frame),
            Unwrite(num_321),
            Unwrite(numeros_txt),
            Unwrite(texto_0)
        )

        self.wait(1)

class onzeCena(Scene):
    def construct(self):
        self.wait(1)

        unidade = Square(side_length=0.2, color=YELLOW, fill_opacity=1)
        dezena = Square(side_length=0.5, color=YELLOW, fill_opacity=1)
        centena = Square(side_length=0.8, color=YELLOW, fill_opacity=1)
        milhar = Square(side_length=1.1, color=YELLOW, fill_opacity=1)

        pesos = VGroup(milhar, centena, dezena, unidade)
        pesos.arrange_in_grid(rows=1, buff=1)

        self.play(Write(milhar))
        self.wait()
        self.play(Write(centena))
        self.wait()
        self.play(Write(dezena))
        self.wait()
        self.play(Write(unidade))
        self.wait()

       
        self.play(Unwrite(pesos))
        self.wait()

class dozeCena(Scene):
    def construct(self):
        self.wait(1)

        texto_01 = MathTex("3","2","4","5","6")
        texto_01.scale(2)

        self.play(Write(texto_01), run_time=2)

        self.play(
            texto_01[0].animate.shift(LEFT),
            texto_01[1:5].animate.shift(RIGHT)
        )

        txt_104= MathTex(r"\cdot 10^4 +")
        txt_104.next_to(texto_01[0], RIGHT, buff=.5).scale(1.5)

        self.play(Write(txt_104))

        prim = VGroup(txt_104, texto_01[0], texto_01[1])

        self.play(
            prim.animate.shift(LEFT),
            texto_01[2:5].animate.shift(RIGHT)
        )

        txt_103 = MathTex(r"\cdot 10^3 +")
        txt_103.next_to(texto_01[1], RIGHT, buff=.5).scale(1.5)
        self.play(Write(txt_103))
        segund= VGroup(prim, txt_103, texto_01[2])

        self.play(
            segund.animate.shift(LEFT),
            texto_01[3:5].animate.shift(RIGHT)
        )

        txt_102 = MathTex(r"\cdot ","10^2", "+")
        txt_102.next_to(texto_01[2], RIGHT, buff=.5).scale(1.5)
        self.play(Write(txt_102))
        
        terceiro= VGroup(segund, txt_102, texto_01[3])

        self.play(
            terceiro.animate.shift(LEFT),
            texto_01[4:5].animate.shift(RIGHT)
        )

        txt_101 = MathTex(r"\cdot ","10^1"," +")
        txt_101.next_to(texto_01[3], RIGHT, buff=.5).scale(1.5)
        self.play(Write(txt_101))

        quarto= VGroup(terceiro, txt_101, texto_01[4])

        self.play(
            quarto.animate.shift(LEFT),
            #texto_01[4].animate.shift(RIGHT)
        )

        txt_100 = MathTex(r"\cdot ","10^0")
        txt_100.next_to(texto_01[4], RIGHT, buff=.5).scale(1.5)
        self.play(Write(txt_100))

        framebox_0 = SurroundingRectangle(txt_100[1], buff=.2)
        framebox_1 = SurroundingRectangle(txt_101[1], buff=.2)
        framebox_2 = SurroundingRectangle(txt_102[1], buff=.2)

        unidade= Tex(r"Unidade")
        unidade.next_to(framebox_0, DOWN, buff=0.5)
        dezena = Tex(r"Dezena")
        dezena.next_to(framebox_1, DOWN, buff=0.5)
        centena = Tex(r"Centena")
        centena.next_to(framebox_2, DOWN, buff=0.5)


        self.wait(1)

        self.play(
            Write(unidade),
            Write(framebox_0)
        )

        self.wait(1)
        self.play(
            ReplacementTransform(unidade, dezena),
            ReplacementTransform(framebox_0, framebox_1)
        )
        self.wait(1)

        self.play(
            ReplacementTransform(dezena, centena),
            ReplacementTransform(framebox_1, framebox_2)
        )
        self.wait(1)

        numer_tot = VGroup(texto_01, txt_100, txt_101, txt_102, txt_103, txt_104)
        self.play(
            Unwrite(framebox_2),
            Unwrite(centena)
        )
        self.wait()
        self.play(
            Unwrite(numer_tot)
        )
        self.wait(1)

class trezeCena(Scene):
    def construct(self):
        self.wait(1)

        texto_01 = MathTex(r"469751 = 4 \cdot 10^5 + 6 \cdot 10^4 + 9 \cdot 10^3 + 7 \cdot 10^2 + 5 \cdot 10^1 + 1 \cdot 10^0 ")

        self.play(Write(texto_01), run_time=2)

        self.wait(2)

        texto_02 = MathTex(r"384 = 3 \cdot 10^2 + 8 \cdot 10^1 + 4 \cdot 10^0")

        self.play(ReplacementTransform(texto_01, texto_02), run_time=2)
        self.wait(2)

        texto_03 = MathTex(r"64 = 6 \cdot 10^1 + 4 \cdot 10^0")
        self.play(ReplacementTransform(texto_02, texto_03), run_time=2)

        self.wait(2)
        
        texto_04 = MathTex(r"5438 = 5 \cdot ", "10^3", "+ 4 \cdot ", "10^2", "+ 3 \cdot ", "10^1", "+ 8 \cdot ", "10^0" )
        self.play(ReplacementTransform(texto_03, texto_04))

        frame0 = SurroundingRectangle(texto_04[1], buff=.2)
        frame1 = SurroundingRectangle(texto_04[3], buff=.2)
        frame2 = SurroundingRectangle(texto_04[5], buff=.2)
        frame3 = SurroundingRectangle(texto_04[7], buff=.2)

        frame = VGroup(frame0, frame1, frame2, frame3)

        self.play(Write(frame), run_time=2)

        texto_05 = Tex(r"Base 10")
        texto_05.move_to(UP*2)
        self.play(Write(texto_05))
        self.wait(2)

        self.play(Unwrite(texto_05), Unwrite(frame), Unwrite(texto_04))



        self.wait()

class catorCena(Scene):
    def construct(self):
        self.wait()

        texto_0 = Tex(r"Base binária")
        texto_0.move_to(UP*2)
        
        retang_1 = Rectangle(width=.4, height=2.0, fill_opacity=1, color=WHITE)
        retang_0 = Rectangle(width=.2, height=2.0, fill_opacity=1, color=WHITE)
        retang_0.next_to(retang_1, LEFT, buff=.5)

        self.play(Create(retang_0), Create(retang_1))

        txt_0 = Tex(r"0")
        txt_0.next_to(retang_0, DOWN, buff=.5)
        txt_1 = Tex(r"1")
        txt_1.next_to(retang_1, DOWN, buff=.5)

        self.play(Write(texto_0))


        self.wait()
        self.play(Write(txt_0), Write(txt_1))
        self.wait()
        self.play(Unwrite(txt_0), Unwrite(txt_1))

        retangulos = VGroup(retang_0, retang_1)
        txt_2 = MathTex(r"(23)_{10} = (10111)_{2} \\ (93)_{10}=(1011101)_{2}")
        self.play(
            ReplacementTransform(retangulos, txt_2)
        )
        

        self.wait(2)

class quinzeCena(Scene):
    def construct(self):
        self.wait()

        num_723 = Tex(r"7","23")
        num_5 = Tex(r"5")
        num_5.move_to(RIGHT+UP*.5)
        num_723.next_to(num_5, LEFT, buff=.5)

        linha = Line([0,0,0], [2,0,0])
        linhav = Line([0,0,0], [0,1,0])
        chave_div = VGroup(linha, linhav).scale(.5)

        grupo0 = VGroup(chave_div, num_5, num_723)
        grupo0.move_to(UP*2)

        self.play(
            Write(chave_div),
            Write(num_723),
            Write(num_5),
            run_time=.5
        )

        frame0 = SurroundingRectangle(num_5, buff=.2)
        texto0= Tex(r"Base 5")
        texto0.next_to(frame0, RIGHT, buff=.5)

        self.play(Write(frame0), Write(texto0))

        self.play(Unwrite(texto0), Unwrite(frame0))
        

        num_14 = Tex(r"14")
        num_14.next_to(num_5, DOWN)
        num_70 = Tex(r"-7","0")
        num_70.next_to(num_723[0], DOWN)

        self.play(Write(num_14), Write(num_70), run_time=.5)
        

        num_23= Tex(r"2","3")
        num_23[0].next_to(num_70[1], DOWN)
        num_23[1].next_to(num_23[0], RIGHT, buff=0.1)
        self.play(Write(num_23), run_time=.5)

        num_4 = Tex(r"4")
        num_4.next_to(num_14, RIGHT, buff=0.1)

        num_20 = Tex(r"-20")
        num_20.next_to(num_23, DOWN)

        self.play(
            Write(num_4),
            Write(num_20),
            run_time=.5
        )

        num_3 = Tex(r"3")
        num_3.next_to(num_20, DOWN)

        self.play(Write(num_3), run_time=.5)

        num_33 = num_3.copy()
        num_33.to_corner(DL)

        frame1 = SurroundingRectangle(num_3, buff=.2)
        self.play(Write(frame1), run_time=.5)

        

        #self.play(Unwrite(frame1))

        #self.play(ReplacementTransform(num_3, num_33))

        quoc_1 = VGroup(num_14, num_4, num_723, num_70, num_23, num_20,num_5, num_3,frame1, chave_div)

        self.play(quoc_1.animate.shift(LEFT))

        chave_div_2 = chave_div.copy()
        num_50 = num_5.copy()

        segunda_div = VGroup(chave_div_2, num_50)
        segunda_div.next_to(num_4, RIGHT)

        self.play(Write(chave_div_2), Write(num_50), run_time=.5)

        num_2 = Tex(r"2")
        num_2.next_to(num_50, DOWN)
        num_10 = Tex(r"-1","0")
        num_10.next_to(num_14, DOWN)

        self.play(Write(num_2), Write(num_10), run_time=.5)

        num_44 = Tex(r"44")
        num_44.next_to(num_10[1], DOWN)

        self.play(Write(num_44), run_time=.5)

        num_8 = Tex(r"8")
        num_8.next_to(num_2, RIGHT, buff=0.1)

        num_40 = Tex(r"-40")
        num_40.next_to(num_44, DOWN)

        num_4_0 = Tex(r"4")
        num_4_0.next_to(num_40, DOWN)

        self.play(Write(num_8), Write(num_40), run_time=.5)

        self.play(Write(num_4_0), run_time=.5)
        
        frame2 = SurroundingRectangle(num_4_0, buff=.2)
        self.play(Write(frame2))

        quoc_2=VGroup(quoc_1, segunda_div, num_2, num_10, num_44, num_8, num_40, num_4_0, frame2 )

        self.play(
            quoc_2.animate.shift(LEFT)
        )

        chave_div_3 = chave_div.copy()
        num_51 = num_5.copy()

        tercera_div = VGroup(chave_div_3, num_51)
        tercera_div.next_to(num_8, RIGHT)

        self.play(Write(tercera_div), run_time=.5)

        num_5_1 = Tex(r"5")
        num_5_1.next_to(num_51, DOWN)

        num_25 = Tex(r"-25")
        num_25.next_to(num_2, DOWN)

        self.play(Write(num_5_1), Write(num_25), run_time=.5)

        num_3_0 = Tex(r"3")
        num_3_0.next_to(num_25, DOWN)
        frame3 = SurroundingRectangle(num_3_0, buff=.2)

        self.play(Write(num_3_0), run_time=.5)
        self.play(Write(frame3))

        quoc_3 = VGroup(quoc_2, tercera_div, num_5_1, num_25, num_3_0, frame3)

        self.play(quoc_3.animate.shift(LEFT))

        
        chave_div_4 = chave_div.copy()
        num_52 = num_5.copy()

        
        quarta_div = VGroup(chave_div_4, num_52)
        quarta_div.next_to(num_5_1, RIGHT)

        self.play(Write(quarta_div), run_time=.5)

        num_01 = Tex(r"1")
        num_01.next_to(num_52, DOWN)

        num_53 = Tex(r"-5")
        num_53.next_to(num_5_1, DOWN)

        self.play(Write(num_01), Write(num_53), run_time=.5)

        num_00 = Tex(r"0")
        num_00.next_to(num_53, DOWN)

        frame4 = SurroundingRectangle(num_00, buff=.2)

        self.play(Write(num_00), run_time=.5)
        self.play(Write(frame4))

        quoc_4 = VGroup(quoc_3, quarta_div, num_01, num_53, num_00, frame4)
        self.play(quoc_4.animate.shift(LEFT))

        chave_div_5 = chave_div.copy()
        num_54 = num_5.copy()

        quinta_div = VGroup(chave_div_5, num_54)
        quinta_div.next_to(num_01, RIGHT)

        self.play(Write(quinta_div), run_time=.5)

        num_0 = Tex(r"0")
        num_02 = num_0.copy()
        num_0.next_to(num_54, DOWN)
        num_02.next_to(num_01, DOWN)

        self.play(Write(num_0), Write(num_02), run_time=.5)
        num_12 = num_01.copy()
        num_12.next_to(num_02, DOWN)
        self.play(Write(num_12), run_time=.5)

        frame5 = SurroundingRectangle(num_12, buff=.2)

        self.play(Write(frame5))
        quoc_5 = VGroup(quoc_4, quinta_div, num_0, num_02, num_12, frame5 )
        self.play(quoc_5.animate.shift(RIGHT))
        #------------------------------------------------------
        flexa = Arrow(start=RIGHT, end=LEFT*2, color=RED)
        flexa.move_to(DOWN*2)
        self.play(Write(flexa))
        self.play(flexa.animate.shift(LEFT*2))
        
        base_5_723 = MathTex(r"723 = (10343)_{5}")
        base_5_723.move_to(RIGHT*2+UP*2)

        self.play(Write(base_5_723))

        tudo = VGroup(quoc_5, flexa, base_5_723)

        ponto = Dot()

        self.wait(1)
        self.play(ReplacementTransform(tudo, ponto))

        self.wait(2)

class dezeceCena(Scene):
    def construct(self):
        
        ponto0 = Dot()
        self.add(ponto0)

        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt*.8)
        line_reference = Line([0,0,0], [0,2,0])
        line_moving = Line([0,0,0], [0,2,0])
        line_moving.add_updater(updater_back)
        
        self.play(ReplacementTransform(ponto0, line_reference))
        self.add(line_moving)
        self.wait(8)
        line_moving.remove_updater(updater_forth)
       
        self.play(Unwrite(line_moving), Unwrite(line_reference))

        self.wait(2)


class deseteCena(Scene):
    def construct(self):
        self.wait()

        linha0 = Line([0,0,0], [0,1,0])
        linha1= linha0.copy()
        linha1.rotate_about_origin(150*DEGREES)
        circul0 = Circle(radius=1.2, color=WHITE)

        txt_19h = Tex(r"19h")
        txt_19h.next_to(circul0, DOWN, buff=.4)
    
        sete_horas= VGroup(linha1, linha0, circul0, txt_19h)

        self.play(Write(sete_horas))
        self.play(sete_horas.animate.shift(LEFT*4+UP))

        linha2 = Line([0,0,0], [0,1,0])
        linha3 = linha2.copy()
        linha3.rotate_about_origin(120*DEGREES)
        circul1 = Circle(radius=1.2, color=WHITE)
        txt_8h = Tex(r"8h")
        txt_8h.next_to(circul1, DOWN, buff=.4)

        oito_horas = VGroup(linha2, linha3, circul1, txt_8h)


        self.play(Write(oito_horas))
        self.play(oito_horas.animate.shift(UP))
        plus = Tex(r"+")
        plus.next_to(circul0, RIGHT, buff=.6).scale(1.5)

        self.play(Write(plus))

        equal = Tex(r"=")
        equal.next_to(circul1, RIGHT, buff=.6).scale(1.5)
        self.play(Write(equal))
        
        linha4 = Line([0,0,0], [0,1,0])
        linha5 = linha4.copy()
        linha5.rotate_about_origin(-90*DEGREES)
        circul2 = Circle(radius=1.2, color=WHITE)
        txt_3h = Tex(r"27h = 3h")
        txt_3h.next_to(circul2, DOWN, buff=.4)

        tres_horas = VGroup(linha4, linha5, circul2, txt_3h)

        tres_horas.move_to(RIGHT*4+UP*.5)
        self.play(Write(tres_horas))

        self.wait()

        self.play(Unwrite(sete_horas), Unwrite(oito_horas), Unwrite(tres_horas), Unwrite(plus), Unwrite(equal))


        self.wait(2)


class oitodezCena(Scene):
    def construct(self):
        self.wait()

        pontos_0 = VGroup(*[Dot(color=PINK) for s in range(0,333)])
        pontos_0.arrange_in_grid(rows=10)

        self.play(Create(pontos_0), run_time=3)
        self.wait(3)

        pontos_1 = VGroup(*[Dot(color=PINK) for s in range(0,33)])
        pontos_1.arrange_in_grid(rows=4)

        self.play(ReplacementTransform(pontos_0, pontos_1))
        self.wait()

        conta_1 = MathTex("33 = 4 \cdot 8 + 1")
        conta_1.move_to(UP*3.5+LEFT*4)

        self.play(
            Write(conta_1), 
            pontos_1[0:32].animate.set_fill(WHITE)
        )

        conta_2 = MathTex(r"33 \cdot 10 = (4 \cdot 8 + 1) \cdot 10")
        conta_2.move_to(UP*2.5 + LEFT*4)

        pontos_2 = VGroup(*[Dot(color=PINK) for s in range(0,330)])
        pontos_2.arrange_in_grid(rows=10).move_to(DOWN)
        pontos_2[0:32].set_fill(WHITE)

        self.wait(4)
        self.play(ReplacementTransform(pontos_1, pontos_2), Write(conta_2))
        conta_3 = MathTex(r"330 = 40 \cdot 8 + 10")
        conta_3.next_to(conta_2, DOWN, buff=.5)

        self.play(
             pontos_2[0:320].animate.set_fill(WHITE),
        )

        self.play(pontos_2.animate.arrange_in_grid(rows=17).move_to(RIGHT*3))

        self.wait(4)
        self.play(Write(conta_3))

        pontos_3 = VGroup(*[Dot(color=WHITE) for s in range(0,333)])
        pontos_3.arrange_in_grid(rows=17).move_to(RIGHT*3)
        pontos_3[328:333].set_fill(PINK)

        conta_4 = MathTex(r"330 + 3 = 40 \cdot 8 + 10 + 3")

        conta_4.next_to(conta_3, DOWN, buff=.5)

        conta_5 = MathTex(r"333 = 8 \cdot (40 + 1) + 5")
        conta_5.next_to(conta_4, DOWN, buff=.5)
        conta_6 = MathTex(r"333 = 8 \cdot 41 + 5")
        conta_6.next_to(conta_5, DOWN, buff=.5)

        self.play(Write(conta_4))
        self.wait(4)
        self.play(ReplacementTransform(pontos_2, pontos_3))
        self.wait(4)
        self.play(Write(conta_5))
        self.wait(4)
        self.play(Write(conta_6))

        self.wait(4)
        ponto = Dot()

        tudo = VGroup(pontos_3, conta_6, conta_5, conta_4, conta_3, conta_2, conta_1)

        self.play(
            ReplacementTransform(tudo, ponto),
            run_time=2
        )
        self.wait()

        self.play(FadeOut(ponto))

class novedezCena(Scene):
    def construct(self):
        self.wait()
        bolas_gr = VGroup(*[Circle(radius=0.2, color=WHITE, fill_opacity=1) for s in range(0,67)])

        bolas_gr.arrange_in_grid(rows=5, buff=0.3)


        self.play(Create(bolas_gr), run_time=2)

        self.wait(3)
        self.play(
            bolas_gr[0:33].animate.set_fill(YELLOW).set_stroke(YELLOW),
            bolas_gr[33:66].animate.set_fill(RED).set_stroke(RED),
            run_time=2
        )

        conta_01 = MathTex(r"67 = 2 \cdot 33 + 1")
        conta_01.move_to(UP*2.5)

        self.play(Write(conta_01))

        conta_02 = MathTex(r" 67 = 3 \cdot 22 +1")
        conta_02.move_to(UP*2.5)

        self.wait(3)
        self.play(
            bolas_gr[0:22].animate.set_fill(YELLOW).set_stroke(YELLOW),
            bolas_gr[22:44].animate.set_fill(RED).set_stroke(RED),
            bolas_gr[44:66].animate.set_fill(BLUE).set_stroke(BLUE),
            ReplacementTransform(conta_01, conta_02)
        )

        conta_03 = MathTex(r"67 = 4 \cdot 16 + 3")
        conta_03.move_to(UP*2.5)
        
        self.wait(3)
        self.play(
            bolas_gr[0:16].animate.set_fill(YELLOW).set_stroke(YELLOW),
            bolas_gr[16:32].animate.set_fill(RED).set_stroke(RED),
            bolas_gr[32:48].animate.set_fill(BLUE).set_stroke(BLUE),
            bolas_gr[48:64].animate.set_fill(PINK).set_stroke(PINK),
            bolas_gr[64:67].animate.set_fill(WHITE).set_stroke(WHITE),
            ReplacementTransform(conta_02, conta_03)
        )
        self.wait(2)

        self.play(
            FadeOut(bolas_gr),
            FadeOut(conta_03)
        )
        self.wait()



class vinteCena(Scene):
    def construct(self):
        self.wait()

        linha0 = Line([0,0,0], [2,0,0])
        linhav0 = Line([0,0,0], [0,1,0])
        chave_div0 = VGroup(linha0, linhav0)

        self.wait(1)
        texto_04 = Tex(r"Algoritmo da ","Divisão")
        texto_04.scale(1.5)

        self.play(Write(texto_04), run_time=3)

        self.wait(1)

        self.play(texto_04.animate.shift(UP*2.5))
        texto_05 = MathTex(r"a,b \in \mathbb{Z} \\ b \neq 0")
        texto_05.move_to(LEFT*5 + UP)
        num_2 = Tex(r"b")
        num_2.move_to(UP*.5+RIGHT*1).scale(1.5)
        num_5 = Tex(r"a")
        num_5.move_to(UP*.5+LEFT*1).scale(1.5)
        num_q = Tex(r"q")
        num_q.next_to(num_2, DOWN, buff=0.5).scale(1.5)
        num_r = Tex(r"r")
        num_r.next_to(num_5, DOWN, buff=0.6).scale(1.5)
        numes = VGroup(num_5, num_2, num_r, num_q)

        quoci = VGroup(chave_div0, numes)
        quoci.move_to(DOWN*.5)
        texto_06 = MathTex(r"a = b \cdot ","q"," + ", "r")
        texto_06.scale(1.5)

        self.play( Write(texto_05), Write(texto_06), run_time=2)

        self.wait()
        self.play(texto_06.animate.shift(UP*1.5))
        self.play(Write(quoci))

        self.wait()

        self.play(
            FadeOut(quoci, shift=LEFT),
            FadeOut(texto_06, shift=LEFT),
            FadeOut(texto_05, shift=LEFT),
            FadeOut(texto_04[0], shift=LEFT),
            texto_04[1].animate.shift(LEFT*1.5),
            run_time=.8
        )

        linha0 = Line([0,0,0], [2,0,0])
        linhav1 = Line([0,0,0], [0,1,0])
        chave_div_2 = VGroup(linha0, linhav1)

        #-----

        
        num_23 = Tex(r"23")
        num_20 = Tex(r"2")
        num_20.move_to(RIGHT+UP*.5)
        num_23.next_to(num_20, LEFT, buff=.5)

        linha = Line([0,0,0], [2,0,0])
        linhav = Line([0,0,0], [0,1,0])
        chave_div = VGroup(linha, linhav).scale(.5)

        grupo0 = VGroup(chave_div, num_20, num_23)
        grupo0.move_to(UP*2)

        self.play(
            Write(chave_div),
            Write(num_23),
            Write(num_20),
            run_time=.5
        )

        frame0 = SurroundingRectangle(num_5, buff=.2)
        texto0= Tex(r"Base 5")
        texto0.next_to(frame0, RIGHT, buff=.5)

        #self.play(Write(frame0), Write(texto0))

        #self.play(Unwrite(texto0), Unwrite(frame0))
        

        num_11 = Tex(r"11")
        num_11.next_to(num_20, DOWN)
        num_22 = Tex(r"-22")
        num_22.next_to(num_23[0], DOWN)

        self.play(Write(num_11), Write(num_22), run_time=.5)
        

        num_010= Tex(r"1")
        num_010.next_to(num_22, DOWN)
        self.play(Write(num_010), run_time=.5)

        frame1 = SurroundingRectangle(num_010, buff=.2)
        self.play(Write(frame1), run_time=.5)

        quoc_1 = VGroup(chave_div, num_23, num_20, num_11, num_22, num_010, frame1)

        self.play(quoc_1.animate.shift(LEFT), run_time=.5)

        chave_div_2 = chave_div.copy()
        num_21 = num_20.copy()

        segunda_div = VGroup(chave_div_2, num_21)
        segunda_div.next_to(num_11, RIGHT)

        self.play(Write(segunda_div), run_time=.5)

        num_50 = Tex(r"5")
        num_50.next_to(num_21, DOWN)
        num_10 = Tex(r"-10")
        num_10.next_to(num_11, DOWN)

        self.play(Write(num_50), Write(num_10), run_time=.5)

        num_011 = Tex(r"1")
        num_011.next_to(num_10, DOWN)

        self.play(Write(num_011), run_time=.5)
       
        frame2 = SurroundingRectangle(num_011, buff=.2)
        self.play(Write(frame2))

        quoc_2=VGroup(quoc_1, segunda_div, frame2,num_50, num_10, num_011 )

        self.play(quoc_2.animate.shift(LEFT))

        chave_div_3 = chave_div.copy()
        num_022 = num_20.copy()

        tercera_div = VGroup(chave_div_3, num_022)
        tercera_div.next_to(num_50, RIGHT)

        self.play(Write(tercera_div), run_time=.5)

        num_021 = Tex(r"2")
        num_021.next_to(num_022, DOWN)

        num_04 = Tex(r"-4")
        num_04.next_to(num_50, DOWN)

        self.play(Write(num_021), Write(num_04), run_time=.5)

        num_012 = Tex(r"1")
        num_012.next_to(num_04, DOWN)
        frame3 = SurroundingRectangle(num_012, buff=.2)

        self.play(Write(num_012), run_time=.5)
        self.play(Write(frame3))

        quoc_3 = VGroup(quoc_2, tercera_div, frame3, num_021, num_04,num_012)

        self.play(quoc_3.animate.shift(LEFT))

        
        chave_div_4 = chave_div.copy()
        num_023 = num_20.copy()

        
        quarta_div = VGroup(chave_div_4, num_023)
        quarta_div.next_to(num_021, RIGHT)

        self.play(Write(quarta_div), run_time=.5)

        num_013 = Tex(r"1")
        num_013.next_to(num_023, DOWN)

        num_024 = Tex(r"-2")
        num_024.next_to(num_021, DOWN)

        self.play(Write(num_013), Write(num_024), run_time=.5)

        num_00 = Tex(r"0")
        num_00.next_to(num_024, DOWN)

        frame4 = SurroundingRectangle(num_00, buff=.2)

        self.play(Write(num_00), run_time=.5)
        self.play(Write(frame4))

        quoc_4 = VGroup(quoc_3, quarta_div, num_00, frame4, num_013, num_024)
        self.play(quoc_4.animate.shift(LEFT))

        chave_div_5 = chave_div.copy()
        num_025 = num_20.copy()

        quinta_div = VGroup(chave_div_5, num_025)
        quinta_div.next_to(num_013, RIGHT)

        self.play(Write(quinta_div), run_time=.5)

        num_0 = Tex(r"0")
        num_02 = num_0.copy()
        num_0.next_to(num_025, DOWN)
        num_02.next_to(num_013, DOWN)

        self.play(Write(num_0), Write(num_02), run_time=.5)
        num_12 = num_013.copy()
        num_12.next_to(num_02, DOWN)
        self.play(Write(num_12), run_time=.5)

        frame5 = SurroundingRectangle(num_12, buff=.2)

        self.play(Write(frame5))
        quoc_5 = VGroup(quoc_4, quinta_div, num_0, num_02, num_12, frame5 )
        self.play(quoc_5.animate.shift(RIGHT))
        #------------------------------------------------------
        flexa = Arrow(start=RIGHT, end=LEFT*2, color=RED)
        flexa.move_to(DOWN*2)
        self.play(Write(flexa))
        self.play(flexa.animate.shift(LEFT*2))
        
        base_2_23 = MathTex(r"23 = (10111)_{2}")
        base_2_23.move_to(RIGHT*2+UP*1.5)

        self.play(Write(base_2_23))

        self.wait()

        self.play(
            FadeOut(base_2_23),
            FadeOut(quoc_5),
            FadeOut(flexa),
            FadeOut(texto_04[1])

        )

        self.wait(2)

class ultimaCena(Scene):
    def construct(self):
        self.wait()

        tarefa_1 = Tex(r"Faça a divisão de 538 por 25 e encontre o resto e o quociente. \\ 1.Tente fazer primeiro uma estimativa. \\ 2. Use o Algorítmo da Divisão para escrever: \\ $538 = 25 \cdot q + r$,     com $0 \le r < 25$ ")


        self.play(Write(tarefa_1), run_time=4)
        self.wait()

        self.play(tarefa_1.animate.shift(UP*2).scale(.8))

        tarefa_2 = Tex(r"Desafio extra: \\ Converta o número 45 (base 10) para a base 3. \\ Lembre-se: Divida sucessivamente por 3, \\ guarde os restos e leia de baixo para cima!")

        tarefa_2.move_to(DOWN)
        self.play(Write(tarefa_2), run_time=4)

        self.wait()

        self.play(tarefa_2.animate.shift(DOWN).scale(.8))
        self.wait()

        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line([0,0,0], [0,.5,0])
        line_moving = Line([0,0,0], [0,.5,0])
        line_moving.add_updater(updater_back)
        circul= Circle(radius=.7, color=WHITE)
        self.play(Write(line_reference), Write(circul))
        self.add(line_moving)
        self.wait(15)
       
        self.play(Unwrite(line_moving), Unwrite(line_reference), Unwrite(circul))
        self.play(Unwrite(tarefa_1), Unwrite(tarefa_2))
        
        self.wait(2)
