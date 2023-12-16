import os

def proxies():
    # Recebe entradas do usuário
    folder_name = input("Digite o nome da pasta: ")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    endpoint = input("Digite o ponto de extremidade: ")
    port = input("Digite a porta: ")

    # Conteúdo dos arquivos
    manifest_json = f"""
    {{
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Proxies",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {{
            "scripts": ["background.js"]
        }},
        "minimum_chrome_version":"22.0.0"
    }}
    """

    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
              singleProxy: {{
                scheme: "http",
                host: "{endpoint}",
                port: parseInt({port})
              }},
              bypassList: ["localhost"]
            }}
          }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{username}",
                password: "{password}"
            }}
        }};
    }}

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {{urls: ["<all_urls>"]}},
                ['blocking']
    );
    """

    # Cria a pasta se não existir
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Caminho completo para os arquivos
    manifest_path = os.path.join(folder_name, "manifest.json")
    background_path = os.path.join(folder_name, "background.js")

    # Salva os arquivos na pasta
    with open(manifest_path, "w") as manifest_file:
        manifest_file.write(manifest_json)

    with open(background_path, "w") as background_file:
        background_file.write(background_js)

    print(f"Pasta '{folder_name}' criada com sucesso.")

# Chamada da função
proxies()
