import imaplib

import pyzmail
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from email_integration.models import EmailAccount, EmailMessage


def import_emails():
    channel_layer = get_channel_layer()
    accounts = EmailAccount.objects.all()

    for account in accounts:
        if account.provider == 'gmail':
            host = 'imap.gmail.com'
        elif account.provider == 'yandex':
            host = 'imap.yandex.ru'
        elif account.provider == 'mailru':
            host = 'imap.mail.ru'
        else:
            continue

        mail = imaplib.IMAP4_SSL(host)
        mail.login(account.email, account.password)
        mail.select('inbox')
        status, data = mail.search(None, 'ALL')

        all_messages = data[0].split()
        total_messages = len(all_messages)
        processed_messages = 0

        for num in all_messages[:50]:  # Ограничиваем обработку первыми 50 сообщениями
            status, data = mail.fetch(num, '(RFC822)')
            message = pyzmail.PyzMessage.factory(data[0][1])

            attachments = []
            if message.mailparts:
                for part in message.mailparts:
                    if part.filename:
                        file_name = part.filename
                        file_data = part.get_payload()
                        attachments.append(file_name)

            sent_date = message.get_decoded_header('date')
            received_date = message.get_decoded_header('date')

            body = message.text_part.get_payload().decode(message.text_part.charset) if message.text_part else ''
            subject = message.get_subject()

            email_message = EmailMessage.objects.create(
                email_account=account,
                subject=subject,
                sent_date=sent_date,
                received_date=received_date,
                body=body,
                attachments=attachments
            )

            processed_messages += 1
            progress = (processed_messages / 50) * 100
            async_to_sync(channel_layer.group_send)(
                'email_import',
                {
                    'type': 'email_import_progress',
                    'message': f'Processed {processed_messages} of 50 messages for account {account.email}',
                    'progress': progress
                }
            )

            # Отправляем сообщение о загрузке каждого сообщения
            async_to_sync(channel_layer.group_send)(
                'email_import',
                {
                    'type': 'email_import_message',
                    'message': {
                        'subject': email_message.subject,
                        'sent_date': email_message.sent_date,
                        'received_date': email_message.received_date,
                        'body': email_message.body,
                        'attachments': email_message.attachments
                    }
                }
            )

        mail.close()
        mail.logout()