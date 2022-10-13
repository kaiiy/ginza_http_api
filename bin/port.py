from dotenv import load_dotenv
import os
load_dotenv()

def load_port():
    port = 8080

    if ginza_port := os.getenv("GINZA_PORT"):
        port = ginza_port
    
    return port