from datetime import datetime
from src.config import las_config
from src.hamta import hamta_avgangar
from src.resultat import skriv_resultat
from src.transformera import platta_ut_avgangar
from src.validera import validera_post

def main():
    config = las_config()
    
    svar = hamta_avgangar() 
    avgangar = platta_ut_avgangar(svar)
    
    print(f"Antal hämtade avgångar: {len(avgangar)}")
    

if __name__ == "__main__":
    main()
