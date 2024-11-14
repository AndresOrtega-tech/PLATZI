a = input("¿piedra, papel o tijera?: ")
b = input("¿piedra, papel o tijera?:  ")



if a  == "piedra" and b == "papel":
    
    print("Sus respuestas fueron: " +a+" y "+b+ ". El papel gana al envolver la piedra. La roca pierde")

if a  == "papel" and b == "piedra":
    
    print("Sus respuestas fueron: " +a +" y "+b+ ". El papel gana al envolver la piedra. La roca pierde")


if a  == "piedra" and b == "tijera":
    
    print("Sus respuestas fueron: "+a +" y "+b+ ". La roca gana al aplastar la tijera. La tijera pierde")

if a  == "tijera" and b == "piedra":
    
    print("Sus respuestas fueron: "+a +" y "+b+ ". La roca gana al aplastar la tijera. La tijera pierde")
    

if a  == "papel" and b == "tijera":
    
    print("Sus respuestas fueron: "+a +" y "+b+ ". La tijera gana al cortar el papel. El papel pierde")
    
if a  == "tijera" and b == "papel":
    
    print("Sus respuestas fueron: "+a +" y "+b+ ". La tijera gana al cortar el papel. El papel pierde")