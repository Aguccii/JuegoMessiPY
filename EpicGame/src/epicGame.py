import pygame, sys, random, pygame.mixer

# Lider de proyecto: Lautaro Corceiro

# Desarrolladores: Lucas Martin Mascaro - Erika Sofía Franco - Franco Navarro - Agustin Scellato


pygame.init()
pygame.mixer.init()


#Cargar sonido
sonido_pelota = pygame.mixer.Sound('src/assets/efecto.mp3')
sonido_pelota.set_volume(0.3)
sonido_pelota_especial = pygame.mixer.Sound('src/assets/dorado.mp3')
sonido_pelota_especial.set_volume(0.3)
sonido_pelota_extra = pygame.mixer.Sound('src/assets/ohno.mp3')
sonido_pelota_extra.set_volume(0.3)

#Acá puse algo por poner, si encuentran algo mejor lo cambiamos
pygame.mixer.music.load('src/assets/musica de fondo.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("src/assets/Juego de Pelotas")

# Cargar la imagen de fondo
fondo = pygame.image.load('src/assets/arco_futbol.jpg') 
fondo = pygame.transform.scale(fondo, (width, height))

# Cargar la imagen del título
titulo = pygame.image.load('src/assets/inicio.png') 
titulo = pygame.transform.scale(titulo, (width, height))

# Cargar instrucciones
instrucciones = pygame.image.load('src/assets/Instrucciones.png') 
instrucciones = pygame.transform.scale(instrucciones, (width, height))

clock=pygame.time.Clock()

tiempo_bonus = 0

tiempo_penalizacion = 0

pausa = False

#seccion de intro
esta_intro = True
mostrar_instrucciones = False
tecla_enter_presionada = False
tiempo_inicial = pygame.time.get_ticks()
while esta_intro:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        

    if not mostrar_instrucciones:
        screen.blit(titulo, ((width // 2) - (titulo.get_width() // 2), (height // 2) - (titulo.get_height() // 2)))
    else:
        screen.blit(instrucciones, ((width // 2) - (instrucciones.get_width() // 2), (height // 2) - (instrucciones.get_height() // 2)))
    
    pygame.display.update()

    tecla = pygame.key.get_pressed()

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_RETURN] and not tecla_enter_presionada:
        if not mostrar_instrucciones:
            mostrar_instrucciones = True
        else:
            esta_intro = False
            juego_en_ejecucion = True

    tecla_enter_presionada = tecla[pygame.K_RETURN]

    pygame.display.update()
    clock.tick(30)
    
    if not esta_intro:
        break

clock = pygame.time.Clock()


class Pelota(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load('src/assets/pelota.png')  
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, width - 30 - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(10, 15)
        self.puntaje = self.speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(30, width - 30 - self.rect.width)
            self.speed = random.randint(10, 15)
            self.puntaje = self.speed

    def reiniciar(self):
        self.rect.x = random.randint(30, width - 30 - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(10, 15)
        self.puntaje = self.speed
    

class Pelota_especial(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load('src/assets/pelotaesp.png')  
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, width - 30-  self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(15, 20)
        self.puntaje = 30

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(30, width - 30 - self.rect.width)
            self.speed = random.randint(15, 20)
            self.puntaje = 30
            
    def reiniciar(self):
        self.rect.x = random.randint(30, width - 30 - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(15, 20)
        self.puntaje = 30


class Pelota_extra(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load('src/assets/pelota_extra.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, width - 30 - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(15, 20)
        self.puntaje = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(30, width - 30 - self.rect.width)
            self.speed = random.randint(15, 20)
    
    def reiniciar(self):
        self.rect.x = random.randint(30, width - 30 - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(15, 20)


class Personaje(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load('src/assets/messi.png')  
        self.image = pygame.transform.smoothscale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height - self.rect.height
        self.velocidad_original = 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad_original  
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad_original 
            
    def reiniciar(self):
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height - self.rect.height
        self.image = pygame.image.load('src/assets/messi.png')  
        self.image = pygame.transform.smoothscale(self.image, (tamaño_personaje, tamaño_personaje))
        self.velocidad_original = 20       



# Tamaños de la pelota y el personaje
tamaño_pelota = 75
tamaño_pelota_especial = 85
tamaño_pelota_extra = 65
tamaño_personaje = 150

personaje = Personaje(tamaño_personaje)
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(personaje)

pelotas = pygame.sprite.Group()
tiempo_creacion_pelota = 500
tiempo_ultima_creacion = pygame.time.get_ticks()
puntaje_total = 0

pelotas_especiales = pygame.sprite.Group()
tiempo_creacion_pelota_especial = 9000
tiempo_ultima_creacion_especial = pygame.time.get_ticks()

pelotas_extra = pygame.sprite.Group()
tiempo_creacion_pelota_extra = 9000
tiempo_ultima_creacion_extra = pygame.time.get_ticks()
puntaje_total = 0

mejor_puntaje = 0


# Duración del juego en segundos
duracion_juego = 60
tiempo_inicio_juego = pygame.time.get_ticks()
juego_en_ejecucion = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:

                puntaje_total = 0
                tiempo_inicio_juego = pygame.time.get_ticks()
                juego_en_ejecucion = False

                for pelota in pelotas:
                    pelota.reiniciar()

                for pelota_especial in pelotas_especiales:
                    pelota_especial.reiniciar()
                    
                for pelota_extra in pelotas_extra:
                    pelota_extra.reiniciar()

                personaje.reiniciar()
                
                personaje.rect.x = width // 2 - personaje.rect.width // 2
                personaje.rect.y = height - personaje.rect.height

                tiempo_ultima_creacion = pygame.time.get_ticks()
                tiempo_ultima_creacion_especial = pygame.time.get_ticks()
                tiempo_ultima_creacion_extra = pygame.time.get_ticks()
            
            if event.key == pygame.K_p:
                pausa = not pausa

    if not pausa:
        tiempo_actual = pygame.time.get_ticks()
    
    if pausa:
        # Agrega el código para mostrar la pantalla de pausa
        font_pausa = pygame.font.Font(None, 72)
        texto_pausa = font_pausa.render('Pausa', True, (227, 0, 0))
        screen.blit(texto_pausa, (width // 2 - texto_pausa.get_width() // 2, height // 2 - texto_pausa.get_height() // 2))
        pygame.display.flip()
        continue

    tiempo_actual = pygame.time.get_ticks()
    # Muestra el título al principio
    if not juego_en_ejecucion:
        screen.blit(titulo, (0, 0))
        pygame.display.flip()
        pygame.time.wait(2)  # Espera 2 segundos antes de comenzar el juego
        juego_en_ejecucion = True
        tiempo_inicio_juego = pygame.time.get_ticks()


    # Comienza el juego después de mostrar el título
    elif tiempo_actual - tiempo_inicio_juego < duracion_juego * 1000:
        if tiempo_actual - tiempo_ultima_creacion > tiempo_creacion_pelota:
            nueva_pelota = Pelota(tamaño_pelota)
            pelotas.add(nueva_pelota)
            todos_los_sprites.add(nueva_pelota)
            tiempo_ultima_creacion = tiempo_actual


        if tiempo_actual - tiempo_ultima_creacion_especial > tiempo_creacion_pelota_especial:
            nueva_pelota_especial = Pelota_especial(tamaño_pelota_especial)
            pelotas_especiales.add(nueva_pelota_especial)
            todos_los_sprites.add(nueva_pelota_especial)
            tiempo_ultima_creacion_especial = tiempo_actual


        if tiempo_actual - tiempo_ultima_creacion_extra > tiempo_creacion_pelota_extra:
            nueva_pelota_extra = Pelota_extra(tamaño_pelota_extra)
            pelotas_extra.add(nueva_pelota_extra)
            todos_los_sprites.add(nueva_pelota_extra)
            tiempo_ultima_creacion_extra = tiempo_actual

        
    
        todos_los_sprites.update()


        colisiones = pygame.sprite.spritecollide(personaje, pelotas, True)
        for pelota in colisiones:
            puntaje_total += pelota.puntaje
            sonido_pelota.play()
        
        
        colisiones = pygame.sprite.spritecollide(personaje, pelotas_especiales, True)
        for pelota_especial in colisiones:
            puntaje_total += (5 * pelota.puntaje)
            sonido_pelota_especial.play()
            tamaño_original = 150  
            tamaño_aumentado = (tamaño_original * 6) // 5 
            personaje.image = pygame.transform.smoothscale(personaje.image, (tamaño_aumentado, tamaño_aumentado))
            tiempo_bonus += 1
            personaje.velocidad_original = 20
            
            
        colisiones = pygame.sprite.spritecollide(personaje, pelotas_extra, True)
        for pelota_extra in colisiones:
            puntaje_total -= (5 * pelota.puntaje)
            sonido_pelota_extra.play()
            tamaño_original = 150  
            tamaño_reducido = (tamaño_original // 3) * 2  
            personaje.image = pygame.transform.smoothscale(personaje.image, (tamaño_reducido, tamaño_reducido))
            tiempo_penalizacion += 1
            personaje.velocidad_original = 10
            

      
        # Dibujar el fondo antes de los sprites
        screen.blit(fondo, (0, 0))

        # Dibujar los sprites en la pantalla
        todos_los_sprites.draw(screen)

        # Puntaje que se va obteniendo
        font = pygame.font.Font(None, 36)
        texto_puntaje = font.render(f'Puntaje: {puntaje_total}', True, (255, 255, 255))
        screen.blit(texto_puntaje, (10, 10))

        #Muestra el mejor puntaje obtenido
        font_hi_score = pygame.font.Font(None, 36)
        texto_hi_score = font_hi_score.render(f'HI-SCORE: {mejor_puntaje}', True, (255, 255, 255))
        screen.blit(texto_hi_score, (width - texto_hi_score.get_width() - 10, 10))

        #Muestra el tiempo de juego
        tiempo_restante = duracion_juego - (tiempo_actual - tiempo_inicio_juego) // 1000 + tiempo_bonus - tiempo_penalizacion
        radio_circulo = 30
        pygame.draw.circle(screen, (169, 169, 169), (width // 2, 50), radio_circulo)  # Círculo de color gris centrado en la parte superior
        font_tiempo = pygame.font.Font(None, 36)
        texto_tiempo = font_tiempo.render(str(tiempo_restante), True, (255, 255, 255))
        texto_rect = texto_tiempo.get_rect(center=(width // 2, 50))  # Centro del texto en el centro del círculo
        screen.blit(texto_tiempo, texto_rect.topleft)

    # Muestra el puntaje final después de que termina el tiempo del juego
    else:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 72)
        texto_final = font.render(f'Puntaje final: {puntaje_total}', True, (255, 255, 255))
        screen.blit(texto_final, (width // 2 - texto_final.get_width() // 2, height // 2 - texto_final.get_height() // 2))

        if puntaje_total>mejor_puntaje:
            mejor_puntaje = puntaje_total

        texto_mejor_puntaje = font.render(f'HI-SCORE: {mejor_puntaje}', True, (255, 255, 255))
        screen.blit(texto_mejor_puntaje, (width // 2 - texto_mejor_puntaje.get_width() // 2, height // 2 - texto_mejor_puntaje.get_height() // 2 - 50))

        font = pygame.font.Font(None, 69)
        texto_reintentar = font.render('Presiona R para jugar nuevamente', True, (255, 255, 255))
        screen.blit(texto_reintentar, (width // 2 - texto_reintentar.get_width() // 2, height // 2 + 100))




    pygame.display.flip()


    clock.tick(30)