# mail/mail.py
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path
from typing import Optional, List, Union


class MyMail:
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int = 587,
        username: Optional[str] = None,
        password: Optional[str] = None,
        use_tls: bool = True,
        use_ssl: bool = False,
    ):
        """
        Inicializace mailového klienta.
        
        :param smtp_server: SMTP server (např. 'smtp.gmail.com')
        :param smtp_port: port (587 pro TLS, 465 pro SSL, 25 pro nešifrované)
        :param username: uživatelské jméno pro přihlášení
        :param password: heslo (doporučeno: App Password pro Gmail)
        :param use_tls: použít STARTTLS (výchozí pro port 587)
        :param use_ssl: použít SSL připojení (výchozí pro port 465)
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.use_ssl = use_ssl

    def send_email(
        self,
        sender: str,
        recipients: Union[str, List[str]],
        subject: str,
        text_content: str,
        html_content: Optional[str] = None,
        attachments: Optional[List[str]] = None,
    ) -> bool:
        """
        Odešle email s podporou textu, HTML a příloh.
        
        :param sender: odesílatel (např. "ja@example.com")
        :param recipients: příjemce nebo seznam příjemců
        :param subject: předmět emailu
        :param text_content: tělo emailu jako prostý text
        :param html_content: volitelné HTML tělo
        :param attachments: seznam cest k souborům (např. ["report.pdf"])
        :return: True při úspěchu
        :raises: Exception při chybě
        """
        # Normalizace příjemců na seznam
        if isinstance(recipients, str):
            recipients = [recipients]

        # Vytvoření zprávy
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg["Message-ID"] = make_msgid()

        # Přidání obsahu
        if html_content:
            msg.set_content(text_content)
            msg.add_alternative(html_content, subtype="html")
        else:
            msg.set_content(text_content)

        # Přílohy
        if attachments:
            for file_path in attachments:
                path = Path(file_path)
                if not path.is_file():
                    raise FileNotFoundError(f"Soubor neexistuje: {file_path}")
                with open(path, "rb") as f:
                    file_data = f.read()
                    mime_type = self._guess_mime_type(path)
                    maintype, subtype = mime_type.split("/", 1) if "/" in mime_type else ("application", "octet-stream")
                    msg.add_attachment(
                        file_data,
                        maintype=maintype,
                        subtype=subtype,
                        filename=path.name,
                    )

        # Odeslání
        try:
            if self.use_ssl:
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    if self.username and self.password:
                        server.login(self.username, self.password)
                    server.send_message(msg, sender, recipients)
            else:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    if self.use_tls:
                        server.starttls()
                    if self.username and self.password:
                        server.login(self.username, self.password)
                    server.send_message(msg, sender, recipients)
            return True
        except Exception as e:
            raise RuntimeError(f"Chyba při odesílání emailu: {e}") from e

    @staticmethod
    def _guess_mime_type(path: Path) -> str:
        """Jednoduchý odhad MIME typu podle přípony."""
        suffix = path.suffix.lower()
        types = {
            ".pdf": "application/pdf",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".txt": "text/plain",
            ".html": "text/html",
            ".csv": "text/csv",
            ".json": "application/json",
            ".zip": "application/zip",
        }
        return types.get(suffix, "application/octet-stream")