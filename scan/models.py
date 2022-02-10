from django.db import models

from django.db import connection


class Accounts(models.Model):
    address = models.CharField(max_length=300)
    balance = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.address} - {self.balance}'

    # def getAllUsers(self):
    #     raw_query = "SELECT * FROM scan_accounts"
    #     cursor = connection.cursor()
    #     cursor.execute(raw_query)
    #     cursor.fetchall()

