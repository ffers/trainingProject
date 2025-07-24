from infrastructure.api_clients.telegram import Telegram


def test_send_message(capsys):
    tg = Telegram()
    tg.sendMessage()
    captured = capsys.readouterr()
    assert "відсилаю повідомленя" in captured.out

