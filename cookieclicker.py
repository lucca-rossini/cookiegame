# Exercício: Debugar o código linha por linha - feito

import turtle # Importa a biblioteca turtle, que permite criar janelas e utilizar funcoes graficas

wn = turtle.Screen() # Cria uma tela da bibilhoteca turtle, denominada wn
wn.title("TheCookieGame by luquinha") # Titulo da janela criada
wn.bgcolor("black") # Cor de fundo da janela criada
wn.register_shape("cookie.gif") # "Pre-load" da imagem cookie.gif na janela

cookie = turtle.Turtle() # Cria o objeto cookie da subclasse Turtle (pertencente a classe RawTurtle), o objeto é capaz de inserir desenhos/imagens na tela
cookie.shape("cookie.gif") # Cria a forma já registrada em register_shape, e a apresenta na tela
cookie.speed(0) # Velocidade da animação = 0 // assim, o valor 0 indica que nao ha animacao alguma no objeto cookie

clicks = 0 # variavel que ira armazenar a quantidade de clicks

pen = turtle.Turtle() # cria mais um objeto na subclasse turtle, o nome pen foi dado pois sera utilizado para escrever na tela
pen.hideturtle() # Esconde a turtle (que aparece como uma setinha por baixo do cookie) segundo a documentacao deixa a velocidade do desenho melhor
pen.color("white") # Define a cor dos desenhos do objeto pen
pen.penup() # Deixa a caneta para cima (??) em termos praticos observei que na ausência do comando a tela começa com uma fina linha do meio do cookie até o texto exibido
pen.goto(0, 200) # Define as coordenadas (x, y) para que irao as coisas escritas pelo objeto pen 
pen.write(f"Clicks: {clicks}", align="center", font=("Times New Roman", 32, "italic")) # Define o objeto pen para escrever o valor armazenado pela variável clicks


# Nota: o argumento de coordenadas pode ser utilizado para aperfeicoar o local dos clicks, definindo que caso o click esteja fora do raio do cookie ele nao sera contabilizado

# Parte totalmente autoral

dols = 0

dolars = turtle.Turtle()
dolars.hideturtle()
dolars.color("green")
dolars.pu()
dolars.goto(-300, 200)
dolars.write(f"US$ {dols}", align="center", font=("Times New Roman", 32, "italic"))

def howmoney(x, y):
    global clicks, dols
    
    if clicks < 100:
        dols = clicks * 3
    elif (clicks < 200) and (clicks > 100):
        dols = clicks * 4
    
    dolars.clear()
    dolars.write(f"US$ {dols}", align="center", font=("Times New Roman", 32, "italic"))
    
    clicks += 1 # Soma 1 ao valor de clicks quando a funcao é chamada
    pen.clear() # Limpa tudo o que o objeto tiver desenhado, na ausencia do metodo os textos ficarao sobrepostos e nao legiveis
    pen.write(f"Clicks: {clicks}", align="center", font=("Times New Roman", 32, "italic")) # Escreve novamente o numero de clicks na tela, agora acrescidos de mais um click

cookie.onclick(howmoney)

wn.mainloop() # Inicia o loop dos eventos na janela principal, o programa rodou aparentemente bem sem a declaracao, porem na documentacao insta que esse deve ser o ultimo paramentro de uma aplicacao grafica turtle
