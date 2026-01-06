import requests
import sys

ASCII_HEADER = """
░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░
"""

EMAIL_API_KEY = "79b1fc948c11a00658d5ee891170fce12f574410"
PHONE_API_KEY = "a690589425a39f001d0e6269146735e1"
ABSTRACT_API_KEY = "b8042c27070d4c2e808b267a16dcb722"

DISCORD_LINKS = ["https://discord.gg/yVwNCfEx"]

def print_discord_links():
    print("\n🔗 Rejoins-nous sur Discord :")
    for link in DISCORD_LINKS:
        print(f" > {link}")
    print("\n")

def phone_lookup():
    print("\n--- PHONE LOOKUP V1 ---")
    phone = input("Entrez le numéro (ex : +33612345678) : ").strip()


    try:
        print("\n[🔍 Numverify] Informations générales...")
        url = f"http://apilayer.net/api/validate?access_key={PHONE_API_KEY}&number={phone}&format=1"
        res = requests.get(url)
        data = res.json()

        if data.get('valid'):
            print(f"✔️ Numéro valide")
            print(f"🌍 Pays : {data.get('country_name')} ({data.get('country_code')})")
            print("🏙️ Localisation : pas disponible")
            print(f"📞 Format national : {data.get('local_format')}")
            print(f"🌐 Format international : {data.get('international_format')}")
            print(f"📶 Opérateur : {data.get('carrier')}")
            print(f"📱 Type de ligne : {data.get('line_type')}")
        else:
            print("❌ Numéro invalide ou inconnu.")
    except Exception as e:
        print("⚠️ Erreur Numverify :", e)

   
    try:
        print("\n[📊 AbstractAPI] Données avancées...")
        url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        res = requests.get(url)
        data = res.json()

        if data.get('valid'):
            print(f"🌐 Opérateur : {data.get('carrier')}")
            print(f"📍 Région : {data.get('region')}")
            print(f"🕒 Fuseau horaire : {data.get('timezone')}")
            print(f"📱 Type : {data.get('type')}")
            print(f"📊 Format e164 : {data.get('format', {}).get('e164')}")
            print(f"🔢 Format international : {data.get('format', {}).get('international')}")
        else:
            print("❌ Numéro non valide (AbstractAPI).")
    except Exception as e:
        print("⚠️ Erreur AbstractAPI :", e)

    print("\n[🕵️ Truecaller] Recherche d'identité...")
    print("⚠️ Module non officiel Truecaller non intégré dans cette version (protection nécessaire).")

def main():
    print_discord_links()
    while True:
        print(ASCII_HEADER)
        print("==== PHONE LOOKUP V1 ====")
        print("1. Phone Lookup")
        print("0. Quitter")

        choice = input("Choix : ").strip()

        if choice == '1':
            phone_lookup()
        elif choice == '0':
            print("Bye!")
            break
        else:
            print("Choix invalide")

    input("\nAppuie sur Entrée pour quitter...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ Une erreur fatale s’est produite :", e)
        input("Appuie sur Entrée pour fermer...")
        sys.exit(1)
