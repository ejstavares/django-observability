from django.test import TestCase
from django.urls import reverse

from .models import Pessoa


class PessoaModelTest(TestCase):
    def test_str_returns_nome(self):
        pessoa = Pessoa.objects.create(nome="Ana", idade=30)

        self.assertEqual(str(pessoa), "Ana")


class PingViewTest(TestCase):
    def test_ping_returns_ok(self):
        response = self.client.get(reverse("ping"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")


class PessoaViewTest(TestCase):
    def test_save_creates_pessoa_and_redirects(self):
        response = self.client.post(reverse("save"), {"nome": "Joao", "idade": 25})

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Pessoa.objects.count(), 1)
        pessoa = Pessoa.objects.first()
        self.assertEqual(pessoa.nome, "Joao")
        self.assertEqual(pessoa.idade, 25)

    def test_delete_removes_pessoa(self):
        pessoa = Pessoa.objects.create(nome="Maria", idade=40)

        response = self.client.get(reverse("pessoa_delete", args=[pessoa.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Pessoa.objects.count(), 0)
