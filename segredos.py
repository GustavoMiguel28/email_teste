from typing import Tuple


def get_infos_secretas() -> Tuple[str, str]:
    email = "gustavo_pito@hotmail.com"
    senha = "ronaldinho"
    if not email:
        raise Exception("preencha seu email e senha!")
    return email, senha