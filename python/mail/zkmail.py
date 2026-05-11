from mail_api import MyMail
from pathlib import Path
# Inicializace
for i in range(100):
    mailer = MyMail(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        username="pelcsamuel464@gmail.com",
        password="tqsgzerahhpjmshd",  # ⚠️ nikdy nepoužívej běžné heslo u Gmailu!
        use_tls=True,
    )

    # Odeslání
    try:
        success = mailer.send_email(
            sender="pelcsamuel464@gmail.com",
            recipients=["pelcsamuel464@gmail.com"],
            subject="Testovací email",
            text_content="Ahoj, toto je test.",
            html_content="""
            <html>
            <body>
                <h1>Test!</h1>
                <p>Ahoj, toto je testovací email bez přílohy.</p>
                <p>Funguje</p>
            </body>
            </html>
            """,
        )
        if success:
            print("✅ Email úspěšně odeslán.")
    except Exception as e:
        print(f"❌ Selhalo: {e}")
