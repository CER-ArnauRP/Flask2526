
# Per fer la web, utilitzem Flask.
# Flask no ve incorporat amb Python, l'hem de descarregar.
# Si el descarreguem directament, l'instal·larà al sistema.
#   No és el que volem, ni el que s'acostuma a fer.
#   Farem lo habitual, que és crear un entorn virtual.
#   Hi ha diferents tipus d'entorn virtual, el més utilitzat 
#       és el "venv". Farem servir aquest.

# Amb un entorn virtual, les dependències com Flask, 
#   s'instal·laran en l'entorn virtual, no en el PC o MAC, etc.

# Aquest entorn virtual formarà part del projecte.

# Per crear l'entorn virtual venv:
#   En Windows: python -m venv venv
#   En Linux o MacOS: python3 -m venv venv

# En la carpeta venv creada, hi ha una còpia de Python,
#   i també s'hi poden afegir les dependències del projecte.

# En VS Code i en Antigravity, al crear venv, apareix un 
#   PopUp que diu: "We noticed a new environment has been 
#       created. Do you want to use it?" Diem que "Yes".

# Si s'ha tancat i no hem pogut dir "Yes", podem fer:
#   Ctrl + Shif + p, i buscar "Python: Select Interpreter", 
#   i triar l'opció que diu "(venv) Recommended".
#       - Això el que fa és dir-li que per executar Python
#       en aquest projecte, faci servir la versió que hi ha 
#       en el venv d'aquest projecte, i no la global.

# Amb això ja tenim el venv a punt. Per fer-lo servir (activar-lo):
#   En Window:          venv\Scripts\activate
#   En Linux o MacOS:   source venv/bin/activate

# L'entorn virtual es desctiva sol al tancar la IDE o la terminal.
#   També podem escriure a la terminal: deactivate
#       (igual per Windows que per Linux o MacOS)

# En activar-se, a la terminal, dirà "(venv)" al principi.
#   Si dona error: 
#       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Ara ja podem afegir la dependència de Flask. Per fer-ho:
#   pip install flask
#       pip és el gestor de dependències de Python.

# Per crear l'arxiu que llista les dependències del projecte:
#   pip freeze > requirements.txt
#       Cada vegada que afegim una dependència, haurem de tornar a fer la 
#           comanda (perquè actualitzi l'arxiu).

