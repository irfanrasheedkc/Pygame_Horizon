        if player1_frozen:
            pass
        else:
            #configuring buttons
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    player1speed+=speed
                if event.key==pygame.K_w:
                    player1speed-=speed
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_s:
                    player1speed-=speed
                if event.key==pygame.K_w:
                    player1speed+=speed 

        if player2_frozen:
            pass
        else:        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    player2speed+=speed
                if event.key==pygame.K_UP:
                    player2speed-=speed 
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN:
                    player2speed-=speed
                if event.key==pygame.K_UP:
                    player2speed+=speed 