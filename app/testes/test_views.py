from .test_setup import TestSetUp
from django.contrib.auth.models import User

from ..models import Author


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(res.data["User"]['email'], self.user_data["email"])
        self.assertEqual(res.data["User"]['username'], self.user_data["username"])
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(
            self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 200)

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data["User"]['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_body_validation_error(self):
        import ipdb; ipdb.set_trace()
        data = {
            "author_id": Author.objects.first().id,
            "category": "Motivacional",
            "title": "A arte da procastinacao",
            "summary": " Se você é do tipo que reluta em entregar as coisas no prazo estabelecido, se distrai facilmente, navega na internet em vez de pagar as contas, ou é do tipo que compra o presente do seu amigo a caminho da festa, este livro vai mudar sua vida. ",
            "body": "Se você é do tipo que reluta em entregar as coisas no prazo estabelecido, se distrai facilmente, navega na internet em vez de pagar as contas, ou é do tipo que compra o presente do seu amigo a caminho da festa, este livro vai mudar sua vida.",

        }
        response = self.client.post(self.articles_list, data=data)
        self.assertEqual(response.status_code, 400)

    def test_body_validation(self):
        data = {
            "author_id": Author.objects.first().id,
            "category": "Motivacional",
            "title": "A arte da procastinacao",
            "summary": " Um guia prático sobre como otimizar seu tempo, deixando (quase) tudo para depois. Pode soar contrário ao senso comum, mas funciona: você pode realizar muitas coisas deixando-as para depois. Essa é a filosofia apresentada no livro A arte da procrastinação. ",
            "first_paragraph": " Se você é do tipo que reluta em entregar as coisas no prazo estabelecido, se distrai facilmente, navega na internet em vez de pagar as contas, ou é do tipo que compra o presente do seu amigo a caminho da festa, este livro vai mudar sua vida. ",
            "body": " Se você é do tipo que reluta em entregar as coisas no prazo estabelecido, se distrai facilmente",

        }
        response = self.client.post(self.articles_list, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["body"], data["body"])
        self.assertEquals(response.data["author"]["id"], str(data["author_id"]))