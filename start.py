import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd

from segredos import get_infos_secretas


def ler_planilhas_emails() -> pd.DataFrame:
    df_msgs = pd.read_excel("email_tos.xlsx")

    return df_msgs


def gerar_msg(subject: str, body: str, _from: str, tos: str) -> str:
    msg = MIMEMultipart()
    msg["From"] = _from
    msg["To"] = tos
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    return msg.as_string()


def enviar_msgs(server: smtplib.SMTP, df_email: pd.DataFrame, _from: str) -> None:

    for _, msg_infos in df_email.iterrows():

        msg = gerar_msg(
            msg_infos["subject"],
            msg_infos["body"],
            _from,
            msg_infos["to"],
        )
        server.sendmail(_from, msg_infos["to"], msg)


def main():
    login, senha = get_infos_secretas()
    df_msgs = ler_planilhas_emails()

    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(login, senha)

        enviar_msgs(server, df_msgs, login)


if __name__ == "__main__":
    main()
